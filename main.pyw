import os
from tkinter import *
from tkinter.messagebox import showinfo
from random import randint

HEIGHT = 4
WIDTH = 4

mp = [[0 for _ in range(WIDTH)] for i in range(HEIGHT)]
canadd = 1
score = 0
highscore = 0

if os.path.exists("config.ini"):
    with open("config.ini", mode="r") as file:
        highscore = int(file.readline().strip())
        
def main():
    global HEIGHT, WIDTH, mp, canadd, score

    win = Tk()
    win.title("2048  -- By lanlan2_")
    win.resizable(0, 0)
    win.iconbitmap("icon.ico")
    win.geometry("+300+200")

    can = Canvas(win,
                 highlightthickness=0,
                 bg="OldLace",
                 height=HEIGHT*80+50,
                 width=WIDTH*80+250)
    can.create_rectangle(20, 20, WIDTH*80+30, HEIGHT*80+30, fill="DimGrey", outline="DimGrey")
    can.create_text(WIDTH*80+140, 50, text="2048", fill="Black", font=("Arial Black",48,"bold"))
    can.create_rectangle(WIDTH*80+50, 100, WIDTH*80+230, 200, fill="Tan", outline="Tan")
    can.create_rectangle(WIDTH*80+50, 220, WIDTH*80+230, 320, fill="Tan", outline="Tan")
    can.create_text(WIDTH*80+140, 120, text="当前分数:", font=("黑体",18))
    can.create_text(WIDTH*80+140, 240, text="最高分数:", font=("黑体",18))
    iid1 = can.create_text(WIDTH*80+140, 160, text=str(score), font=("consolas",20))
    iid2 = can.create_text(WIDTH*80+140, 280, text=str(highscore), font=("consolas",20))
    
    def redraw():
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if mp[i][j] == 0:
                    can.create_rectangle(j*80+30, i*80+30, j*80+100, i*80+100, fill="Grey", outline="Grey")
                    #can.create_text(j*80+65, i*80+65, text="0", font=("Arial Black",32,"bold"), fill="WhiteSmoke")
                elif mp[i][j] == 2:
                    can.create_rectangle(j*80+30, i*80+30, j*80+100, i*80+100, fill="LightGrey", outline="LightGrey")
                    can.create_text(j*80+65, i*80+65, text=str(mp[i][j]), font=("Arial Black",32,"bold"), fill="Black")
                elif mp[i][j] == 4:
                    can.create_rectangle(j*80+30, i*80+30, j*80+100, i*80+100, fill="LemonChiffon", outline="LemonChiffon")
                    can.create_text(j*80+65, i*80+65, text=str(mp[i][j]), font=("Arial Black",32,"bold"), fill="Black")
                elif mp[i][j] == 8:
                    can.create_rectangle(j*80+30, i*80+30, j*80+100, i*80+100, fill="DarkSalmon", outline="DarkSalmon")
                    can.create_text(j*80+65, i*80+65, text=str(mp[i][j]), font=("Arial Black",32,"bold"), fill="WhiteSmoke")
                elif mp[i][j] == 16:
                    can.create_rectangle(j*80+30, i*80+30, j*80+100, i*80+100, fill="LightCoral", outline="LightCoral")
                    can.create_text(j*80+65, i*80+65, text=str(mp[i][j]), font=("Arial Black",32,"bold"), fill="WhiteSmoke")
                elif mp[i][j] == 32:
                    can.create_rectangle(j*80+30, i*80+30, j*80+100, i*80+100, fill="IndianRed", outline="IndianRed")
                    can.create_text(j*80+65, i*80+65, text=str(mp[i][j]), font=("Arial Black",32,"bold"), fill="WhiteSmoke")
                elif mp[i][j] == 64:
                    can.create_rectangle(j*80+30, i*80+30, j*80+100, i*80+100, fill="Red", outline="Red")
                    can.create_text(j*80+65, i*80+65, text=str(mp[i][j]), font=("Arial Black",32,"bold"), fill="WhiteSmoke")
                elif mp[i][j] == 128:
                    can.create_rectangle(j*80+30, i*80+30, j*80+100, i*80+100, fill="NavajoWhite", outline="NavajoWhite")
                    can.create_text(j*80+65, i*80+65, text=str(mp[i][j]), font=("Arial Black",24,"bold"), fill="WhiteSmoke")
                elif mp[i][j] == 256:
                    can.create_rectangle(j*80+30, i*80+30, j*80+100, i*80+100, fill="Wheat", outline="Wheat")
                    can.create_text(j*80+65, i*80+65, text=str(mp[i][j]), font=("Arial Black",24,"bold"), fill="WhiteSmoke")
                elif mp[i][j] == 512:
                    can.create_rectangle(j*80+30, i*80+30, j*80+100, i*80+100, fill="BurlyWood", outline="BurlyWood")
                    can.create_text(j*80+65, i*80+65, text=str(mp[i][j]), font=("Arial Black",24,"bold"), fill="WhiteSmoke")
                elif mp[i][j] == 1024:
                    can.create_rectangle(j*80+30, i*80+30, j*80+100, i*80+100, fill="SandyBrown", outline="SandyBrown")
                    can.create_text(j*80+65, i*80+65, text=str(mp[i][j]), font=("Arial Black",18,"bold"), fill="WhiteSmoke")
                elif mp[i][j] == 2048:
                    can.create_rectangle(j*80+30, i*80+30, j*80+100, i*80+100, fill="Orange", outline="Orange")
                    can.create_text(j*80+65, i*80+65, text=str(mp[i][j]), font=("Arial Black",18,"bold"), fill="WhiteSmoke")
                else:
                    if len(str(mp[i][j])) == 4:
                        can.create_rectangle(j*80+30, i*80+30, j*80+100, i*80+100, fill="DeepPink", outline="DeepPink")
                        can.create_text(j*80+65, i*80+65, text=str(mp[i][j]), font=("Arial Black",18,"bold"), fill="WhiteSmoke")
                    else:
                        can.create_rectangle(j*80+30, i*80+30, j*80+100, i*80+100, fill="Magenta", outline="Magenta")
                        can.create_text(j*80+65, i*80+65, text=str(mp[i][j]), font=("Arial Black",15,"bold"), fill="WhiteSmoke")  
    can.pack()

    def checkiflose():
        global canadd
        s = 0
        for i in mp:
            for j in i:
                if j != 0:
                    s += 1
                if j >= 2048:
                    win.unbind("<KeyPress>")
                    showinfo("提示", "恭喜，你成功了！")
                    
        if s == HEIGHT * WIDTH:
            canadd = 0
            
            def combineup(amp):
                for i in range(WIDTH):
                    li = []
                    for j in range(HEIGHT):
                        if amp[j][i] != 0:
                            li.append(amp[j][i])
                            amp[j][i] = 0
                    if li != []:
                        for m in list(enumerate(li)):
                            amp[m[0]][i] = m[1]
                for i in range(WIDTH):
                    for j in range(HEIGHT):
                        if amp[j][i] != 0 and j != HEIGHT - 1:
                            if amp[j][i] == amp[j+1][i]:
                                amp[j][i] *= 2
                                amp[j+1][i] = 0
                return amp
            
            def combinedown(amp):
                for i in range(WIDTH):
                    li = []
                    for j in range(HEIGHT):
                        if amp[j][i] != 0:
                            li.append(amp[j][i])
                            amp[j][i] = 0
                    if li != []:
                        for m in list(enumerate(li[::-1])):
                            amp[HEIGHT-m[0]-1][i] = m[1]
                            
                for i in range(WIDTH):
                    for j in range(HEIGHT-1,-1,-1):
                        if amp[j][i] != 0 and j != 0:
                            if amp[j][i] == amp[j-1][i]:
                                amp[j][i] *= 2
                                amp[j-1][i] = 0
                return amp

            def combineleft(amp):
                for i in range(HEIGHT):
                    li = []
                    for j in range(WIDTH):
                        if amp[i][j] != 0:
                            li.append(amp[i][j])
                            amp[i][j] = 0
                    if li != []:
                        for m in list(enumerate(li)):
                            amp[i][m[0]] = m[1]
                for i in range(HEIGHT):
                    for j in range(WIDTH):
                        if amp[i][j] != 0 and j != WIDTH - 1:
                            if amp[i][j] == amp[i][j+1]:
                                amp[i][j] *= 2
                                amp[i][j+1] = 0
                return amp

            def combineright(amp):
                for i in range(HEIGHT):
                    li = []
                    for j in range(WIDTH):
                        if amp[i][j] != 0:
                            li.append(amp[i][j])
                            amp[i][j] = 0
                    if li != []:
                        for m in list(enumerate(li[::-1])):
                            amp[i][WIDTH-m[0]-1] = m[1]
                            
                for i in range(HEIGHT):
                    for j in range(WIDTH-1,-1,-1):
                        if amp[i][j] != 0 and j != 0:
                            if amp[i][j] == amp[i][j-1]:
                                amp[i][j] *= 2
                                amp[i][j-1] = 0
                return amp
            
            if [[n for n in m] for m in mp] == combineup([[n for n in m] for m in mp]) and [[n for n in m] for m in mp] == combinedown([[n for n in m] for m in mp]) and [[n for n in m] for m in mp] == combineleft([[n for n in m] for m in mp]) and [[n for n in m] for m in mp] == combineright([[n for n in m] for m in mp]):
                win.unbind("<KeyPress>")
                showinfo("提示", "很遗憾，你失败了！")
        else:
            canadd = 1
            

    def add():
        global canadd
        if canadd == 1:
            while True:
                a = randint(0, HEIGHT-1)
                b = randint(0, WIDTH-1)
                if mp[a][b] == 0:
                    mp[a][b] = 2
                    break
    add()
    redraw()
    
    def move(event):
        def up():
            def combine():
                global score, highscore
                for i in range(WIDTH):
                    li = []
                    for j in range(HEIGHT):
                        if mp[j][i] != 0:
                            li.append(mp[j][i])
                            mp[j][i] = 0
                    if li != []:
                        for m in list(enumerate(li)):
                            mp[m[0]][i] = m[1]
                            
                for i in range(WIDTH):
                    for j in range(HEIGHT):
                        if mp[j][i] != 0 and j != HEIGHT - 1:
                            if mp[j][i] == mp[j+1][i]:
                                mp[j][i] *= 2
                                mp[j+1][i] = 0
                                score += mp[j][i]
                                can.itemconfigure(iid1, text=score)
                                if score > highscore:
                                    highscore = score
                                    can.itemconfigure(iid2, text=highscore)
                                    with open("config.ini", mode="w") as file:
                                        file.write(str(highscore))                                
            combine()
            current = [[n for n in m] for m in mp]
            combine()
            if current != [[n for n in m] for m in mp]:
                up()
                
        def down():
            def combine():
                global score, highscore
                for i in range(WIDTH):
                    li = []
                    for j in range(HEIGHT):
                        if mp[j][i] != 0:
                            li.append(mp[j][i])
                            mp[j][i] = 0
                    if li != []:
                        for m in list(enumerate(li[::-1])):
                            mp[HEIGHT-m[0]-1][i] = m[1]
                            
                for i in range(WIDTH):
                    for j in range(HEIGHT-1,-1,-1):
                        if mp[j][i] != 0 and j != 0:
                            if mp[j][i] == mp[j-1][i]:
                                mp[j][i] *= 2
                                mp[j-1][i] = 0
                                score += mp[j][i]
                                can.itemconfigure(iid1, text=score)
                                if score > highscore:
                                    highscore = score
                                    can.itemconfigure(iid2, text=highscore)
                                    with open("config.ini", mode="w") as file:
                                        file.write(str(highscore))
            combine()
            current = [[n for n in m] for m in mp]
            combine()
            if current != [[n for n in m] for m in mp]:
                down()
                
        def left():
            def combine():
                global score, highscore
                for i in range(HEIGHT):
                    li = []
                    for j in range(WIDTH):
                        if mp[i][j] != 0:
                            li.append(mp[i][j])
                            mp[i][j] = 0
                    if li != []:
                        for m in list(enumerate(li)):
                            mp[i][m[0]] = m[1]
                            
                for i in range(HEIGHT):
                    for j in range(WIDTH):
                        if mp[i][j] != 0 and j != WIDTH - 1:
                            if mp[i][j] == mp[i][j+1]:
                                mp[i][j] *= 2
                                mp[i][j+1] = 0
                                score += mp[i][j]
                                can.itemconfigure(iid1, text=score)
                                if score > highscore:
                                    highscore = score
                                    can.itemconfigure(iid2, text=highscore)
                                    with open("config.ini", mode="w") as file:
                                        file.write(str(highscore))
            combine()
            current = [[n for n in m] for m in mp]
            combine()
            if current != [[n for n in m] for m in mp]:
                left()

        def right():
            def combine():
                global score, highscore
                for i in range(HEIGHT):
                    li = []
                    for j in range(WIDTH):
                        if mp[i][j] != 0:
                            li.append(mp[i][j])
                            mp[i][j] = 0
                    if li != []:
                        for m in list(enumerate(li[::-1])):
                            mp[i][WIDTH-m[0]-1] = m[1]
                            
                for i in range(HEIGHT):
                    for j in range(WIDTH-1,-1,-1):
                        if mp[i][j] != 0 and j != 0:
                            if mp[i][j] == mp[i][j-1]:
                                mp[i][j] *= 2
                                mp[i][j-1] = 0
                                score += mp[i][j]
                                can.itemconfigure(iid1, text=score)
                                if score > highscore:
                                    highscore = score
                                    can.itemconfigure(iid2, text=highscore)
                                    with open("config.ini", mode="w") as file:
                                        file.write(str(highscore))
                                
            combine()
            current = [[n for n in m] for m in mp]
            combine()
            if current != [[n for n in m] for m in mp]:
                right()
                        
        if event.keysym == "Up":
            up()
        elif event.keysym == "Down":
            down()
        elif event.keysym == "Left":
            left()
        elif event.keysym == "Right":
            right()
        else:
            return
        
        add()
        redraw()
        checkiflose()
                
    win.bind("<KeyPress>", move)
    win.mainloop()

if __name__ == "__main__":
    main()
