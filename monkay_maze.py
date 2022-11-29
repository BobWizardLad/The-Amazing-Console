from pyamaze import maze
import turtle
def findx_main():
    # create turtle
    myTurtle = turtle.Turtle()
    wn = turtle.Screen()
    wn.setup(width=860, height=750)

    # create maze
    m=maze()
    m.CreateMaze()
    m.run()


    turtle.done()
    wn.mainloop()