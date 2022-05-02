import pgzrun

WIDTH  = 610
HEIGHT = 410
card_w = 140
card_h = 190

card_b  = 'cardback_blue5'
card = []
x = 10
y = 10
m = 10
w = 4
h = 2

for i in range(h):
    for n in range(w):
        card.append(Actor(card_b,topleft=(x,y)))
        x += card_w + m
    x = m
    y += card_h + m

def draw():
    screen.clear()
    for c in card:
        c.draw()
pgzrun.go()
