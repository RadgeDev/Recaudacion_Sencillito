import pymysql.cursors
from datetime import date
from datetime import datetime, timedelta


# Open database connection
connection = pymysql.connect(host='',
                             user='',
                             password="",
                             db='',
                             cursorclass=pymysql.cursors.DictCursor)



def obtener_nabono():

    with connection.cursor() as cursor:
        # Prepare SQL query to select a record into the database.
        try:
            sql = "SELECT Num_Abono  FROM Numero_Abono"

            # Execute the SQL command
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            for index in results:
                n_abo = int(index['Num_Abono'])
            if n_abo != None:
               txt_sql = " UPDATE Numero_Abono  SET  Num_Abono =(%s)"
               cursor.execute(txt_sql, (int(n_abo + 1)))
               connection.commit()
               print(n_abo)
            else:
                n_abo= 0


           # cursor.close()
            return n_abo

        except pymysql.err.ProgrammingError as except_detail:
               print("pymysql.err.ProgrammingError: «{}»".format(except_detail))
        finally:
               cursor.close()
              

def obtener_nid(rutx):

    with connection.cursor() as cursor:
        # Prepare SQL query to select a record into the database.
        try:
            sql = "SELECT MAX(id) as id  FROM pagos_sencillito where rut = '" + str(rutx) + "' "

            # Execute the SQL command
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            for index in results:
                n_id =  int(vnulo(index['id']))
      
            return n_id

        except pymysql.err.ProgrammingError as except_detail:
               print("pymysql.err.ProgrammingError: «{}»".format(except_detail))
        finally:
               cursor.close()

    
def insertar_recaudacion(rut, voucher, monto, fecha, hora, estado):
    
    with connection.cursor() as cursor:
        # Prepare SQL query to select a record into the database.
        try:
            if rut !="" and monto !="" and fecha !="" and hora !="" and estado !="":
                sql = "INSERT INTO pagos_sencillito (rut,voucher ,monto, fecha, hora,estado)" \
                     " VALUES ((%s),(%s),(%s),(%s),(%s),(%s))"
                args = (rut, voucher, monto, fecha, hora, estado)
                cursor.execute(sql, args)
                connection.commit()
               # cursor.close()
                print("DATOS '" +rut + "' INSERTADOS EN PAGOS SENCILLITO")

        except pymysql.err.ProgrammingError as except_detail:
               print("pymysql.err.ProgrammingError: «{}»".format(except_detail))
        finally:
               cursor.close()
              

def insertar_transac(ntran, rutx, monto,fecha,hora):
    d = datetime.today()
    with connection.cursor() as cursor:
        # Prepare SQL query to select a record into the database.
        try:
            if rutx !="" and monto !="" and ntran !="" :
                sql = "INSERT INTO Transac (Tip_Tran,N_Tran ,Rut, Fec_Tran, Ho_Tran,Usu_Tran,N_Maqui,Lug_Tran,Comer_Tran,Mont_Tran)" \
                     " VALUES ((%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s))"
                args = (3, ntran, rutx,fecha, hora, 'SENCILLITO',67,1,2,monto)
                cursor.execute(sql, args)
                connection.commit()
                print("DATOS '" +rutx + "' INSERTADOS EN PAGOS ENCILLITO")


        except pymysql.err.ProgrammingError as except_detail:
               print("pymysql.err.ProgrammingError: «{}»".format(except_detail))
        finally:
               cursor.close()
              


def insertar_abonos(ntran,rutx, monto,fecha,folio,fecv,ag,abmopr,aboge,abperi,aboman,abinp,abenvi,abseg,abcomi,abdico,abcorr,abeva,abocap,pg):
    with connection.cursor() as cursor:
        # Prepare SQL query to select a record into the database.
        try:
            if rutx !="" and monto !="" and ntran !="" :
                sql = "INSERT INTO abonos (Tip_Tran , N_Tran , Rut,  Fec_Tran,  Mont_Tran, fol_eecc, f_venc, Abo_Gascob, Abo_Mopro, Abo_Gcgene," \
                     "Abo_Moperi, Abo_Moante, Abo_Impu, Abo_Envi, Abo_Segu, Abo_Comi, Abo_Dico, Abo_Corri, Abo_Evalu, Abo_Capi, Pgpaplicar, PAGO) "\
                     " VALUES ((%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s))"
                args = (3, ntran, rutx,fecha, monto,folio,fecv,ag,abmopr,aboge,abperi,aboman,abinp,abenvi,abseg,abcomi,abdico,abcorr,abeva,abocap,pg,'NO' )
                cursor.execute(sql, (args))
                connection.commit()
               # cursor.close()
                print("DATOS '" +rutx + "' INSERTADOS EN ABONOS")

        except pymysql.err.ProgrammingError as except_detail:
               print("pymysql.err.ProgrammingError: «{}»".format(except_detail))
        finally:
               cursor.close()
              

def pagos_abonovencida(ntran,rutx, monto,fecha,abogas,aboint,abokap):
    with connection.cursor() as cursor:
        # Prepare SQL query to select a record into the database.
        try:
            if rutx !="" and monto !="" and ntran !="" :
                sql = "INSERT INTO abonos (Tip_Tran, N_Tran, N_Cuenta, Rut, Fec_Tran, Mont_Tran, Fol_Eecc, Fec_Conta, Abo_Gascob, Abo_Moperi "
                sql +=  ", Abo_Moante, ESTADO)"
                sql +=  " VALUES ((%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s))"

                args = (3, ntran, rutx,rutx,fecha, monto,0,fecha,abogas,aboint,abokap,'VENCIDA')
                cursor.execute(sql, (args))
                connection.commit()
                #cursor.close()
                print("DATOS '" + rutx + "' INSERTADOS EN ABONOS")

        except pymysql.err.ProgrammingError as except_detail:
               print("pymysql.err.ProgrammingError: «{}»".format(except_detail))
        finally:
               cursor.close()
              


def pagar_sal_venc(rutx, fechabox,sal_capix,gascobx,interex,saldox,m_abonox,saldo_finx,abo_gastox,abo_intex,abo_venx):
    with connection.cursor() as cursor:
        # Prepare SQL query to select a record into the database.
        try:
            if rutx !="" and fechabox !="" and sal_capix !="" :
                sql = " INSERT INTO sal_venc (rut,fecha_abon,saldo_capi,gas_cobra,intereses,saldo,m_abono,saldo_fin,abo_gasto,abo_inte,abo_ven)"
                sql +=  " VALUES ((%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s))"
                args = (rutx, fechabox,sal_capix,gascobx,interex,saldox,m_abonox,saldo_finx,abo_gastox,abo_intex,abo_venx)
                cursor.execute(sql, (args))
                connection.commit()
              #  cursor.close()
                print("DATOS '" + rutx + "' INSERTADOS EN ABONOS")

        except pymysql.err.ProgrammingError as except_detail:
               print("pymysql.err.ProgrammingError: «{}»".format(except_detail))
        finally:
               cursor.close()
              


def pago_repactacionvencida(rutx, montox,folioxxx):

    foliox = folioxxx
    global estadox
    with connection.cursor() as cursor:
        # Prepare SQL query to select a record into the database.
       
        try:
            montopagar = montox
            montopagarx = montox
            if rutx !="" and montox !="" and foliox !="" and  foliox != 0 :
                d = datetime.today()
                mifecha  = d.strftime("%Y-%m-%d %H:%M:%S")
                sql = " INSERT INTO Pago_Repactacion (Rut,folio,montopago,fechapago,usuarioPago) "
                sql +=  " VALUES ((%s),(%s),(%s),(%s),(%s))"
                args = (rutx, foliox , montox ,mifecha ,'SENCILLITO')
                cursor.execute(sql, (args))
                connection.commit()

                print("DATOS '" + rutx + "' INSERTADOS EN Pago_Repactacion")
                sql = "SELECT  * FROM detalle_Repactacion where folio = " + str(foliox) + " "
                # Execute the SQL command
                rows_count = cursor.execute(sql)
                # Fetch all the rows in a list of lists.
                if rows_count > 0  and montox > 0:
                     results = cursor.fetchall()
                     for index in results:
                        salreal = int(vnulo(index['saldo_real']))
                        abono_monto = int(vnulo(index['abono_monto']))
                        n_cuotax = int(vnulo(index['n_cuota']))
                        if salreal > 0:
                            if montox >= salreal:
                                abono_monto = abono_monto + salreal
                                montox =  montox - salreal
                                salreal = 0
                                estado = "PAGADA"
                            else:
                                abono_monto = abono_monto + montox
                                salreal = salreal - montox
                                montox = 0
                                estado = "PAGO PARCIAL"
                     
                            txt_sql = " UPDATE detalle_Repactacion  SET  abono_monto = (%s), saldo_real = (%s),Estado = (%s)"
                            txt_sql += " WHERE folio = (%s)   and n_cuota = (%s) "
                            cursor.execute(txt_sql, (abono_monto,salreal,estado, foliox,n_cuotax))
                            connection.commit()
                            if montox == 0:
                                break

                flagbandera = False
                #4to Paso actualizar el encabezado de la repactacion
          
                sql = "SELECT * FROM encabezado_Repactacion"
                sql += " WHERE folio = " + str(foliox) + " "
                rows_count = cursor.execute(sql)
                # Fetch all the rows in a list of lists.
                if rows_count > 0 :
                    montoapagar = montopagarx
                    results = cursor.fetchall()
                    for index in results:
                        deudafinal = int(vnulo(index['deuda_final']))
                        pie = int(vnulo(index['pie']))
                        abonospie = int(vnulo(index['abonos_pie']))
                        saldo = int(vnulo(index['saldo']))
                        abonos_saldo = int(vnulo(index['abonos_saldo']))

                    deudafinal = deudafinal - montoapagar
                    fechaUltimoAbono  = d.strftime("%Y-%m-%d")
                    if pie > abonospie:
                        if montoapagar >= (pie - abonos_pie):
                            montoapagar = montoapagar - (pie - abonos_pie)
                            abonospie = pie
                            if deudafinal <= 0:
                                estadox = 'PAGADA'
                                flagbandera = True
                                condonacionpago(rutx)
                        else:
                            abonospie = abonospie + montoapagar
                            montoapagar = 0
                            if deudafinal <= 0:
                                estadox = 'PAGADA'
                                flagbandera = True
                                condonacionpago(rutx)
                    
                        if montoapagar > 0:
                            if montoapagar >= saldo - abonos_saldo:
                                montoapagar = 0
                                abonos_saldo = saldo
                                estadox = "PAGADA"
                                deudafinal = 0
                                flagbandera = True
                            #inserto condonacion
                                condonacionpago(rutx)
                            else:
                                abonos_saldo = abonos_saldo + montoapagar
                                montoapagar = 0
                                estadox = "VIGENTE"
                    else:
                        if saldo > abonos_saldo:
                            if montoapagar >= saldo - abonos_saldo:
                                montoapagar = 0
                                abonos_saldo = saldo
                                estadox = "PAGADA"
                                deudafinal = 0
                                flagbandera = True
                                #inserto condonacion
                                condonacionpago(rutx)
                            else:
                                abonos_saldo = abonos_saldo + montoapagar
                                montoapagar = 0
                                estadox = "VIGENTE"
                        else:
                            montoapagar = 0
                            abonos_saldo = saldo
                            estadox = "PAGADA"
                            deudafinal = 0
                            flagbandera = True
                           #inserto condonacion
                            condonacionpago(rutx)
                    
                    txt_sql = " UPDATE encabezado_repactacion  SET  deuda_final = (%s), abonos_pie = (%s),Estado = (%s) ,abonos_saldo = (%s)"
                    txt_sql += " WHERE folio = (%s) "
                    cursor.execute(txt_sql, (deudafinal,abonospie,estadox, abonos_saldo,foliox))
                    connection.commit()


                    #flagbandera = False
                    if flagbandera == False:
                       sql = "SELECT Min(vencimiento) as fecha, n_cuota FROM Detalle_Repactacion"
                       sql += " WHERE folio = " + str(foliox) + " AND estado <> 'PAGADA' GROUP BY n_cuota ORDER BY n_cuota ASC LIMIT 1"
                       rows_count = cursor.execute(sql)
                       if rows_count > 0:
                            results = cursor.fetchall()
                            for index in results:
                                vfecha = index['fecha']
                                ncuotax = int(vnulo(index['n_cuota']))

                            mifecha  = d.strftime("%Y-%m-%d")
                            vfecha =  vfecha.strftime("%Y-%m-%d")
                            fvenci = datetime.strptime(vfecha, "%Y-%m-%d")
                            fhoy = datetime.strptime(mifecha, "%Y-%m-%d")
                            if fhoy > fvenci and ncuotax != 0:
                                estadoxx = 'ATRASADA'
                            else:
                                if ncuotax ==  0:
                                    estadoxx = 'GENERADA'
                                else:
                                    estadoxx = 'VIGENTE'
                            
                            txt_sql = " UPDATE encabezado_repactacion  SET  Estado = (%s) , FechaUltimoAbono = (%s)  "
                            txt_sql += " WHERE folio = (%s) "
                            cursor.execute(txt_sql, (estadoxx,mifecha,foliox))
                            connection.commit()
                       
            
        except pymysql.err.ProgrammingError as except_detail:
               print("pymysql.err.ProgrammingError: «{}»".format(except_detail))
        finally:
                cursor.close()






       
def date_dif(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)


def condonacionpago(rutx):
    with connection.cursor() as cursor:
        # Prepare SQL query to select a record into the database.
        try:
            sql = "SELECT SALDO,INTE_DIA,SALDO_INTE,SAL_GASTOS FROM vencida "
            sql += " WHERE rut = '" + str(rutx) + "' "
            rows_count = cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            if rows_count > 0 :
                results = cursor.fetchall()
                for index in results:
                    Saldo =    int(vnulo(index['SALDO']))
                    INTE_DIA = int(vnulo(index['INTE_DIA']))
                    SALDO_INTE = int(vnulo(index['SALDO_INTE']))
                    SAL_GASTOS = int(vnulo(index['SAL_GASTOS']))
                    deuda = (Saldo + INTE_DIA + SALDO_INTE + SAL_GASTOS)
            else:
                deuda = 0
    
            d = datetime.today()
            mifecha  = d.strftime("%Y-%m-%d")
            sql =  "INSERT INTO detalle_cargos (rut,fecha,monto,tip_cargo,usuario,porcentaje, observacion)"
            sql += " VALUES ((%s),(%s),(%s),(%s),(%s),(%s),(%s))"
            args = (rutx, mifecha ,deuda ,1,'SENCILLITO',100,'CONDONACION AUTOMATICA')
            cursor.execute(sql, (args))
            connection.commit()

            sql = " UPDATE VENCIDA  SET  INTE_DIA = (%s), SALDO = (%s), SALDO_INTE = (%s), SAL_GASTOS = (%s), GAS_COBRA = (%s) "
            sql += " WHERE rut = (%s) "
            cursor.execute(sql, (0,0,0,0,0,rutx))
            connection.commit()


        except pymysql.err.ProgrammingError as except_detail:
               print("pymysql.err.ProgrammingError: «{}»".format(except_detail))
        finally:
               cursor.close()
              

def pago_vencida(rutx,montox,ntran,fechatr):
    with connection.cursor() as cursor:
        # Prepare SQL query to select a record into the database.
        try:
             d = datetime.today()
             mifecha  = d.strftime("%Y-%m-%d")
             abogas = 0
             aboint = 0
             abokap = 0
             abosalint = 0
             montopag = montox
             sql = "SELECT * FROM Vencida WHERE rut = '" + rutx +"'"
             
             rows_count = cursor.execute(sql)
             # Fetch all the rows in a list of lists.
             if rows_count > 0 :
                results = cursor.fetchall()
                for index in results:
                  salgastos   = int(vnulo(index['SAL_GASTOS']))
                  intedia     = int(vnulo(index['INTE_DIA']))
                  saldointe   = int(vnulo(index['SALDO_INTE']))
                  saldo       = int(vnulo(index['SALDO']))
                  abonox    = int(vnulo(index['ABONOS']))
              
                if salgastos !="" and intedia !="" and saldo !="" :

                   salgas = salgastos
                   salint = saldointe
                   intedia = intedia
                   salkap = saldo

                 #paga saldo gastos
                if salgastos > 0:
                    if montox >= salgastos:
                        abogas = salgastos
                        montox = montox - salgastos
                        salgastos = 0
                    else:
                         abogas = montox
                         salgastos = salgastos - montox
                         montox = 0
                #paga saldo interes pendiente
                if saldointe > 0:
                    if montox >= saldointe:
                        abosalint = saldointe
                        montox = montox - saldointe
                        saldointe = 0
                    else:
                        abosalint = montox
                        saldointe = saldointe - montox
                        montox = 0
                #paga saldo interes actual
                if intedia > 0:
                    if montox >= intedia:
                        aboint = intedia
                        montox = montox - intedia
                        intedia = 0
                    else:
                        aboint = montox
                        intedia = intedia - montox
                        montox = 0
                
               #paga saldo capital
                if saldo > 0:
                    if montox >= saldo:
                        abokap = saldo
                        abonox = abonox + saldo
                        montox = montox - saldo
                        saldo = 0
                    else:
                        abokap = montox
                        saldo = saldo - montox
                        abonox = abonox + abokap
                        montox = 0
                
                aboint = aboint + abosalint

                txt_sql = " UPDATE Vencida  SET  saldo_inte = (%s), INTE_DIA = (%s),SAL_GASTOS = (%s),Saldo = (%s),abonos = (%s),dias_ulabo = (%s)"
                txt_sql += " WHERE rut = (%s) "
                cursor.execute(txt_sql, (saldointe,intedia,salgastos,saldo,abonox,mifecha, rutx))
                connection.commit()
                cursor.close()
                pagos_abonovencida(ntran,rutx, montopag,fechatr,abogas,aboint,abokap)
                saldofin = (salkap + salgas + salint)
                salabo =  (salkap + salgas + salint) - montopag
                pagar_sal_venc(rutx, mifecha,salkap,salgas,salint,saldofin,montopag,salabo,abogas,aboint,abokap)
                print("DATOS '" + rutx + "' MODIFICADOS EN  VENCIDA")

        except pymysql.err.ProgrammingError as except_detail:
               print("pymysql.err.ProgrammingError: «{}»".format(except_detail))
        finally:
               cursor.close()
              


def insertar_eecc(rutx,montcan,ntranx,fechaxf):

    with connection.cursor() as cursor:
        # Prepare SQL query to select a record into the database.
        try:
             ntran = ntranx
             connection.open
             sql = "SELECT *  FROM eecc where rut = '" + rutx +"'"
             rows_count = cursor.execute(sql)
            # Fetch all the rows in a list of lists.
             if rows_count > 0 :
             # Execute the SQL command
                #cursor.execute(sql) 
             # Fetch all the rows in a list of lists.
                results = cursor.fetchall()
                for index in results:
                    salante   = int(vnulo(index['SAL_ANTE']))
                    abomoante = int(vnulo(index['ABO_MOANTE']))
                    mongascob = int(vnulo(index['MON_GASCOB']))
                    monmopro  = int(vnulo(index['MON_MOPRO']))
                    abomopro  = int(vnulo(index['ABO_MOPRO']))
                    abogascob = int(vnulo(index['ABO_GASCOB']))
                    mongene   = int(vnulo(index['MON_GCGENE']))
                    abogene   = int(vnulo(index['ABO_GCGENE']))
                    monmoperi = int(vnulo(index['MON_MOPERI']))
                    abomoperi = int(vnulo(index['ABO_MOPERI']))
                    monimpu   = int(vnulo(index['MON_IMPU']))
                    aboimpu   = int(vnulo(index['ABO_IMPU']))
                    monenvi   = int(vnulo(index['MON_ENVIO']))
                    aboenvi   = int(vnulo(index['ABO_ENVI']))
                    monsegu   = int(vnulo(index['MON_SEGU']))
                    abosegu   = int(vnulo(index['ABO_SEGU']))
                    moncomi   = int(vnulo(index['MON_COMI']))
                    abocomi   = int(vnulo(index['ABO_COMI']))
                    mondico   = int(vnulo(index['MON_DICO']))
                    abodico   = int(vnulo(index['ABO_DICO']))
                    moncorri  = int(vnulo(index['MON_CORRI']))
                    abocorri  = int(vnulo(index['ABO_CORRI']))
                    monevalu  = int(vnulo(index['MON_EVALU']))
                    aboevalu  = int(vnulo(index['ABO_EVALU']))
                    moncapi   = int(vnulo(index['MON_CAPI']))
                    abocapi   = int(vnulo(index['ABO_CAPI']))
                    pgapli   =  int(vnulo(index['PGPAPLICAR']))
                    foliox   =  int(vnulo(index['FOLIO']))
                    fecven =    (index['FECHA_VEN']).strftime("%Y-%m-%d")


            
                if salante !="" and mongascob !="" and monmopro !="" :

                    ABO_GASCOB = define_abono(mongascob,abogascob,montcan)
                    MONTO_CANX = saca_saldo(mongascob,abogascob,montcan)
                    ABO_GASCOBX =  abogascob + vnulo(ABO_GASCOB) 
                 
                    ABO_MOPRO  = define_abono(monmopro,abomopro,MONTO_CANX)
                    MONTO_CANX = saca_saldo(monmopro,abomopro,MONTO_CANX)
                    ABO_MOPROX  =  abomopro +  vnulo(ABO_MOPRO)

                    ABO_GCEGENE  = define_abono(mongene,abogene,MONTO_CANX)
                    MONTO_CANX   = saca_saldo(mongene,abogene,MONTO_CANX)
                    ABO_GCGENEX   =  abogene +  vnulo(ABO_GCEGENE)

                    ABO_MOPERI   = define_abono(monmoperi,abomoperi,MONTO_CANX)
                    MONTO_CANX   = saca_saldo(monmoperi,abomoperi,MONTO_CANX)
                    ABO_MOPERIX   =  abomoperi +  vnulo(ABO_MOPERI)

                    ABO_MOANTE   = define_abono(salante,abomoante,MONTO_CANX)
                    MONTO_CANX   = saca_saldo(salante,abomoante,MONTO_CANX)
                    ABO_MOANTEX   =  abomoante +  vnulo(ABO_MOANTE)

                    ABO_IMPU     = define_abono(monimpu,aboimpu,MONTO_CANX)
                    MONTO_CANX   = saca_saldo(monimpu,aboimpu,MONTO_CANX)
                    ABO_IMPUX     =  aboimpu +  vnulo(ABO_IMPU)

                    ABO_ENVIO     = define_abono(monenvi,aboenvi,MONTO_CANX)
                    MONTO_CANX    = saca_saldo(monenvi,aboenvi,MONTO_CANX)
                    ABO_ENVIOX     =  aboenvi +  vnulo(ABO_ENVIO)

                    ABO_SEGU     = define_abono(monsegu,abosegu,MONTO_CANX)
                    MONTO_CANX   = saca_saldo(monsegu,abosegu,MONTO_CANX)
                    ABO_SEGUX     =  abosegu +  vnulo(ABO_SEGU)

                    ABO_COMI     =  define_abono(moncomi,abocomi,MONTO_CANX)
                    MONTO_CANX   =  saca_saldo(moncomi,abocomi,MONTO_CANX)
                    ABO_COMIX     =  abocomi +  vnulo(ABO_COMI)

                    ABO_DICO     =  define_abono(mondico,abodico,MONTO_CANX)
                    MONTO_CANX   =  saca_saldo(mondico,abocomi,MONTO_CANX)
                    ABO_DICOX     =  abocomi +  vnulo(ABO_DICO)

                    ABO_CORRI     =  define_abono(moncorri,abocorri,MONTO_CANX)
                    MONTO_CANX    =  saca_saldo(moncorri,abocorri,MONTO_CANX)
                    ABO_CORRIX     =  abocorri +  vnulo(ABO_CORRI)

                    ABO_EVALU     =  define_abono(monevalu,aboevalu,MONTO_CANX)
                    MONTO_CANX    =   saca_saldo(monevalu,aboevalu,MONTO_CANX)
                    ABO_EVALUX     =  aboevalu +  vnulo(ABO_EVALU)

                    ABO_CAPI     =  define_abono(moncapi,abocapi,MONTO_CANX)
                    MONTO_CANX   =  saca_saldo(moncapi,abocapi,MONTO_CANX)
                    ABO_CAPIX     =  abocapi +  vnulo(ABO_CAPI)
               
                    if MONTO_CANX > 0:
                        PGAPLICARX = pgapli + vnulo(MONTO_CANX)
                        ABPG = vnulo(MONTO_CANX)
                    else:
                        PGAPLICARX = pgapli
                        ABPG = 0
                     
                    txt_sql = " UPDATE eecc  SET  ABO_GASCOB = (%s) , ABO_MOPRO = (%s) , ABO_GCGENE = (%s) , ABO_MOPERI = (%s) , " \
                     " ABO_MOANTE = (%s) , ABO_IMPU = (%s) , ABO_ENVI = (%s), ABO_SEGU = (%s) , ABO_COMI = (%s) , ABO_DICO = (%s) , ABO_CORRI = (%s),"\
                     " ABO_EVALU = (%s) , ABO_CAPI = (%s) , PGPAPLICAR = (%s)   WHERE rut = (%s) "
                    cursor.execute(txt_sql, (ABO_GASCOBX, ABO_MOPROX,ABO_GCGENEX,ABO_MOPERIX,ABO_MOANTEX,ABO_IMPUX,ABO_ENVIOX,ABO_SEGUX,ABO_COMIX,ABO_DICOX,ABO_CORRIX,ABO_EVALUX,ABO_CAPIX,PGAPLICARX,rutx))
                    connection.commit()
                    cursor.close()

                    #d = datetime.today()
                    #fechax = d.strftime("%Y-%m-%d")
                    fechax =  fechaxf
                    insertar_abonos( ntran,rutx, montcan,fechax,foliox,fecven,ABO_GASCOB,ABO_MOPRO,ABO_GCEGENE,ABO_MOPERI,ABO_MOANTE,ABO_IMPU,ABO_ENVIO,ABO_SEGU,ABO_COMI,ABO_DICO,ABO_CORRI,ABO_EVALU,ABO_CAPI,ABPG)

        except pymysql.err.ProgrammingError as except_detail:
               print("pymysql.err.ProgrammingError: «{}»".format(except_detail))
        finally:
               cursor.close()
              



def verificar_pago(rut, fecha, monto, voucher, ntrans):

    with connection.cursor() as cursor:
        # Prepare SQL query to select a record into the database.
        try:
            txt_sql = "SELECT * FROM abonos"
            txt_sql += " where rut = '" + rut + "' and fec_tran >= '" + fecha + "' and "
            txt_sql += " n_tran = " + str(ntrans) + " and mont_tran = " + str(monto) + " and TIP_TRAN = 3"
            rows_count = cursor.execute(txt_sql)
            n_id = obtener_nid(rut)
            # Fetch all the rows in a list of lists.
            if rows_count > 0 :

                txt_sql = "UPDATE pagos_sencillito  SET estado = 'ABONADO' ,transac = (%s) WHERE rut = (%s)" 
                txt_sql += " and voucher = (%s) and id = (%s) "
                cursor.execute(txt_sql, (ntrans, rut, voucher,n_id))
                connection.commit()

            else:
                txt_sql = " UPDATE pagos_sencillito  SET  estado = 'ERROR NO PAGO' WHERE rut = (%s) and voucher = (%s) and id = (%s)"
                cursor.execute(txt_sql, (rut, voucher,n_id))
                connection.commit()
        


            print("DATOS VERIFICADOS")
           # cursor.close()
        except pymysql.err.ProgrammingError as except_detail:
               print("pymysql.err.ProgrammingError: «{}»".format(except_detail))
        finally:
               cursor.close()



              

def actualiza_mora(rut, monto,ntran):

    with connection.cursor() as cursor:
        # Prepare SQL query to select a record into the database.
        try:
            d = datetime.today()
            mifecha  = d.strftime("%Y-%m-%d")
            txt_sql = "SELECT id, Rut, Saldopend, Abonos_Pos, Estado, Saldo,dias_atras FROM Moras"
            txt_sql += " where rut = '" + rut + "' AND Estado = 'P' ORDER BY F_Venc ASC "
            rows_count = cursor.execute(txt_sql)
            # Fetch all the rows in a list of lists.
            if rows_count > 0 :
                results = cursor.fetchall()
                abonomoras = monto
           
                for index in results:
                    saldop  = int(vnulo(index['Saldopend']))
                    abonop  = int(vnulo(index['Abonos_Pos']))
                    estadox = str(index['Estado'])
                    sal     = int(vnulo(index['Saldo']))
                    diasax  = int(vnulo(index['dias_atras']))
                    idx  = int(vnulo(index['id']))

                    if abonomoras >= saldop:
                        sql = "INSERT INTO  PagoMora(fecha,rut,monto,dias, boleta)" \
                        " VALUES ((%s),(%s),(%s),(%s),(%s))"
                        args = (mifecha,rut,abonomoras,diasax,ntran )
                        cursor.execute(sql, (args))
                        connection.commit()
                        abonomoras = monto - saldop
                        txt_sql = " UPDATE moras  SET  Abonos_Pos = (%s) ,SALDOPEND = 0, estado = 'C' WHERE rut = (%s) and id = (%s)"
                        cursor.execute(txt_sql, (sal,rut, idx))
                        connection.commit()
                    else:
                        if abonomoras > 0:
                            sql = "INSERT INTO  PagoMora(fecha,rut,monto,dias, boleta)" \
                            " VALUES ((%s),(%s),(%s),(%s),(%s))"
                            args = (mifecha,rut,abonomoras,diasax,ntran )
                            cursor.execute(sql, (args))
                            connection.commit()
                    

                        abonop = abonop + abonomoras
                        saldop = saldop - abonomoras
                        txt_sql = " UPDATE moras  SET  Abonos_Pos = (%s) ,SALDOPEND = (%s)  WHERE rut = (%s) and id = (%s)"
                        cursor.execute(txt_sql, (abonop,saldop,rut, idx))
                        connection.commit()
            
           # cursor.close()
        except pymysql.err.ProgrammingError as except_detail:
               print("pymysql.err.ProgrammingError: «{}»".format(except_detail))
        finally:
               cursor.close()
              

def actualiza_tramo(rutx,montox):

    with connection.cursor() as cursor:
        # Prepare SQL query to select a record into the database.
        try:
            sql = "SELECT deuda,fecha_inicio,fecha_final,abonos,dias,tramo FROM asignaciones_guardadas"
            sql += " where rut = '" + rutx + "' "

            # Execute the SQL command
           # cursor.execute(sql)
            rows_count = 0
            rows_count = cursor.execute(sql)
            # Fetch all the rows in a list of lists.

            if rows_count > 0:
                results = cursor.fetchall()
                for index in results:
                    deudax = int(vnulo(index['deuda']))
                    fini   = (index['fecha_inicio']).strftime("%Y-%m-%d")
                    ffinal = (index['fecha_final']).strftime("%Y-%m-%d")
                    abonox = int(vnulo(index['abonos']))
                    tramox = str(vnulostr(index['tramo']))
                    diasx =  int(vnulo(index['dias']))

        
                if fini != "" and ffinal != "" :
                    if montox >= deudax: 
                        estado_asignacion = "PAGADO TOTAL"
                        tramox = 'TI'
                        diasx = 0
                    else:
                        estado_asignacion = "PAGADO PARCIAL"
                

                abonado = abonox + vnulo(montox)
                txt_sql = " UPDATE asignaciones_guardadas  SET  estado = (%s) ,abonos = (%s),tramo = (%s), dias = (%s) where rut = (%s)"
                cursor.execute(txt_sql, (estado_asignacion,abonado,tramox,diasx,rutx))
                connection.commit()
               
        except pymysql.err.ProgrammingError as except_detail:
               print("pymysql.err.ProgrammingError: «{}»".format(except_detail))
        finally:
               cursor.close()
              



def asignaciones_vencida(rutx,montox):

    with connection.cursor() as cursor:
        # Prepare SQL query to select a record into the database.
        try:
            sql = "SELECT deuda,abonos FROM asignaciones_guardadas"
            sql += " where rut = '" + rutx + "' "

            # Execute the SQL command
            rows_count = cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            if rows_count > 0:
                results = cursor.fetchall()
                for index in results:
                    deudax = int(vnulo(index['deuda']))
                    abonox = int(vnulo(index['abonos']))
            
                if montox >= deudax: 
                    estado_asignacion = "PAGADO TOTAL"
                else:
                    estado_asignacion = "PAGADO PARCIAL"
                

                abonado = abonox + vnulo(montox)
                txt_sql = " UPDATE asignaciones_guardadas  SET  estado = (%s) ,abonos = (%s) where rut = (%s)"
                cursor.execute(txt_sql, (estado_asignacion,abonado,rutx))
                connection.commit()
            else:
                print("SIN RESULTADOS")
        
        except pymysql.err.ProgrammingError as except_detail:
               print("pymysql.err.ProgrammingError: «{}»".format(except_detail))
        finally:
               cursor.close()
              


def ObtieneFolioAPagar(rutx):

    with connection.cursor() as cursor:
        # Prepare SQL query to select a record into the database.
        try:
            sql = " SELECT folio  FROM Encabezado_repactacion WHERE rut = '" + rutx + "' AND (estado='GENERADA' or estado='VIGENTE' or estado='ATRASADA' )"
            sql += " order by fechaRepactacion desc limit 1"
            # Execute the SQL command
            rows_count = cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            if rows_count > 0:
                results = cursor.fetchall()
                for index in results:
                    foliox = int(vnulo(index['folio']))
                return foliox
            else:

                 return 0
        
        except pymysql.err.ProgrammingError as except_detail:
               print("pymysql.err.ProgrammingError: «{}»".format(except_detail))
        finally:
               cursor.close()
              
            

def cargar_repactacion_pendiente(rutx):

    with connection.cursor() as cursor:
        # Prepare SQL query to select a record into the database.
        try:
            sql = " SELECT rut  FROM Encabezado_repactacion WHERE rut = '" + rutx + "' AND (estado='GENERADA' or estado='VIGENTE' or estado='ATRASADA')"
    
            # Execute the SQL command
            rows_count = cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            if rows_count > 0:
                actualiza_repactacion = True
                    
            else:
                actualiza_repactacion = False
            
            return actualiza_repactacion

        except pymysql.err.ProgrammingError as except_detail:
               print("pymysql.err.ProgrammingError: «{}»".format(except_detail))
        finally:
               cursor.close()
              

def actualiza_tblaut(rutx,montox):

    with connection.cursor() as cursor:
        # Prepare SQL query to select a record into the database.
        try:
            sql = "SELECT Cup_cuotas, Dis_Comcuo, Deuda_moro, Fl_Moro FROM tblaut"
            sql += " where rut = '" + rutx + "' "

             # Execute the SQL command
            rows_count = cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            if rows_count > 0:
                results = cursor.fetchall()
                for index in results:
                    cupcuotas = int(vnulo(index['Cup_cuotas']))
                    dispo     = int(vnulo(index['Dis_Comcuo']))
                    dmoro     = int(vnulo(index['Deuda_moro']))
                    flmoro    = str(vnulostr(index['Fl_Moro']))

                if cupcuotas != "" and dispo != "" :
                    salmoro = dmoro - montox
                    disponible = dispo + montox
                    if salmoro <= 0:
                        dmoro = 0
                        flmoro = 'N'

                txt_sql = " UPDATE tblaut  SET  Dis_Comcuo = (%s) ,Deuda_Moro = (%s),Fl_Moro = (%s) where rut = (%s)"
                cursor.execute(txt_sql, (disponible,dmoro,flmoro,rutx))
                connection.commit()
        
        except pymysql.err.ProgrammingError as except_detail:
               print("pymysql.err.ProgrammingError: «{}»".format(except_detail))
        finally:
               cursor.close()
              

def actualiza_ultpago(rutx):

    with connection.cursor() as cursor:
        # Prepare SQL query to select a record into the database.
        try:
            d = datetime.today()
            mifecha  = d.strftime("%Y-%m-%d")

            txt_sql = " UPDATE Cliente  SET  ult_fecha_pago = (%s)  where rut = (%s)"
            cursor.execute(txt_sql, (mifecha,rutx))
            connection.commit()
        
        except pymysql.err.ProgrammingError as except_detail:
               print("pymysql.err.ProgrammingError: «{}»".format(except_detail))
        finally:
               cursor.close()


def trae_excusa(rutx,nabono,cartera):
    with connection.cursor() as cursor:
        # Prepare SQL query to select a record into the database.
        try:


            aplica_pago = "NO"
            if cartera == True:
                 d = datetime.today() - timedelta(days=45)
            else:
                 d = datetime.today() - timedelta(days=10)


            fechax = d.strftime("%Y-%m-%d")


            sql =   " SELECT fecha_ing, usua_ing from explica where rut= '" + str(rutx) + "'  "
            sql +=  " and  fecha_ing between '" + str(fechax) + "' and DATE_ADD(curdate(),interval 2 DAY) "
            sql +=  " AND (usua_ing='ERNESTO DIAZ VALENZUELA' or usua_ing='LUIS CAROCA' or usua_ing='LUIS CAROCA ' "
            sql +=  " or usua_ing='lcaroca' or usua_ing='hsilva' or usua_ing='Hector Silva' or usua_ing='mbravo'or usua_ing='Miguel Bravo')"
            sql +=  "  order by fecha_ing desc limit 1; "
            rows_count = cursor.execute(sql)
          
            # Fetch all the rows in a list of lists.
            if rows_count > 0 :
                results = cursor.fetchall()
                for index in results:
                    USU_EXCUSA = index['usua_ing']
                    FEC_EXCUSA = index['fecha_ing']
                    aplica_pago = "SI"

                FEC_EXCUSA =  FEC_EXCUSA.strftime("%Y-%m-%d")
                 
            else:
                USU_EXCUSA = None
                FEC_EXCUSA = None
                aplica_pago = "NO"

            
            g = datetime.today() - timedelta(days=7)
            fecha_ante2 = g.strftime("%Y-%m-%d")


            sql =  " SELECT fecha, cobrador"
            sql +=  " from r_llamados_cobro"
            sql +=  " where rut_titular='" + str(rutx) + "'"
            sql +=  " and  fecha  between '" + str(fecha_ante2) + "'  and CURDATE()  "
            sql +=  " and (accion='Compromiso de abono.' or accion='RECADO')"
            sql +=  " order by fecha desc limit 1"
            rows_count = cursor.execute(sql)
          
            # Fetch all the rows in a list of lists.
            if rows_count > 0 :
                results = cursor.fetchall()
                for index in results:
                    USU_EXCUSA_FONO = index['cobrador']
                    FEC_EXCUSA_FONO = index['fecha']
                
                FEC_EXCUSA_FONO =  FEC_EXCUSA_FONO.strftime("%Y-%m-%d")
                 
            else:
                USU_EXCUSA_FONO = None
                FEC_EXCUSA_FONO = None
      
           
         
            sql = " UPDATE abonos  SET  TERRENO = (%s), FECHA_TERRENO = (%s), PAGO = (%s), FONO =(%s) ,FECHA_FONO =(%s)  "
            sql += " WHERE rut = (%s) and N_TRAN = (%s) AND TIP_TRAN = 3 "
            cursor.execute(sql, (USU_EXCUSA,FEC_EXCUSA,aplica_pago,USU_EXCUSA_FONO,FEC_EXCUSA_FONO,rutx,nabono))
            connection.commit()


        except pymysql.err.ProgrammingError as except_detail:
               print("pymysql.err.ProgrammingError: «{}»".format(except_detail))
        finally:
               cursor.close()


def trae_fecha_evaluacion(rutx,nabono):
    with connection.cursor() as cursor:
        # Prepare SQL query to select a record into the database.
        try:
            FECHA_EVALUACION = None
            TRAMO = None
            d = datetime.today() - timedelta(days=35)
            fechainx = d.strftime("%Y-%m-%d")

            sql =   " SELECT fecha_inicio, tramo  FROM asignacion_mensual  where rut= '" + str(rutx) + "'  "
            sql +=  " and  fecha_inicio between '" + str(fechainx) + "' and CURDATE() "
            sql +=  "  order by fecha_inicio desc limit 1; "
            rows_count = cursor.execute(sql)
          
            # Fetch all the rows in a list of lists.
            if rows_count > 0 :
                results = cursor.fetchall()
                for index in results:
                    FECHA_EVALUACION = index['fecha_inicio']
                    TRAMOX = index['tramo']
            
                FECHA_EVALUACION =  FECHA_EVALUACION.strftime("%Y-%m-%d")
               
            else:
                FECHA_EVALUACION = None
                TRAMOX = None
           
           
           


            sql = " UPDATE abonos  SET  FECHA_EVALUACION = (%s), TRAMO = (%s)  "
            sql += " WHERE rut = (%s) and N_TRAN = (%s) AND TIP_TRAN = 3 "
            cursor.execute(sql, (FECHA_EVALUACION,TRAMOX,rutx,nabono))
            connection.commit()


        except pymysql.err.ProgrammingError as except_detail:
               print("pymysql.err.ProgrammingError: «{}»".format(except_detail))
        finally:
               cursor.close()
              

def vnulo(valor):
    try:
        if valor is None:
            return 0
        else:
            return valor

    except:
        print("Error valor :")

def vnulostr(valor):
    try:
        if valor is None:
            return ""
        else:
            return valor

    except:
        print("Error valor :")

def define_abono(monto,abono,saldo):
    try:
        mmonto = vnulo(monto)
        mabono = vnulo(abono)
        real_abono = 0
        if saldo > 0:
            real_abono = mmonto - mabono
            if real_abono > saldo:
                real_abono = saldo
        return real_abono

    except:
        print("Error valor :")

def saca_saldo(monto,abono,saldo):
    try:
        mmonto = vnulo(monto)
        mabono = vnulo(abono)
        if saldo > 0:
            real_abono = mmonto - mabono
            if real_abono <= saldo:
                saldox = saldo - real_abono
            else:
                saldox = 0
        else:
            saldox = 0
        return saldox

    except:
        print("Error valor :")


def tipo_cartera(rutx):

    with connection.cursor() as cursor:
        # Prepare SQL query to select a record into the database.
        try:
            sql = "SELECT EN_VENCIDA  FROM cliente "
            sql += " where rut = '" + rutx + "'  and EN_VENCIDA = 'S'"
    
            # Execute the SQL command
            rows_count = cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            if rows_count > 0:
                cartera = True
                    
            else:
                cartera = False
            
            return cartera

        except pymysql.err.ProgrammingError as except_detail:
               print("pymysql.err.ProgrammingError: «{}»".format(except_detail))
        finally:
               cursor.close()



