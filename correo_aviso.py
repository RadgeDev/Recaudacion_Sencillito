import smtplib
import email.message
from datetime import date
import datetime
import pymysql.cursors
import time


connection = pymysql.connect(host='',
                             user='',
                             password="",
                             db='',
                             cursorclass=pymysql.cursors.DictCursor)


def verificar_pago():

    with connection.cursor() as cursor:
        # Prepare SQL query to select a record into the database.
        try:
            txt_sql = "SELECT rut,monto,voucher,fecha,hora FROM pagos_sencillito WHERE fecha > '2020-05-01'  AND (estado <>  'ABONADO' or estado IS NULL);"
            # Execute the SQL command                            
            cursor.execute(txt_sql)
            row_count = cursor.rowcount
            if row_count > 0:
               results = cursor.fetchall()
               for index in results:
                    rut = str(index['rut'])
                    monto = int(index['monto'])
                    voucher = int(index['voucher'])
                    fecha = str(index['fecha'])
                    hora = str(index['hora'])
                    enviar_email(rut, monto, voucher, fecha, hora)
                    time.sleep(5)
            cursor.close()
        except:
            print("Error: No hay datos verificar")
            cursor.close()
            connection.close()


def enviar_email(rut,monto,voucher,fecha,hora):

    server = smtplib.SMTP('mail.tarjetacyd.cl:587')
    email_content = """
      <html>

      <head>
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8">

       <title>Tutsplus Email Newsletter</title>
       <style type="text/css">
        a {color: #d80a3e;}
        body, #header h1, #header h2, p {margin: 0; padding: 0;}
       #main {border: 1px solid #cfcece;}
       img {display: block;}
       #top-message p, #bottom p {color: #3f4042; font-size: 12px; font-family: Arial, Helvetica, sans-serif; }
      #header h1 {color: #ffffff !important; font-family: "Lucida Grande", sans-serif; font-size: 24px; margin-bottom: 0!important; padding-bottom: 0; }
      #header h3 {color: #ffffff !important; font-family: "Lucida Grande", sans-serif; font-size: 16px; margin-bottom: 0!important; padding-bottom: 0; }
      #header p {color: #ffffff !important; font-family: "Lucida Grande", "Lucida Sans", "Lucida Sans Unicode", sans-serif; font-size: 12px;  }
      h5 {margin: 0 0 0.8em 0;}
        h5 {font-size: 18px; color: #444444 !important; font-family: Arial, Helvetica, sans-serif; }
      p {font-size: 12px; color: #444444 !important; font-family: "Lucida Grande", "Lucida Sans", "Lucida Sans Unicode", sans-serif; line-height: 1.5;}
       </style>
    </head>

    <body>


    <table width="100%" cellpadding="0" cellspacing="0" bgcolor="e4e4e4"><tr><td>
    <table id="top-message" cellpadding="20" cellspacing="0" width="600" align="center">
        <tr>
          <td align="center">
          </td>
        </tr>
      </table>

    <table id="main" width="600" align="center" cellpadding="0" cellspacing="15" bgcolor="ffffff">
        <tr>
          <td>
            <table id="header" cellpadding="10" cellspacing="0" align="center" bgcolor="8fb3e9">
              <tr>
                <td width="570" align="center"  bgcolor="#d80a3e"><h1>AVISO TRANSACCION SIN INGRESAR </h1></td>
              </tr>
               <tr>
                <td width="570" align="left"  bgcolor="#d80a3e"><h3>NUMERO VOUCHER : """ + str(voucher) + """ </h3></td>
              </tr>
                  <tr>
                <td width="570" align="left"  bgcolor="#d80a3e"><h3>RUT CLIENTE : """ + str(rut) + """ </h3></td>
              </tr>

              <tr>
                <td width="570" align="left"  bgcolor="#d80a3e"><h3>MONTO : $ """ + str(monto) + """ </h3></td>
              </tr>
              <tr>
                <td width="570" align="left"  bgcolor="#d80a3e"><h3>FECHA :""" + str(fecha) + """  </h3></td>
              </tr>
              <tr>
                <td width="570" align="left"  bgcolor="#d80a3e"><h3>HORA :""" + str(hora) + """  </h3></td>
              </tr>
              
              <tr>
                <td width="570" align="right" bgcolor="#d80a3e"><p>""" + str(date.today()) + """</p></td>
              </tr>
            </table>
          </td>
        </tr>

        <tr>


      </table>
      <table id="bottom" cellpadding="20" cellspacing="0" width="600" align="center">
        <tr>
          <td align="center">
            <p>CYD 2019</p>

          </td>
        </tr>
      </table><!-- top message -->
    </td></tr></table><!-- wrapper -->

    </body>
    </html>


    """
    x = datetime.datetime.now()
    msg = email.message.Message()
    msg['Subject'] = 'Alerta CYD Servidor Sencillito  ' + str(x) + ''
    msg['From'] = ''
    recipients = ['eavila@example.cl']

    password = ""
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_content)
    s = smtplib.SMTP('mail:587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], recipients, msg.as_string(), msg.encode("utf8"))


verificar_pago()
