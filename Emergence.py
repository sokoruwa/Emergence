# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 00:39:52 2019

@author: hrmb

Please use the following link to learn more about GUI programming in python
using tkinter module. 
https://www.geeksforgeeks.org/python-gui-tkinter/

"""

import tkinter
from random import randint

class Emergence:
    
    def __init__(self, gridsize = 10, gridtype = 0):
        """ initialize the emergence grid
        """
        if gridsize > 10:
            print("grid size is reduced to the max size 10")
            self.gridsize = 10
        else:
            self.gridsize = gridsize # number of grid points in each dimension
        
        self.dotsize = 10 # the diameter for each dot
        self.xspace = 40 # the space between two adjacent dots
        self.yspace = self.xspace
        self.numberofcolors = 2 # could be more than 2
        self.TOTALGRIDRATIO = 0.8
        self.gridcolors = [[0] * self.gridsize] * self.gridsize # to save the colors for each point
        self.coords = [[(0,0)] * self.gridsize] * self.gridsize # to save coordinates of grid dots
        self.gridwidth = 0
        self.canvaswidth = 0 
        
        # at this point, we only have one example 10x10 grid
        # if user requires an example grid with size smaller than 10,
        # we will use the top left subsquare of the 10x10 example
        if gridtype == 0 : # use the example grid
            examplegridcolors = [[0, 1, 0, 0, 0, 1, 0, 0, 1, 1], #row 1
                     [1, 1, 0 ,0, 0, 1, 0, 0, 0, 1],  #row 2
                     [0, 0, 0, 1, 1, 0, 1, 0, 0, 1],  #row 3
                     [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],  #row 4
                     [1, 1, 1, 1, 1, 0, 0, 0, 0, 1],  #row 5
                     [0, 0, 1, 0, 0, 1, 1, 0, 0, 1],  #row 6
                     [0, 1, 1, 0, 0, 0, 1, 1, 0, 1],  #row 7
                     [0, 0, 0, 1, 0, 1, 1, 0, 0, 1],
                     [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 0, 1, 1, 0, 1, 1]]
                     
            self.gridcolors = examplegridcolors     
            
        else:
        # initialize the grid using random numbers
            for i in range(self.gridsize):
                for j in range(self.gridsize):
                    self.gridcolors[i][j] = randint(0, self.numberofcolors - 1)
                    
        # initialize the GUI window here. 
        # create the main window
        self.mainwindow = tkinter.Tk() 
        # initialize the canvas to None. 
        self.canvas = None
       
    # use this function for debugging purposes   
    def printGrid(self):
        """ prints the gridcolors in text
        """
        for i in range(self.gridsize):
            for j in range(self.gridsize):
                print(self.gridcolors[i][j] + "\t" , end="")
            print()
    
    # this function make the GUI window 
    def showindow(self):
        self.mainwindow.title("Emergence Grid")
        self.mainwindow.geometry("500x500") # default size of the window
        self.mainwindow.resizable(0, 0)
        self.mainwindow.bind('<Button-1>', self.onMouseClick) # bind the onMouseClick to the left mouse click <Button-1>
        # make the application ready to run. mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event till the window is not closed.
        self.mainwindow.mainloop()
    
    def computeGridLayout(self):
        """ The computeGridLayout method computes the coordinates of the dots
        """
        # compute width and height of the grid
        self.gridwidth = self.gridsize * (self.dotsize + self.xspace)
        self.canvaswidth = self.gridwidth / self.TOTALGRIDRATIO 
        # create canvas
        if self.canvas == None :
            self.canvas = tkinter.Canvas(self.mainwindow, height = self.canvaswidth, width = self.canvaswidth)
        else:
            self.canvas.delete("all") # clear the canvas

        self.canvas.pack() 
        
    def drawGrid(self):
        """ draw the grid dots on canvas
        """
        r = self.dotsize //2
        topLeftCorner_x = (self.canvaswidth - self.gridwidth) //2 # make the grid to be on center of canvas
        topLeftCorner_y = topLeftCorner_x
        
        for i in range(self.gridsize):
            for j in range(self.gridsize):
                # compute the coordinates of grid
                x = topLeftCorner_x + j * self.xspace
                y = topLeftCorner_y + i * self.yspace
                
                if self.gridcolors[i][j] == 0 :
                    color = "blue"
                else:
                    color = "red"
                    
                self.canvas.create_oval(x-r, y-r, x+r, y+r, fill=color) # draw a circle
                
    
    # put your code here. 
    def check_inbounds(self, i, j):  # checks if values of the neighbouring dots are in range of the grid
        if i in range(self.gridsize) and j in range(self.gridsize):
            return True
        else:
            return False
        
    def check_grid(self, a, b): # checks if the neigbors are in bounds of the range and assigns initial dot based on neighboring colours
        count_b = 0
        count_r = 0
        for i in range(a-1,a+2):
            for j in range(b -1, b + 2 ):
                if self.check_inbounds(i, j):
                    if i == a and b == j:  # excludes initial dot
                        count_b += 0
                        count_r += 0
                    elif self.gridcolors[i][j] == 1:
                        count_r += 1 #counts reds
                    else:
                        count_b += 1 #counts blues
                    
        
        if count_r > count_b:
            return 1
        elif count_b > count_r:
            return 0
        else:
            return self.gridcolors[a][b]
                    
            
        
    def updateEmergenceGrid(self):
        """ The updateEmergenceGrid function updates grid based on emergence rules
        """
        new_grid = [[0 for i in range(self.gridsize)] for i in range(self.gridsize)]
        
        for i in range(self.gridsize):
            for j in range(self.gridsize):
                s = self.check_grid(i, j)  # value of new dot
                new_grid[i][j] = s # assigns each value of new dot to each dot in the new grid
        self.gridcolors = new_grid
        print (self.gridcolors)     
                
                    
            
                    
                    
                    
                    
                 
                    
                     
                
                    
                
       
                       
    
    def onMouseClick(self, event):
        """ The onMouseClick event handler will call everytime user clicks on main form.
        """
        # each time you click on the form, you need to recompute grid layout and draw it. 
        # please remove the following two lines when you develope your code.
        
        self.computeGridLayout() # for test purposes
        self.drawGrid() # for test purposes
        self.updateEmergenceGrid()
        
        
        

if __name__ == "__main__":
    
    e = Emergence(10,0)
    e.showindow()

    
# Emergence
