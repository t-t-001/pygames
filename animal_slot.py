import pgzrun

WIDTH   = 420
HEIGHT  = 230
picture = []
picture.append(Actor('slot01',topleft=( 30,30)))
picture.append(Actor('slot02',topleft=(140,30)))
picture.append(Actor('slot03',topleft=(250,30)))
switch = Actor('laser',topleft=(375,50))
ball   = Actor('ball_red_small',topleft=(369,50))

stop_button  =  []
stop_button.append(Actor('button_yellow',topleft=( 30,150)))
stop_button.append(Actor('button_yellow',topleft=(140,150)))
stop_button.append(Actor('button_yellow',topleft=(250,150)))

def draw():
    for i in range(3):
        picture[i].draw()
        stop_button[i].draw()
    switch.draw()
    ball.draw()
pgzrun.go()

