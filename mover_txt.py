
import paramiko
import os, shutil,glob,time
import correo_aviso_vacio
hostname = ""
username = ""
password = ""


def validar_archivo_subir():
    try:

        directorya = "D:\\sencillito\\ARCHIVO SUBIR"
        directoryb = "D:\\sencillito\\HISTORICO CYD"
        files = [file for file in os.listdir(directorya) if os.path.isfile(os.path.join(directorya, file))]
        for file in files:
            if not os.path.exists(os.path.join(directoryb, file)):
                shutil.copy(os.path.join(directorya, file), directoryb)
            else:
                os.remove(os.path.join(directorya, file))

    except Exception as e:
            print(e.message)
            exit(1)


def bajar_archivo_rendicion():
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, username=username, password=password)
        print("Conectado a %s" % hostname)
        rutarecibido = "D:\\sencillito\\HISTORICO SENCILLITO"
        list_of_files = glob.glob(rutarecibido + "\\*")
        latest_file = max(list_of_files, key=os.path.getctime)
        namefile = latest_file[-26:]
        sftp = ssh.open_sftp()
        stdin, stdout, stderr = ssh.exec_command('cd Salida; ls -1t')
        archivos = []
        for line in stdout.read().splitlines():
            last_file = str(line)
            lasttxt = str(last_file).replace("b", '')
            last_file = str(lasttxt).replace("'", '')
            if last_file == namefile:
                break
            else:
                archivos.append(str(last_file))

        for nomfile in reversed(archivos):
            remotepathserver = '/home/CyD/Salida/'
            local = "D:\\sencillito\\ARCHIVO BAJAR"
            sftp.get(remotepathserver + '/' + nomfile, os.path.join(local, nomfile))
            print("ARCHIVO  DESCARGADO:  " + nomfile)
            filesize = os.path.getsize(os.path.join(local, nomfile))
            if filesize == 0:
                print("El archivo esta vacio envio aviso: " + str(filesize))
                correo_aviso_vacio.enviar_email(nomfile)
            else:
                print("El archivo tiene datos ok!: " + str(filesize))
      


        sftp.close()
        ssh.close()
    except paramiko.AuthenticationException:
        print("fallo al conectar credenciales username/password" % hostname)
        exit(1)
    except Exception as e:
        print(e.message)
        exit(2)


def validar_archivo_bajado():
    try:

        directorya = "D:\\sencillito\\ARCHIVO BAJAR"
        directoryb = "D:\\sencillito\\HISTORICO SENCILLITO"
        files = [file for file in os.listdir(directorya) if os.path.isfile(os.path.join(directorya, file))]
        for file in files:
            if not os.path.exists(os.path.join(directoryb, file)):
                shutil.copy(os.path.join(directorya, file), directoryb)
                time.sleep(2)
            else:
                os.remove(os.path.join(directorya, file))
                time.sleep(2)
    except Exception as e:
        print(e)
        exit(1)


