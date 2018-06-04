import socket
from os.path import commonprefix
def index():
    words = {
        'how are you':'yes',
        'how old are you':'20',
        
    }
    HOST = ''
    PORT = 50007
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    s.listen(1)
    print('you are listening:',PORT)
    conn,addr = s.accept()
    print(' Connected by',addr)
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print('Received message:',data)
        m = 0
        key = ''
        for k in words.keys():
            data = ' '.join(data.split())
            if len(commonprefix([k,data])) > len(k)*0.7:
                key = k
                break
            length = len(set(data.split())&set(k.split()))
            if length > m:
                m = length
                key = k
         conn.sendall(word.get(key,'sorry.').encode())
    conn.close()
    s.close()

