import socket, time
import conexion


def enviar_trama(tarpan, monto, fecha , voucher , rutcom , fecformt):
    tcp_ip = ''
    tcp_port = 
    trama = ''
    trama_final= trama.format(tarpan, monto, fecha)
    print(trama_final)
    trama_byte = trama_final.encode()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((tcp_ip, tcp_port))
    s.send(trama_byte)
    resp = str(s.recv(1024).decode('utf-8', errors='replace'))
    n_trancyd = resp[44:-33]
    print(n_trancyd[44:-33])
    time.sleep(2)
    conexion.verificar_pago(rutcom, str(fecformt), int(monto), int(voucher),int(n_trancyd))
    s.close()




