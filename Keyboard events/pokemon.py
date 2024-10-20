import pgzrun
import random
import time

WIDTH, HEIGHT, TITLE = 800,800,'Pokémon'

ash=Actor('ash')
pikachu=Actor('pikachu')

ash.pos=(100, HEIGHT/2)
pikachu.pos=(WIDTH-100, HEIGHT/2)
score=0

isGameOver=False

def moving():
    pikachu.pos=(random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50))
    

def update():
    global score
    if keyboard.w:
        ash.y-=3
    if keyboard.a:
        ash.x-=3
    if keyboard.d:
        ash.x+=3
    if keyboard.s:
        ash.y+=3

    if ash.colliderect(pikachu):
        score+=1
        moving()

def draw():
    screen.clear()
    screen.blit('background2', (0,0))
    screen.draw.text('Score: '+ str(score), (WIDTH-100, 50))
    ash.draw()
    pikachu.draw()
    if isGameOver:
        screen.fill(color=(150,200,100))
        screen.draw.text("Game over\n\nYour final score was: " +str(score), (WIDTH/3, HEIGHT/3), fontsize=50, color=(255,0,255))


def gameover():
    global isGameOver
    isGameOver=True


clock.schedule(gameover, 30.0)



pgzrun.go()