
import pymysql.cursors
import datetime
import os,time
import subir_file


# Open database connection
connection = pymysql.connect(host='',
                             user='',
                             password='',
                             db='',
                             cursorclass=pymysql.cursors.DictCursor)
# prepare a cursor object using cursor() method
with connection.cursor() as cursor:

    try:

        sql = "CALL GET_EECC_SENCILLITO()"
# Execute the SQL command
        cursor.execute(sql)
# Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        if results:
            todays_date = datetime.datetime.now()
            filename = 'CYD' + todays_date.strftime('%Y%m%d%H%M%S') + '.txt'
            savepath="D:\\sencillito\\ARCHIVO SUBIR"
            completeName = os.path.join(savepath, filename)
            newfile = open(completeName, "w")
        for index in results:
            ltr = []
            ltr.append(index['rut'] + str(','))
            ltr.append(index['verificador'] + str(','))
            ltr.append(str(round(index['folio'])) + str(','))
            ltr.append(index['nombre'] + str(','))
            ltr.append(str(round(index['tot_pagar'])) + str(','))
            ltr.append(index['fecha_ven'])
            lenltr = len(ltr)
            for i in range(lenltr):
                newfile.write('{}'.format(ltr[i]))
            newfile.write("\n")

        newfile.close()
        cursor.close()
        connection.close()
        print("ARCHIVO DEUDA EECC  CREADO")
        time.sleep(5)
        subir_file.subir_archivo()

    except Exception as e:
        print(e.message)
        print("ERROE CARGA DIARIA EECC")
