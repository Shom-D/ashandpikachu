import pgzrun
import random
import time


WIDTH, HEIGHT, TITLE= 625,475, 'Game'

tom= Actor("tom")
jerry= Actor("jerry")
score=0


tom.pos= (100,300)
jerry.pos= (WIDTH-100, HEIGHT/2)
isGameOver= False

def moving():
    jerry.pos= (random.randint(50,WIDTH-50), random.randint(50,HEIGHT-50))

def update():
    global score
    if keyboard.left:
        tom.x -= 3
    if keyboard.right:
        tom.x += 3
    if keyboard.up:
        tom.y -=3
    if keyboard.down:
        tom.y += 3

    if tom.colliderect(jerry):
        score+=1
        moving()

    
def draw():
    global score
    screen.clear()
    screen.blit("background", (0,0))
    tom.draw()
    jerry.draw()
    screen.draw.text('Score: '+ str(score), (WIDTH-100, 25))
    if isGameOver:
        screen.fill(color=(150,100,100))

        message= "Game over\n\nYour final score was: " +str(score)
        screen.draw.text(message, (WIDTH/3, HEIGHT/3), fontsize=30, color=(255,255,0))



def gameOver():
    global isGameOver
    isGameOver=True
    

clock.schedule(gameOver, 10.0)

pgzrun.go()