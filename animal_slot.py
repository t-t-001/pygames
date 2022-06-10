import pgzrun      # Pygame Zeroのオブジェクトを使用可能とする
import random

WIDTH   = 420
HEIGHT  = 230

wheel   = [[],[],[]]
for i in range(1,8):
    wheel[0].append(Actor('slot0' + str(i), center=(80,0)))
    wheel[1].append(Actor('slot0' + str(i), center=(190,0)))
    wheel[2].append(Actor('slot0' + str(i), center=(300,0)))

for n in range(3):
    wheel[n][n].y    =   80
    wheel[n][n+1].y  =  -20

mask    =   Actor('mask',topleft=(0,0))
switch  =   Actor('laser',topleft=(375,50))
ball    =   Actor('ball_red_small',topleft=(369,50))

stop_button  =  []
stop_button.append(Actor('button_yellow',topleft=( 30,150)))
stop_button.append(Actor('button_yellow',topleft=(140,150)))
stop_button.append(Actor('button_yellow',topleft=(250,150)))

slot_count = [[0,1],[1,2],[2,3]]   # 見えている絵柄
drum = [1,1,1]         # 0:回転中のドラム、1:停止しているドラム

def draw():
    screen.clear()    #ウィンドウのクリア
    for i in range(3):
        wheel[i][slot_count[i][0]].draw()
        wheel[i][slot_count[i][1]].draw()
    mask.draw()       #オブジェクトの描画　マスク
    switch.draw()     #オブジェクトの描画　棒
    ball.draw()       #オブジェクトの描画　棒の上のボール
    for i in range(3):
        stop_button[i].draw()     #オブジェクトの描画　ストップボタン

def on_mouse_down(pos):
    if ball.collidepoint(pos):                     #マウスダウン時、ボールとマウスが衝突してたら
        for i in range(3):
            drum[i] = 0                            #３つのドラムの状態を回転中にする
    else:
        for n in range(3):
            if stop_button[n].collidepoint(pos):   #３つのストップボタンのうち、どれかと衝突したら
                drum[n] = 1                        #衝突したボタンの状態を停止にする

def update():                                     #update関数は、1秒に60回呼び出される
    for i in range(3):
        if drum[i]  == 0:
            rotation(i)

def rotation(num):
    global slot_count
    wheel[num][slot_count[num][0]].y  +=  1
    wheel[num][slot_count[num][1]].y  +=  1
    if wheel[num][slot_count[num][0]].y > 180:
        slot_count[num][0]  +=  1
        slot_count[num][1]  +=  1
        if slot_count[num][0]  == 6:
            slot_count[num][1]  =  0
        elif slot_count[num][0]  == 7:
            slot_count[num][0]  =  0
        wheel[num][slot_count[num][0]].y  =  80
        wheel[num][slot_count[num][1]].y  =  -20
pgzrun.go()

