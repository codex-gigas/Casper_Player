try:
    from tkinter import messagebox
except:
    # Python 2
    import tkMessageBox as messagebox

from tkinter import *
from tkinter import filedialog
import threading
from pygame import mixer
from mutagen.mp3 import MP3
from ttkthemes import themed_tk as tk
import os
from tkinter import ttk
import playlist_window as pw
import easygui
import time
import player
import casper_functions as cf

#Creating window
root=Tk()
#root.get_themes()
#root.set_theme("equilux")
root.configure(background='black')



# Status Bar after it will be  Progress Bar

#progress_bar = ttk.Progressbar(root, orient='horizontal', mode='determinate', length=500)
#progress_bar.pack()

#StatusBar = Label(root, text = "Casper Welcomes You", relief = SUNKEN, anchor = W)
#StatusBar.pack(side = BOTTOM, fill = X)

# Creating functions and triggering events
def on_close():
    cf.stop_music()
    if(pw.windowopened == TRUE):
        pw.Close()
    root.destroy()





'''
def set_volume(val):
    global volume
    volume = float(val)/100
    mixer.music.set_volume(volume)

    #print("Paused!")
'''






# End of Functions and Events

# Creating Frames LEFT AND RIGHT

leftframe = Frame(root, bg = "black")
leftframe.pack(side=LEFT)

rightframe = Frame(root, bg = "black")
rightframe.pack(side=RIGHT)

topframe = Frame(rightframe)
topframe.pack()

middleframe = Frame(rightframe)
middleframe.pack(padx=10,pady=10)


#bottomframe = Frame(rightframe)
#bottomframe.pack(padx=30,pady=30)






#creating menu bar
menubar = Menu(root)
root.config(menu = menubar) # Configuration of Menubar
 # Creating Submenu
submenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = submenu)
#submenu.add_command(label = "New Playlist", command = New_Playlist)
submenu.add_command(label = "Playlist", command = pw.Open_Playlist)
submenu.add_command(label = "Exit", command = root.destroy)

submenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Select", menu = submenu)
submenu.add_command(label = "Play", command = cf.default_songs)
submenu.add_command(label = "Previos", command = cf.previos_music)
submenu.add_command(label = "Next", command = cf.next_music)
submenu.add_command(label = "Pause", command = cf.pause_music)
submenu.add_command(label = "Stop", command = cf.stop_music)
submenu.add_command(label = "Clear cache", command = cf.Clear_Cache)


#submenu = Menu(menubar, tearoff = 0)
#menubar.add_cascade(label = "Tools", menu = submenu)
#submenu.add_command(label = "Settings", command = cf.Open_Settings)

submenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Help", menu = submenu)
submenu.add_command(label = "About us", command = cf.AboutUs)
#submenu.add_command(label = "Manual", command = User_Manual)

mixer.init()  # Inisitization of Mixer
root.geometry('420x125') # Window Dimenstions
root.title("Casper")
root.iconbitmap(r"caspericon.ico")


lefttopframe = Frame(leftframe,bg="black")
lefttopframe.pack()

cf.text = Label(lefttopframe,text = "Casper", anchor = W, fg="white", bg = "black", font= "san-sarf 10 bold")
cf.text.pack(padx=15,pady=5)

#labelimg = Label(root, image = _img)
#labelimg.pack()

#cf.currtime = Label(leftframe, text = "00:00", font = "DS-Digital 20", fg="white", bg="black")
#cf.currtime.pack(side = LEFT, padx = 12, pady= 10)

#cf.totaltime = Label(leftframe, text = "00:00", font = "DS-Digital 20", fg="white", bg="black")
#cf.totaltime.pack(side = LEFT, padx = 2)




#Next button
_NextImg = PhotoImage(file = "images/next_track.gif")
cf.NextBtn = ttk.Button(middleframe, image = _NextImg, command=cf.next_music)
cf.NextBtn.pack(side = RIGHT)


_PauseImg = PhotoImage(file = "images/pause.gif")
cf.PauseBtn = ttk.Button(middleframe, image = _PauseImg,command=cf.pause_music)
cf.PauseBtn.pack(side = RIGHT)


#  PLay button
_PlayImg = PhotoImage(file = "images/play.gif")
cf.PlayBtn = ttk.Button(middleframe, image = _PlayImg,command=cf.default_songs)
cf.PlayBtn.pack(side = RIGHT)


# Previous button
_Previousimg = PhotoImage(file = "images/previous_track.gif")
cf.PreviousBtn = ttk.Button(middleframe, image = _Previousimg, command=cf.previos_music)
cf.PreviousBtn.pack(side = RIGHT)





'''
scale =ttk.Scale(topframe, from_ = 0, to = 100, orient = HORIZONTAL, command = set_volume)
scale.set(60)
mixer.music.set_volume(0.6)
scale.pack(side = LEFT)
'''


root.resizable(0,0)

root.protocol("WM_DELETE_WINDOW",on_close)
root.mainloop()
