import sys
import socket

if __name__ == "__main__":

    timeout = int(sys.argv[1])
    print(f"timeout set to{timeout}")
    s = socket.socket()
    s.settimeout(timeout)

    host = "localhost"
    port = 8000
    s.connect((host,port))

    s.send('GET / HTTP/1.0\r\n\r\n'.encode()) 
    try:
        data = ''
        data = s.recv(1024).decode()
        print (data)
    except Exception as e:
        print(f"recv exception: {e}")
    finally:
        try:
            s.shutdown(socket.SHUT_RDWR)
            s.close()
        except Exception as e:
            print(f"shutdown/close exception: {e}")
