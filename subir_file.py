import paramiko
import os
import glob
import mover_txt

hostname = ""
username = ""
password = ""


def subir_archivo():
    try:
        mover_txt.validar_archivo_subir()
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, username=username, password=password)
        print("Conectado a %s" % hostname)
        sftp = ssh.open_sftp()
        rutaupload = "D:\\sencillito\\ARCHIVO SUBIR"
        list_of_files = glob.glob(rutaupload + "\\*")
        latest_file = max(list_of_files, key=os.path.getctime)
        namefile = latest_file[-21:]

        localpath = os.path.join(rutaupload, namefile)
        remotepath = '/home/CyD/Entrada/' + namefile + ''
        sftp.put(localpath, remotepath)
        print('Archivo ' + namefile + ' Subido Correctamente')
        stdin, stdout, stderr = ssh.exec_command('cd Salida; ls -1t | head -1')
        sftp.close()
        ssh.close()
    except paramiko.AuthenticationException:
        print("fallo al conectar credenciales username/password" %hostname)
        exit(1)
    except Exception as e:
        print(e)
        exit(2)
