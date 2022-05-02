import pgzrun

WIDTH  = 200
HEIGHT = 200
card = Actor('cardclubsa',center=(100,100))

def draw():
    screen.clear()
    card.draw()
    
pgzrun.go()
