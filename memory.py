from ctypes import pointer
from email import message
import pgzrun
import time
import random
import math

from sqlalchemy import null

WIDTH  = 610  #ウィンドウの横幅
HEIGHT = 410  #ウィンドウの縦幅
card_w = 140  #カードの横幅
card_h = 190  #カードの縦幅

#カードの表のリスト生成とシャッフル
card_f = []
for i in range(1,5):
    card_f.append('{:02}'.format(i) + 'cardclubs')
    card_f.append('{:02}'.format(i) + 'cardhearts')
random.shuffle(card_f)

#カードの裏
card_b  = 'cardback_blue5'

card      = []    #カードのActor
count     =  0    #めくった順番
total     =  0    #2回めくった回数
turn_card = []    #めくったカード
wait_flg  = False #待ち時間中はTrue 
point     =  0    #数字が揃うと1ポイント

x         = 10    #カード配置用のx座標
y         = 10    #カード配置用のy座標

#カードの生成と配置座標のセット
for i in range(2):
    for n in range(4):
        card.append(Actor(card_b,topleft=(x,y)))
        x += card_w + 10
    x = 10
    y += card_h + 10

#ウィンドウ内の描画
def draw():
    screen.clear()
    if point == len(card)/2:
        message  =  ['Score','Charenge:' +  str(total),'Rate:' +  str(math.floor(point/total*100)) + '%']
        for i in range(3):
            screen.draw.text(message[i],(100,150+i*50), color='orange',fontsize=48)
    else:
        for c in card:
            c.draw()

#マウスクリックの処理
def on_mouse_down(pos):
    global count
    global turn_card
    global wait_flg
    if wait_flg:
        return
    for i in range(len(card)):
        if card[i].collidepoint(pos):
            if card[i].image == card_b:
                card[i].image = card_f[i] #カードを表にする
                turn_card.append(card[i]) #めくったカードを記録
                count += 1
    if count == 2:
        count = 0
        clock.schedule_unique(restore,1)
        wait_flg = True  #マウスクリックを無効化
#1秒後にカードを裏に戻す関数
def restore():
    global point
    global turn_card
    global wait_flg
    global total
    #違う数字ならカードを裏返す
    if turn_card[0].image[:2] != turn_card[1].image[:2]:
        turn_card[0].image = card_b
        turn_card[1].image = card_b
    else:
        point += 1 #同じ数字なら裏返さずにポイントを加算
    total += 1 #2回めくった回数を増やす
    turn_card.clear()
    wait_flg = False
pgzrun.go()
