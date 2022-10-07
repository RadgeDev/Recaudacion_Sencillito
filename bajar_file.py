import paramiko
import os
import glob,time


hostname = ""
username = ""
password = ""


def bajar_archivo_rendicion():
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, username=username, password=password)
        print("Conectado a %s" % hostname)
        rutarecibido = "D:\\sencillito\\HISTORICO SENCILLITO"
        list_of_files = glob.glob(rutarecibido + "\\*")
        latest_file = max(list_of_files, key=os.path.getctime)
        namefile = str(latest_file[-26:])
        sftp = ssh.open_sftp()
        stdin, stdout, stderr = ssh.exec_command('cd Salida; ls -1t')
        archivos = []
        for line in stdout.read().splitlines():
            last_file = str(line)
            lasttxt = str(last_file).replace("b", '')
            last_file = str(lasttxt).replace("'", '')
            if last_file == namefile:
                print('NO HAY NUEVAS RECAUDACIONES.')
                break
            else:
                archivos.append(str(last_file))

        for nomfile in reversed(archivos):
            remotepathserver = ''
            local = "D:\\sencillito\\ARCHIVO BAJAR"
            sftp.get(remotepathserver + '/' + nomfile, os.path.join(local, nomfile))
            print("ARCHIVO  DESCARGADO:  " + nomfile)
            time.sleep(2)
        sftp.close()
        ssh.close()
    except paramiko.AuthenticationException:
        print("fallo al conectar credenciales username/password" % hostname)
        exit(1)
    except Exception as e:
        print(e.message)
        exit(2)



