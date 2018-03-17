import time
import mraa
import socket
import pyupm_grove as grove

temp = grove.GroveTemp(0)

light = grove.GroveLight(0)

button = mraa.Gpio(6)
button.dir(mraa.DIR_IN)

sound=mraa.Aio(1)

s=socket.socket()
s.connect(("172.20.10.10",9090))

while True:
    if button.read():
        temp_now = temp.value()
        ambientLight = light.value()
        t = str(temp_now)
        a = str(sound.read())
        l = str(ambientLight)
        all ="temp: "+ t+ " Light Level: "+l+" sound " +a+" "
        s.send(all)
        time.sleep(1)
    data=s.recv(1024)
    print(data)
s.close()