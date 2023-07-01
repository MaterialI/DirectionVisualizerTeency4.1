import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from serial import Serial
import serial
import re
import numpy as np
import math
import time
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

port = serial.Serial('COM5', 9600, timeout= 1)

def setUp():
    # Set the limits and labels of the plot
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.set_zlim([0, 1])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    

def decodeReadout(readout):
    # res = readouts.decode('utf-8') #gyro readout encoding
    pattern = r'-?\d+.\d+'
    numbers = re.findall(pattern, readout)
    
    return numbers


def magnitude(vector):
    return math.sqrt(sum(pow(element, 2) for element in vector))

def anim(i):
        
        global readouts 
        readouts = ''
        readouts += port.read(port.inWaiting()).decode()
        if '\n' in readouts:
            buffer = readouts.split('\n')[-2:]
        
        data = decodeReadout(readouts)
        print(data)
        alpha = float(data[0])*0.0174533 #yaw 
        beta = float(data[1])*0.0174533 #pitch 
        gamma = float(data[2])*0.0174533 #roll

        # Define the starting point and direction of the arrow
        matrix = np.matrix(([np.cos(beta)*np.cos(gamma), np.sin(alpha)*np.sin(beta)*np.cos(gamma) - np.cos(alpha)*np.sin(gamma), np.cos(alpha)*np.sin(beta)*np.cos(gamma)+ np.sin(alpha)* np.sin(gamma)],
                          [np.cos(beta)*np.sin(gamma), np.sin(alpha)*np.sin(beta)*np.sin(gamma) - np.cos(alpha)*np.cos(gamma), np.cos(alpha)*np.sin(beta)*np.sin(gamma)+ np.sin(alpha)* np.cos(gamma)],
                          [-1*np.sin(beta), np.sin(alpha)*np.cos(beta), np.cos(alpha)*np.cos(beta)]))
        
        start = [0.5, 0.5,0.5]
        direction = np.dot(matrix, [1, 0, 0])

        
        
        res = direction.reshape([1,3])
        direction =  np.ravel(direction)
        direction.flatten()

        #make a unit vector 
        direction/= magnitude(direction)
        direction*=0.05
        print(direction)
        plt.cla()
        #ax.scatter3D(direction[0],direction[1], direction[2], cmap = 'Reds')
        # Plot the arrow
        ax.quiver(start[0], start[1], start[2], direction[0], direction[1], direction[2])
def main():


    setUp()
    i = 0
    animation = FuncAnimation(fig, func = anim, frames=np.arange(0,10,0.01), interval = 10)    
    plt.show()



    # Display the plot
    

if __name__ == "__main__":
    main()