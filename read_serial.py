import serial
ser = serial.Serial('COM1', 9600, timeout = 1) 
print ("Starting up")
connected = False
while True:
    try:
        print ("Attempt to Read")
        readOut = ser.readline()
        time.sleep(1)
        print ("Reading: ", readOut) 
        break
    except:
        pass
    print ("Restart")
    ser.flush() #flush the buffer