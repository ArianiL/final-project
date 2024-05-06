import turtle

# Function to set up the turtle
def setup():
    turtle.setup(800, 600)
    turtle.title("Simple Drawing Program")
    turtle.speed(0)
    turtle.pensize(2)
    turtle.pencolor("black")

# Function to draw a line
def draw_line(x, y):
    if turtle.isdown():
        turtle.ondrag(None)  # Disable event handling while drawing
        turtle.goto(x, y)
        turtle.ondrag(draw_line)  # Re-enable event handling

# Function to change color to red
def set_red():
    turtle.pencolor("red")

# Function to change color to blue
def set_blue():
    turtle.pencolor("blue")

# Function to change color to green
def set_green():
    turtle.pencolor("green")

# Function to clear the screen
def clear_screen():
    turtle.clear()

# Function to erase
def erase():
    turtle.pencolor("white")
    turtle.pensize(20)

# Function to reset the pen
def reset_pen():
    turtle.pencolor("black")
    turtle.pensize(2)

# Function to increase brush size
def increase_brush_size():
    pen_size = turtle.pensize()
    turtle.pensize(pen_size + 1)

# Function to decrease brush size
def decrease_brush_size():
    pen_size = turtle.pensize()
    if pen_size > 1:
        turtle.pensize(pen_size - 1)

def main():
    setup()

    # Set up event listeners
    turtle.onscreenclick(draw_line)
    turtle.onkeypress(set_red, "r")
    turtle.onkeypress(set_blue, "b")
    turtle.onkeypress(set_green, "g")
    turtle.onkeypress(clear_screen, "c")
    turtle.onkeypress(erase, "e")
    turtle.onkeypress(reset_pen, "p")
    turtle.onkeypress(increase_brush_size, "Up")
    turtle.onkeypress(decrease_brush_size, "Down")

    # Listen for events
    turtle.listen()
    turtle.mainloop()

if __name__ == "__main__":
    main()
