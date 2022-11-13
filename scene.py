# Import the functions from the Draw 2-D library
# so that they can be used in this program.
import random
import math
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing

def draw_pine_tree(canvas, center_x, bottom, height):
    
    """Draw a single pine tree.
    Parameters
        canvas: The canvas where this function
            will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    # Compute the coordinates of the trunk.
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")
    # Compute the coordinates of the skirt
    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="snow1")

def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)
    
    #Snow
    diameter = 15
    space = 5
    interval = diameter + space

    # Draw a rectangular series of circles.
    y = 100
    for row in range(6):
        x = 100
        for cell in range(20):
            draw_oval(canvas, x, y,
                    x + diameter, y + diameter, fill="snow1")
            x += interval
        y += interval

    half_height = round(scene_height / 1.3)
    min_diam = 15
    max_diam = 20

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)

    #Cloud
    draw_cloud(canvas)
    
    # Draw 100 circles, each with
    # a random location and diameter.
    for i in range(150):
        x = random.randint(0, scene_width - max_diam)
        y = random.randint(0, half_height)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter,
                fill="snow1")

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 1.8,
        scene_width, scene_height, width=0, fill="slateGray1", outline = "black")

def draw_cloud(canvas):
    draw_oval(canvas, 50, 490, 300, 400, outline="white", fill="white")
    draw_oval(canvas, 260, 470, 450, 400, outline="white", fill="white")
    draw_oval(canvas, 100, 480, 350, 400, outline="white", fill="white")
#
def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 1.8, width=0, fill="azure1")

    # Draw a pine tree.
    # draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)
    draw_pine_tree(canvas, 100, 100, 200)
    draw_pine_tree(canvas, 400, 75, 150)
    draw_pine_tree(canvas, 700, 150, 310)
    draw_pine_tree(canvas, 250, 250, 100)

# Call the main function so that
# this program will start executing.
main()