# set screen width and height
WIDTH = 800
HEIGHT = 400

# create the back layer
back = Actor('double_back')
back.topleft = 0, 0
back.speed = 1

#create the middle layer
middle = Actor('double_middle')
middle.topleft = 0, 0
middle.speed = 3

#create the front layer
front = Actor('double_front')
front.topleft = 0, 0
front.speed = 5

#add images to list
images = [back,middle,front]

def update():
    for i in images:
        # advance each layer
        i.left -= i.speed
        # if layer has moved beyond the left of the screen...
        if i.left <= (WIDTH * -1):
            # ...move back to the right of the screen
            i.left = 0

def draw():
    screen.clear()
    # draw all images in the image list
    for i in images:
        i.draw()
