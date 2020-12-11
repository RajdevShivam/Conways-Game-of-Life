import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def randomInitialise(n_rows, n_cols, prob=0.1):
    """
    DESCRIPTION: This Function randomly initialises numpy array of n_rows, n_cols with probablity of 1 being prob
    INPUT: n_rows-> Number of rows of needed numpy array
           n_cols-> Number pf columns of needed numpy array
           prob-> probablity of initialising it with 1
    OUTPUT: numpy array of shape (n_rows, n_cols) with 1, 0 of probablity of prob and 1-prob respectively
    """
    return np.random.choice([1,0], n_rows*n_cols, p=[prob, 1-prob]).reshape(n_rows, n_cols)

def countNeighbours(X,Y, grid):
    """
    DESCRIPTION: This function counts number of neighbours of a cell in a binary array of 0's and 1's
                 assuming the surface of the grid is toroidal in shape
    INPUT: Cell position
            X-> Row Number of the cell
            Y-> Column number of the cell
            grid-> grid in which cell belongs and we want to calculate neighbours from
    OUTPUT: Number of Neighbours
    """
    s=0
    n_rows=grid.shape[0]
    n_cols=grid.shape[1]
    for i in range(-1,2):
        for j in range(-1,2):
            #Making the surface toroid
            row= (X+i+n_rows)%n_rows
            col= (Y+j+n_cols)%n_cols
            s+=grid[row][col]
    s-=grid[X][Y]
    return s

def step(i,  grid, img):
    #print(i)
    newGrid= np.zeros(grid.shape, dtype=int)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            neighbours= countNeighbours(i, j, grid)
            #Apply Conway's rule
            if(grid[i][j]==1):
                if(neighbours<2 or neighbours>3):
                    newGrid[i][j]=0
                else:
                    newGrid[i][j]=1
            else:
                if(neighbours==3):
                    newGrid[i][j]=1
    
    #Set the updated grid in the image           
    img.set_data(255*newGrid)
    grid[:] = newGrid[:]

    return img,

def main():
    
    N=20                    #Value of N should be greater than or equal to 3
    updateInterval = 500    #Interval Between Frames in Milli-Second
    totalSteps=50           #Total Number of times the new step should take place
    name="example"          #Name of the video file which we want to generate
    
    #Randomly initialise 0's and 1's in the array
    #grid=randomInitialise(N,N)
    
    #Fill the array with 0's
    grid= np.zeros((N,N))
    
    #Fill the required portion of array 
    grid[9:12, 9:12]= np.array([[1,1,1],
                               [1,0,1],
                               [1,1,1]])    
    
    #Make animation by repeatedly calling the function
    fig, ax = plt.subplots()
    img = ax.imshow( 255*grid, interpolation='nearest' )
    ani = animation.FuncAnimation(fig, step, frames=totalSteps,
                                  fargs=(grid, img,), 
                                  interval=updateInterval) 

    #Save the animation
    ani.save(name+".mp4", writer='ffmpeg')
    plt.close()
    
    
if __name__=="__main__":
    main()