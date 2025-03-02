from pygame import *
from random import *
from time import sleep
init()

scr_size=[800,500]
window=display.set_mode(scr_size)
re=[1]
tax=200
tby=430
ta=tax
tb=tby
tx=100
ty=10
dircx="R"
dirc="D"
cy=randint(30,100)
cx=randint(250,450)

tab=[tax,tby,tx,ty]
clock=time.Clock()
display.set_caption('Tennis')
font = font.SysFont(None, 55)
tscore=0
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    window.blit(screen_text, [x,y])

f=open("D:/table_tennis/main/data.txt","r")
f.seek(0,0)
#print(f.readline())
#print("hiii")
colo="green"
tscore=f.read(2)
f.close()
tab_dir="R"
exitgame=False
score=0

while not exitgame:
    window.fill("black")
    colo="green"
    
    text_screen("Score: " + str(score)+"   highest="+str(tscore) ,"red", 2, 2)
    c=draw.circle(window,"white",(cx,cy),10)
    a=draw.rect(window,colo,Rect(tax,tby,tx,ty))
    
    for x in event.get():
        if x.type==QUIT:
            exit_g=True
            quit()
        
        if x.type==KEYDOWN or x.type==KEYUP:
            if x.key==K_SPACE:
                exitgame=True
            if x.key==K_a:
                sleep(10)
            if x.key==K_RIGHT:
                tax+=30
            if x.key==K_LEFT:
                tax-=30
            if x.key==K_UP:
                tby-=5
            if x.key==K_DOWN:
                if tby<450:
                    tby+=5

    if ((cx>=tax )and (cx<=tax+100))and(cy>tby-5 and cy<tby+5):
            score=score+1
            dirc="U"
    if cy>=440:
        window.fill("white")
        text_screen("Game Over " ,"red", 5, 5)
        display.update()
        sleep(2)
        exitgame=True

    if dirc=="D":
        cy=cy+10
        if dircx=="R":
            cx=cx+10
            if cx>770:
                dircx="L"
        else:
            cx=cx-10
            if cx<30:
                dircx="R"
        if cy>=470:
            dirc="U"

    else :
        cy=cy-10
        if dircx=="R":
            cx=cx+10
            if cx>770:
                dircx="L"
        else:
            cx=cx-10
            if cx<30:
                dircx="R"
        if cy<30:
            dirc="D"

    display.update()
    clock.tick(20)

z=int(score)
y=int(tscore)
if z>y:
    w=str(score)
else:
    w=str(tscore)
f=open("D:/table_tennis/main/data.txt","w")
f.seek(0,0)
f.write(w)
f.close()
quit()