import socket
import BeepBoop as bp
import RPi.GPIO as GPIO

host = ''
port = 5560
buzz = 27 # pin for buzzer


def setupsever():
    '''Creates the host socket
    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket Created')
    try:
        s.bind((host,port))
    except socket.error as msg:
        print(msg)
    print('Binding Complete')
    return s

def setupConnection():
    '''Creates connection for one computer
    '''
    s.listen(1) # Allows one Connection
    conn, address = s.accept() # Waits for someone to connect
    print('Connected to: {}'.format(address))
    return conn

def dataTransfer(conn):
    '''Recevies commands and sends out responses
    '''
    while True:
        data = conn.recv(1024)
        data = data.decode('utf-8')
        dataMsg = data.split(' ',1)
        command = dataMsg[0].lower()
        if command == 'msg': # msg command returns a morse code message to host
            reply = 'Sending: {}'.format(dataMsg[1])
            try:
                bp.W_morse(buzz,dataMsg[1])
            except:
                reply = 'There was an error beeping your message...\nAvoid using special characters.'
        elif command == 'exit': # tells host that the client left
            print('Client disconnected')
            break
        elif command == 'kill': # closes host server and client exits
            print('Shutting Down')
            GPIO.cleanup()
            s.close()
            break
        else:
            reply = 'Unknown Command'

        print('Command "{}" received'.format(data))
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
        GPIO.cleanup()
        s.close()
        break
    except:
        GPIO.cleanup()
        s.close()
        break
