import pymysql.cursors


# Open database connection
connection = pymysql.connect(host='',
                             user='',
                             password="",
                             db='',
                             cursorclass=pymysql.cursors.DictCursor)


def obtener_tarpan(rut):

    with connection.cursor() as cursor:
        # Prepare SQL query to select a record into the database.
        try:
            sql = "select Tar_pan from tarjeta where Cli_Rut =" + rut +""

            # Execute the SQL command
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            for index in results:
                tarpan = str(index['Tar_pan'])
            cursor.close()
            return tarpan

        except:
            print("Error: No hay datos tarpan")
            connection.close()


def insertar_recaudacion(rut, voucher, monto, fecha, hora, estado):

    with connection.cursor() as cursor:
        # Prepare SQL query to select a record into the database.
        try:
            if rut !="" and monto !="" and fecha !="" and hora !="" and estado !="":
                sql = "INSERT INTO pagos_sencillito (rut,voucher ,monto, fecha, hora,estado)" \
                     " VALUES ((%s),(%s),(%s),(%s),(%s),(%s))"
                args = (rut, voucher, monto, fecha, hora, estado,)
                cursor.execute(sql, args)
                connection.commit()
                cursor.close()
                print("DATOS '" +rut + "' INSERTADOS EN PAGOS ENCILLITO")

        except:
            print("Error: No hay datos insert recaudacion")
            connection.close()


def verificar_pago(rut, fecha, monto, voucher, ntrans):

    with connection.cursor() as cursor:
        # Prepare SQL query to select a record into the database.
        try:
            txt_sql = "SELECT count(rut) as contador FROM abonos"
            txt_sql += " where rut = '" + rut + "' and fec_tran = '" + fecha + "' and "
            txt_sql += " n_tran = " + str(ntrans) + " and mont_tran = " + str(monto) + " and TIP_TRAN = 3"
            # Execute the SQL command
            cursor.execute(txt_sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            for index in results:
                contador = int(index['contador'])

            if int(contador) == 0:
                txt_sql = " UPDATE pagos_sencillito  SET  estado = 'ERROR NO PAGO' WHERE rut = (%s) and voucher = (%s)"
                cursor.execute(txt_sql, (rut, voucher))
                connection.commit()
            else:
                txt_sql = "UPDATE pagos_sencillito  SET estado = 'ABONADO' ,transac = (%s) WHERE rut = (%s)" \
                          " and voucher = (%s)"
                cursor.execute(txt_sql, (ntrans, rut, voucher))
                connection.commit()
            print("DATOS VERIFICADOS")
            cursor.close()
        except:
            print("Error: No hay datos verificar")
            cursor.close()
            connection.close()


#insertar_recaudacion(str('44444444-4'), 1235,100, str('2019-03-24'), str('08:00:00'), str('abonado'))
#verificar_pago('44444444-4', '2019-04-26', 103, 1235, 1020929)
