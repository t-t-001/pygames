import pgzrun

WIDTH  = 200
HEIGHT = 200
card = Actor('cardclubsa',midright=(0,100))

def draw():
    screen.clear()
    card.draw()

def update():
    card.x += 1
    # card.left += 1
    
pgzrun.go()
