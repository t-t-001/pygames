from itertools import count
import pgzrun

count = 0
turn_card = []
wait_flg = False
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

#カードの表のリスト生成とシャッフル
card_f = []
for i in range(1,5):
    card_f.append('{:02}'.format(i) + 'cardclubs')
    card_f.append('{:02}'.format(i) + 'cardhearts')
random.shuffle(card_f)


#ウィンドウ内の描画
def draw():
    screen.clear()
    for c in card:
        c.draw()
#マウスクリックの処理
def on_mouse_up(pos):
    global count
    global turn_card
    global wait_flg
    if wait_flg:
        return
    for c in card:
        if c.collidepoint(pos):
            c.image = '01cardclubs'
            turn_card.append(c) #めくったカードを記録
            count += 1
    if count == 2:
        count = 0
        clock.schedule_unique(restore,1)
        wait_flg = True  #マウスクリックを無効化
#1秒後にカードを裏に戻す関数
def restore():
    global turn_card
    global wait_flg
    turn_card[0].image  =  card_b
    turn_card[1].image  =  card_b
    turn_card.clear()
    wait_flg = False


pgzrun.go()
