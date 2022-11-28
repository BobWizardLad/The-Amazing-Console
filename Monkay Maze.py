#create turtle
import turtle
myTurtle = turtle.Turtle()
wn = turtle.Screen()
wn.setup(width=860,height=750)

#create maze
from pyamaze import maze
m=maze()
m.CreateMaze()
m.run()


turtle.done()
wn.mainloop()