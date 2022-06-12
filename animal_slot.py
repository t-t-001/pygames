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
    wheel[n][n].y    =   80  #ホイル0は0番目の絵柄・・・、ホイル2は2番目の絵柄を、y座標80に
    wheel[n][n+1].y  =  -20  #ホイル0は1番目の絵柄・・・、ホイル2は3番目お絵柄を、y座標-20にて初期表示

mask    =   Actor('mask',topleft=(0,0))
switch  =   Actor('laser',topleft=(375,50))
ball    =   Actor('ball_red_small',topleft=(369,50))

stop_button  =  []
stop_button.append(Actor('button_yellow',topleft=( 30,150)))
stop_button.append(Actor('button_yellow',topleft=(140,150)))
stop_button.append(Actor('button_yellow',topleft=(250,150)))

slot_count = [[0,1],[1,2],[2,3]]   # 見えている絵柄
drum = [1,1,1]         # 0:回転中のドラム、1:停止しているドラム
stop_flg = [0,0,0]  # 0：回転中、1:ストップ要求中

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
        animate(ball,pos=(385,165),tween='bounce_end',duration=1)
        for i in range(3):
            drum[i] = 0                            #３つのドラムの状態を回転中にする
            stop_flg[i] = 0
    else:
        for n in range(3):
            if stop_button[n].collidepoint(pos) and drum[n] ==0:   #３つのストップボタンのうち、どれかと衝突したら
                stop_flg[n] = 1

def update():                                     #update関数は、1秒に60回呼び出される
    for i in range(3):
        if drum[i]  == 0:
            rotation(i)

def rotation(num):
    global slot_count
    wheel[num][slot_count[num][0]].y  +=  4
    wheel[num][slot_count[num][1]].y  +=  4
    if wheel[num][slot_count[num][0]].y > 180 and stop_flg[num] == 1:
        drum[num] = 1
    elif wheel[num][slot_count[num][0]].y > 180:
        slot_count[num][0]  +=  1
        slot_count[num][1]  +=  1
        if slot_count[num][0]  == 6:
            slot_count[num][1]  =  0
        elif slot_count[num][0]  == 7:
            slot_count[num][0]  =  0
        wheel[num][slot_count[num][0]].y  =  80
        wheel[num][slot_count[num][1]].y  =  -20
pgzrun.go()

