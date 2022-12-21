from tkinter import *
import math

pink = "#e2979c"
red = "#e7305b"
green = "#9bdeac"
yellow = "#f7f5dd"
font_name = "courier"
work_min = 1
short_break_min = 5
long_break_min = 20
reps = 0
def reset_timer():
    window.after_cancel
def start_timer():
    
    global reps
    reps += 1 
    work_sec= work_min*60
    short_break_sec = short_break_min*60
    long_break_sec = long_break_min*60

    
    if reps % 8 ==0:
        count_time(long_break_sec)
    elif reps %2 ==0:        
        count_time(short_break_sec)
    else:
        count_time(work_sec)    
def count_time(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvase.itemconfig(time_fun,text=f"{count_min}:{count_sec}")
    if count>0:
        window.after(1000,count_time,count-1)
    else:
        count_time(work_min)    

window = Tk()
window.title("pomodoro")

window.config(padx=280,pady=280,bg=yellow)
title = Label(text="Timer",fg=green,bg=yellow,font=(font_name,50,"bold"))
title.grid(column=1,row=0)
#creat canvase#

canvase = Canvas(width=200,height=224,bg=yellow,highlightthickness=0)
#input to how object are fiting in canvase
tomato_image = PhotoImage(file="tomato.png")
#creaet image and fit image in canves

canvase.create_image(100,112,image=tomato_image)


time_fun=canvase.create_text(100,140,text="00:00",fill="white",font=(font_name,35,"bold"))
canvase.grid(column=1,row=1)
#count_time(5)
start_button = Button(text="start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)
reset_button = Button(text="reset",highlightthickness=0)
reset_button.grid(column=2,row=2)
window.minsize(width=500,height=480)
lable_check = Label(text="✔",highlightthickness=0,fg="green",bg="white",font=(font_name,15,"bold"))
lable_check.grid(column=1,row=3)
window.mainloop()
