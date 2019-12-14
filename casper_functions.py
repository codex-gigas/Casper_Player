try:
    from tkinter import messagebox
except:
    # Python 2
    import tkMessageBox as messagebox
import pygame
from tkinter import *
from tkinter import filedialog
import threading
from pygame import mixer
from mutagen.mp3 import MP3
from ttkthemes import themed_tk as tk
import os,shutil
from tkinter import ttk
import playlist_window as pw
import easygui
import time
import player

Mpaused = FALSE

def pause_music():
    global Mpaused
    Mpaused = TRUE
    #_PlayImg = PhotoImage(file = "images/play.gif")
    #PlayBtn.configure(image = _PlayImg, command = play_music)
    mixer.music.pause()
    #StatusBar['text'] = "Paused!"

def default_songs():
    global Mpaused
    cache_path = "cache"
    cache_songs = os.listdir(cache_path)
    if Mpaused:
        mixer.music.unpause()
        #StatusBar['text'] = "Resumed" + ' ' + os.path.basename(file_data[0]) + ' ...'
        Mpaused = FALSE

    elif(len(cache_songs)!=0):
        for song_item in cache_songs:
            default_songs_path = cache_path + "/" + song_item
            play_music(default_songs_path)

    else:
            messagebox.showerror("Recent Files","Recent Files are empty or Something is playing already")

def play_music(songpath):
    global filename
    filename = songpath
    print(filename)
    #Song_details(filename)
    global Mpaused

    #PlayBtn.configure(image = _PauseImg, command = pause_music)
    stop_music()
    time.sleep(0.5)
    if Mpaused:
        mixer.music.unpause()
        #StatusBar['text'] = "Resumed" + ' ' + os.path.basename(file_data[0]) + ' ...'
        Mpaused = FALSE
    else:
        try:
                    mixer.music.load(filename)
                    #text['text'] = "Playing " + os.path.basename(file_data[0]) + ' ...'
                    song_playing = TRUE
                    mixer.music.play()

                    #StatusBar['text'] = "Playing" + ' ' + os.path.basename(file_data[0]) + ' ...'
        except:
            messagebox.showerror('ERROR', 'file Correpted.')

def stop_music():
    global Stopped
    mixer.music.stop()
    #Stopped = TRUE
    mins,secs = 0,0
    #currtime['text'] = "00:00"
    #StatusBar['text'] = "Music has been Stoped."

def Song_details(filename):
    global file_data
    file_data = os.path.splitext(filename)
    if file_data[1] == '.mp3':
        audio = MP3(filename)
        total_length = audio.info.length
    else:
        length = mixer.Sound(filename)
        total_length = length.get_length()
    mins,secs = divmod(total_length,60)
    mins = round(mins)
    secs = round(secs)
    timeformat = '{:02d}:{:02d}'.format(mins,secs)
    totaltime['text'] = timeformat
    t1 = threading.Thread(target = start_count, args = (total_length,))
    t1.start()


def start_count(total_time):
    total_time=round(total_time)
    global Mpaused
    global mins
    global secs
    mins,secs = 0,0

    current_time=0
    while current_time<=total_time:
       # time.sleep(1)
        if Mpaused:
            continue
        else:
            mins,secs = divmod(current_time,60)
            mins = round(mins)
            secs = round(secs)
            timeformat1 = '{:02d}:{:02d}'.format(mins,secs)
            currtime['text'] = timeformat1
            time.sleep(1)
            current_time+=1

    #PlayBtn.configure(image = _PlayImg, command = play_music)


def previos_music():
    mixer.music.stop()
    try:
        if(pw.selected_song_index<=len(pw.song_list)):
            song_index = pw.selected_song_index
            pw.selected_song_index = pw.selected_song_index + 1
            song_index = song_index + 1
            song_name = pw.Queue[song_index]
            mynextsongpath = pw.mypath + "/" + song_name
    #pygame.mixer.music.load(pw.song_list[songindex+1])
            src = mynextsongpath
            target = "D:/Project/SpikePlayer/cache"
            cache_songs = os.listdir(target)
            os.remove(target + "/" + str(cache_songs[0]))
            cache_songs.pop()
            shutil.copy(src, target)
            cache_songs.append(song_name)
            import casper_functions as cf
            cf.play_music(mynextsongpath)
        else:
            messagebox.showerror("ERROR","You have reached end of the playlist")
    except:
        messagebox.showerror("ERROR","No more song to play")


def next_music():
    mixer.music.stop()
    try:
        if(pw.selected_song_index<=len(pw.song_list)):
            song_index = pw.selected_song_index
            pw.selected_song_index = pw.selected_song_index - 1
            song_index = song_index - 1
            song_name = pw.Queue[song_index]
            mynextsongpath = pw.mypath + "/" + song_name
    #pygame.mixer.music.load(pw.song_list[songindex+1])
            src = mynextsongpath
            target = "D:/Project/SpikePlayer/cache"
            cache_songs = os.listdir(target)
            os.remove(target + "/" + str(cache_songs[0]))
            cache_songs.pop()
            shutil.copy(src, target)
            cache_songs.append(song_name)
            import casper_functions as cf
            cf.play_music(mynextsongpath)
        else:
            messagebox.showerror("ERROR","You have reached end of the playlist")
    except:
        messagebox.showerror("ERROR","No more song to play")


def Open_Settings():
    pass
def AboutUs():
    messagebox.showinfo('About developer', 'This software was developed by Fairoz Ahmed Shaik.')
def User_Manual():
    pass


def Clear_Cache():
    pass

