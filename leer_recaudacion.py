import os
import glob
import tcp
import mover_txt
import bajar_file
import conexion
import conexion_abono


bajar_file.bajar_archivo_rendicion()
mover_txt.validar_archivo_bajado()
rutarecaudacion = "D:\\sencillito\\ARCHIVO BAJAR\\"

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
                if rut != "" and monto != "" and fechahora != "":
                    conexion_abono.insertar_recaudacion(rutcom, int(n_documento), int(monto), fechaformat, horaformat,'EN PROCESO')
                else:
                    print("SIN RECAUDACION ARCHIVO  " + str(linea))
        


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
                horatrans = str(hora[:2] + ':' + hora[2:-2])
                fechaformat = str(fecha[:4] + '-' + fecha[4:-2] + '-' + fecha[6:])
                if rut != "" and monto != "" and fechahora != "":
                    cartera = conexion_abono.tipo_cartera(rutcom)
                    mtran = conexion_abono.obtener_nabono()
                    
                    if cartera == False :
                     
                        conexion_abono.insertar_transac(mtran,rutcom,int(monto),fechaformat,horatrans)
                        conexion_abono.insertar_eecc(rutcom,int(monto),mtran,fechaformat)
                        conexion_abono.actualiza_mora(rutcom, int(monto),mtran)
                        conexion_abono.actualiza_tramo(rutcom,int(monto))
                        conexion_abono.actualiza_tblaut(rutcom,int(monto))
                        conexion_abono.actualiza_ultpago(rutcom)
                        conexion_abono.verificar_pago(rutcom, fechaformat, int(monto), int(n_documento), mtran)
                        conexion_abono.trae_excusa(rutcom,mtran,cartera)
                        conexion_abono.trae_fecha_evaluacion(rutcom,mtran)

                    else:

                        conexion_abono.insertar_transac(mtran,rutcom,int(monto),fechaformat,horatrans)
                        conexion_abono.pago_vencida(rutcom,int(monto),mtran,fechaformat)
                        conexion_abono.asignaciones_vencida(rutcom,int(monto))
                        conexion_abono.actualiza_ultpago(rutcom)
                        foliox = conexion_abono.ObtieneFolioAPagar(rutcom)
                        if  foliox != 0:
                            conexion_abono.pago_repactacionvencida(rutcom, int(monto),foliox)

                        conexion_abono.trae_excusa(rutcom,mtran,cartera)
                        conexion_abono.trae_fecha_evaluacion(rutcom,mtran)
                        conexion_abono.verificar_pago(rutcom, fechaformat, int(monto), int(n_documento), mtran)






                else:
                    print("SIN RECAUDACION ARCHIVO  " + str(linea))








