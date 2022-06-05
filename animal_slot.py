import pgzrun      # Pygame Zeroのオブジェクトを使用可能とする
import random

WIDTH   = 420
HEIGHT  = 230
picture = []   #絵柄用のリスト
picture.append(Actor('slot01',topleft=( 30,30)))     # 
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
    screen.clear()    #ウィンドウのクリア
    switch.draw()     #オブジェクトの描画　棒
    ball.draw()       #オブジェクトの描画　棒の上のボール
    for i in range(3):
        picture[i].draw()         #オブジェクトの描画　絵柄
        stop_button[i].draw()     #オブジェクトの描画　ストップボタン

def on_mouse_down(pos):
    global slot_count
    if ball.collidepoint(pos):                     #マウスダウン時、ボールとマウスが衝突してたら
        for i in range(3):
            drum[i] = 0                            #３つのドラムの状態を回転中にする
    else:
        for n in range(3):
            if stop_button[n].collidepoint(pos):   #３つのストップボタンのうち、どれかと衝突したら
                drum[n] = 1                        #衝突したボタンの状態を停止にする

def update():                                     #update関数は、1秒に60回呼び出される
    global slot_count
    global time_count
    time_count += 1                               #1秒間に60回足される
    if time_count == 20:                          #この回数になったら
        time_count = 0                            #カウンタ初期化
        for i in range(3):                        #3つのドラム分繰り返し
            if drum[i]  == 0:                     #回転中のドラムだったら
                slot_count[i] += 1                #スロットの絵柄を順々に変更
                if slot_count[i]  == 8:           #絵柄は1〜7の7種類なので、8になったら1に初期化
                    slot_count[i]  =  1
                # slot_count[i] = random.randrange(1, 7)  #絵柄をランダムに変更してみた
                picture[i].image  =  'slot0' + str(slot_count[i])    #絵柄イメージを変更
pgzrun.go()

