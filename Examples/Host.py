import socket
import BeepBoop as bp
import RPi.GPIO as GPIO

host = ''
port = 5560
buzz = 27

store = 'Hello World'

def setupsever():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket Created')
    try:
        s.bind((host,port))
    except socket.error as msg:
        print(msg)
    print('Binding Complete')
    return s

def setupConnection():
    s.listen(1) # Allows one Connection
    conn, address = s.accept()
    print('Connected to: {}'.format(address))
    return conn

def dataTransfer(conn):
    while True:
        data = conn.recv(1024)
        data = data.decode('utf-8')
        dataMsg = data.split(' ',1)
        command = dataMsg[0].lower()
        if command == 'msg':
            reply = 'Sending: {}'.format(dataMsg[1])
            bp.W_morse(buzz,dataMsg[1])
        elif command == 'exit':
            print('Client disconnected')
            break
        elif command == 'kill':
            print('Shutting Down')
            GPIO.cleanup()
            s.close()
            break
        else:
            reply = 'Unknown Command'

        print('Command: {} received'data)
        conn.sendall(str.encode(reply))
        print('Data has been sent!')
    conn.close()


s = setupsever()

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzz,GPIO.OUT, initial = 0)

while True:
    try:
        conn = setupConnection()
        dataTransfer(conn)

    except KeyboardInterrupt:
        s.close()
        GPIO.cleanup()
        break
    except:
        GPIO.cleanup()
        s.close()
        break

