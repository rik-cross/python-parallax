# set screen width and height
WIDTH = 800
HEIGHT = 400

# create 2 parts of the back layer
back1 = Actor('back')
back1.topleft = 0, 0
back1.speed = 1
back2 = Actor('back')
back2.topleft = WIDTH, 0
back2.speed = 1

#create 2 parts of the middle layer
middle1 = Actor('middle')
middle1.topleft = 0, 0
middle1.speed = 3
middle2 = Actor('middle')
middle2.topleft = WIDTH, 0
middle2.speed = 3

#create 2 parts of the front layer
front1 = Actor('front')
front1.topleft = 0, 0
front1.speed = 5
front2 = Actor('front')
front2.topleft = WIDTH, 0
front2.speed = 5

#add images to list
images = [back1,back2,middle1,middle2,front1,front2]

def update():
    for i in images:
        # advance each layer
        i.left -= i.speed
        # if layer has moved beyond the left of the screen...
        if i.left <= (WIDTH * -1):
            # ...move back to the right of the screen
            i.left += WIDTH * 2

def draw():
    screen.clear()
    # draw all images in the image list
    for i in images:
        i.draw()
