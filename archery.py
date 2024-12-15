import pgzrun
import random

WIDTH= 700
HEIGHT= 600

bow= Actor("bow&arrow.png")
target= Actor("target.png")

bow.pos= (WIDTH//2, HEIGHT- 60)
speed= 5
targets= []
arrows= []
score= 0

targets.append(target)
targets[-1].x = 10
targets[-1].y = 100

def draw():
    screen.clear()
    screen.fill("royal blue")
    bow.draw()
    screen.draw.text("Score = "+ str(score), (50,50))
    for e in targets:
        e.draw()

def update():
    global score
    if keyboard.left:
        bow.x -= speed
        if bow.x <= 40:
            bow.x= 40
    elif keyboard.right:
        bow.x += speed
        if bow.x >= WIDTH- 40:
            bow.x= WIDTH - 40
    for e in targets:
        e.y += 5
        if e.y >= HEIGHT:
            e.y= -100
            e.x = random.randint(40, WIDTH- 40)







pgzrun.go()