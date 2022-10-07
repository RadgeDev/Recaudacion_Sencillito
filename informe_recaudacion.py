import os
import glob
import xlwt
import pymysql.cursors
from xlwt import Workbook 
from datetime import date
from datetime import datetime, timedelta


wb = Workbook() 

connection = pymysql.connect(host='',
                             user='',
                             password="",
                             db='',
                             cursorclass=pymysql.cursors.DictCursor)

# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1') 
sheet1.write(0, 0, 'RECAUDACION SENCILLITO RECEPCIONADA')
sheet1.write(1, 0, 'RUT')
sheet1.write(1, 1, 'VALE')
sheet1.write(1, 2, 'MONTO')
sheet1.write(1, 3, 'FECHA')
sheet1.write(1, 4, 'HORA')

sheet1.write(0, 7, 'RECAUDACION CYD INGRESADA')
sheet1.write(1, 7, 'RUT')
sheet1.write(1, 8, 'VALE')
sheet1.write(1, 9, 'TRANSAC')
sheet1.write(1, 10, 'MONTO')
sheet1.write(1, 11, 'FECHA')
sheet1.write(1, 12, 'HORA')
i= 1
d = datetime.today() - timedelta(days=1)

rutarecaudacion = "D:\\sencillito\\RECAUDACIONDIARIACYD"
for namefile in glob.glob(os.path.join(rutarecaudacion, '*.txt')):
    with open(namefile, "r") as fichero:
        for linea in fichero:
            if str(linea[:-12]) != "Sin Recaudacion":
                rut = str(linea[1:-35])
                dig = str(linea[9:-34])
                rutcom = str(linea[1:-35]) + '-' + str(linea[9:-34])
                n_documento = str(linea[10:-24])
                monto = str(linea[20:-15])
                fechahora = str(linea[29:-1])
                fecha = str(linea[29:-7])
                hora = str(linea[37:-1])
                horaformat = str(hora[:2] + ':' + hora[2:-2] + ':' + hora[4:])
                fechaformat = str(fecha[:4] + '-' + fecha[4:-2] + '-' + fecha[6:])
               
                d2 = datetime.strptime(str(fechaformat), '%Y-%m-%d')
                d2 = d2.strftime('%Y-%m-%d')
                d1 = d.strftime('%Y-%m-%d')
                if d2 >= d1 :
                    i = i + 1
                    sheet1.write(i, 0, str(rutcom)) 
                    sheet1.write(i, 1, int(n_documento)) 
                    sheet1.write(i, 2, int(monto)) 
                    sheet1.write(i, 3, str(fechaformat)) 
                    sheet1.write(i, 4, str(horaformat)) 
                    wb.save('D:\\excels\\recaudacioncyd_'+ d.strftime("%Y-%m-%d") + '.xls') 
            else:
                print("SIN RECAUDACION ARCHIVO  " + str(linea))


with connection.cursor() as cursor:
        # Prepare SQL query to select a record into the database.
        try:
            i = 1
            fec = str(d.strftime("%Y-%m-%d"))
            txt_sql = "SELECT rut,monto,voucher,transac,fecha,hora FROM pagos_sencillito WHERE fecha >= '" + str(fec) +"' and estado = 'ABONADO' ;"
            # Execute the SQL command                            
            cursor.execute(txt_sql)
            row_count = cursor.rowcount
            if row_count > 0:
               results = cursor.fetchall()
               for index in results:
                    rut = str(index['rut'])
                    monto = int(index['monto'])
                    voucher = int(index['voucher'])
                    transac = int(index['transac'])
                    fecha = str(index['fecha'])
                    hora = str(index['hora'])
                    i = i + 1
                    sheet1.write(i, 7, str(rut)) 
                    sheet1.write(i, 8, int(voucher)) 
                    sheet1.write(i, 9, int(transac)) 
                    sheet1.write(i, 10, int(monto)) 
                    sheet1.write(i, 11, str(fecha)) 
                    sheet1.write(i, 12, str(hora))
                    wb.save('D:\\excels\\recaudacioncyd_'+ d.strftime("%Y-%m-%d") + '.xls')
            cursor.close()
        except:
            print("Error: No hay datos verificar")
            cursor.close()
            connection.close()






