import serial
import threading

# Serial port configuration
port = 'COM5'  # Replace with the appropriate port name
baud_rate = 9600
mutex = threading.Lock()
# Create a serial connection object
ser = serial.Serial(port, baud_rate, timeout=1)


# Thread function to read data from the serial port
def read_serial():
   global data 
   data = ''
   while True:
      data += ser.read(ser.inWaiting()).decode()
      if '\n' in data:
         buffer = data.split('\n')[-2:]
      
      
def main():
   read_serial() 
   ser.close()


if __name__ == "__main__":
    main()
# Main program loop

# Clean up the serial connection

