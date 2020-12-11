# Conways-Game-of-Life
All the codes are written in python IDE Spyder(Python 3.7)
Make sure libraries like numpy and matplotlib are already installed.
Make sure that ffmpeg is installed on your laptop. If it is not installed then follow instructions
given in the link to install: http://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/

Please note that instead of simulating infinite 2d orthogonal plane, I have simulated a toroidal 
surface. This is because computer has finite memory and computing power. It is impossible to simulate 
infinite 2d plane with finite computing power.

Initialising the parameter:
Change the values in main function and run the file again:
N= Determines the size of grid. Should be greater than 3 (current value 20)
updateInterval= Change it to change interval between frames in Milli-Second (current value 500)
totalSteps= Total number of time steps for which we want to simulate the universe
name= Name of the file in which we want to store the value. Please write the name without extension

In my screen 0's(dead) are shown by purpleish color and 1's(alive) are shown by yellow color.
Color scheme on your pc may differ. 

To initialize the starting state we must use numpy array of 0's and 1's. Fill create NxN array of 0's.
Then fill in the 1's(alive squares) wherever we want to. After the code is executed, open and see the
video file generated and see the result.
