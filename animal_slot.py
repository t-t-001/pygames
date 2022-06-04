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

slot_count = [1,2,3]   # 見えている絵柄
drum = [1,1,1]         # 0:回転中のドラム、1:停止しているドラム
time_count = 0         # 経過時間のカウント用(60秒で1)

def draw():
    screen.clear()
    switch.draw()
    ball.draw()
    for i in range(3):
        picture[i].draw()
        stop_button[i].draw()

def on_mouse_down(pos):
    global slot_count
    if ball.collidepoint(pos):
        for i in range(3):
            drum[i] = 0
    else:
        for n in range(3):
            if stop_button[n].collidepoint(pos):
                drum[n] = 1

def update():
    global slot_count
    global time_count
    time_count += 1
    if time_count == 20:
        time_count = 0
        for i in range(3):
            if drum[i]  == 0:
                slot_count[i] += 1
                if slot_count[i]  == 8:
                    slot_count[i]  =  1
                picture[i].image  =  'slot0' + str(slot_count[i])
pgzrun.go()

