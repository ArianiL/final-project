# Drawing Program

## Demo
Demo Video: https://youtu.be/tig5fasm2xA 

## GitHub Repository
GitHub Repo: https://github.com/ArianiL/final-project 

## Description
This Python program creates a simple drawing program using the `turtle` module, similar to basic drawing features found in software like Procreate. Here's what the program does:

1. Setup Function (`setup()`):
   - Initializes the turtle graphics window with a size of 800x600 pixels.
   - Sets the window title to "Simple Drawing Program".
   - Sets the drawing speed to maximum.
   - Sets the initial pen size to 2 pixels.
   - Sets the initial pen color to black.

2. Draw Function (`draw_line(x, y)`):
   - Draws a line when the mouse is dragged, moving the turtle to the specified coordinates.

3. Color Functions (`set_red()`, `set_blue()`, `set_green()`):
   - Changes the pen color to red, blue, or green, respectively.

4. Clear Screen Function (`clear_screen()`):
   - Clears the drawing from the screen.

5. Eraser Function (`erase()`):
   - Turns the pen color to white and increases the pen size to 20 pixels, effectively acting as an eraser.

6. Reset Pen Function (`reset_pen()`):
   - Resets the pen color to black and the pen size to 2 pixels, reverting the pen back to its default drawing settings.

7. Brush Size Functions (`increase_brush_size()`, `decrease_brush_size()`):
   - Increases or decreases the brush size by one pixel.

8. Main Function (`main()`):**
   - Calls the `setup()` function to set up the drawing program.
   - Sets up event listeners for drawing lines, changing colors, clearing the screen, erasing, and adjusting the brush size.
   - Listens for events and starts the turtle graphics event loop.

9. Execution Block:
   - Calls the `main()` function when the script is executed as the main program.