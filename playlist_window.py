import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import threading
from pygame import mixer
from mutagen.mp3 import MP3
import os,shutil
import easygui
import time


dir_songs_path = ""
windowopened = FALSE

target = "D:/Project/SpikePlayer/cache"
cache_songs = os.listdir(target)


def onselect(event):
    w = event.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    info = find_info(value)
    listSelection.delete(0, END)
    listSelection.insert(END, "Node ID: " + info[0])
    listSelection.insert(END, "Owner/Description: " + info[1])
    listSelection.insert(END, "Last Latitude: " + info[2])
    listSelection.insert(END, "Last Longitude: " + info[3])
    listSelection.insert(END, "Last Longitude: " + info[4])
    listSelection.insert(END, "Last Longitude: " + info[5])
    listSelection.insert(END, "Last Longitude: " + info[6])

file_list=[]
def Open_Playlist():
    global lb
    global listNodes
    global listSelection
    global playlist
    global StatusBar
    global file_list
    global window
    global songs_list

    path = "D:/Project/SpikePlayer/PlaylistDirs/"

    mapNodes = "http://ukhas.net/api/mapNodes"
    nodeData = "http://ukhas.net/api/nodeData"
    current_id = 0

    window = Tk() # create window
    windowopened = TRUE
    window.configure(bg='skyblue')
    window.title("Casper Playlist")
    window.geometry("650x400")

    lbl1 = Label(window, text="Playlists", fg='skyblue', font=("Times", 12, "bold"), bg = "white")
    lbl2 = Label(window, text="Playlist Songs", fg='skyblue', font=("Times", 12,"bold"), bg= "white")


    lbl1.grid(row=0, column=0, sticky=W)
    lbl2.grid(row=0, column=1, sticky=W)

    refresh_Song = ttk.Button(window, text = "Refersh", command = RefreshList)
    refresh_Song.grid(row=0, column=1, sticky=E)

    frm = Frame(window)
    frm.grid(row=1, column=0, sticky=W+N+S)
    window.rowconfigure(1, weight=1)
    window.columnconfigure(1, weight=1)

    scrollbar = Scrollbar(frm, orient="vertical")
    scrollbar.pack(side=RIGHT, fill=Y)

    listNodes = Listbox(frm, width=20, yscrollcommand=scrollbar.set, font=("Helvetica", 12), bg = "skyblue")
    listNodes.pack(expand=True, fill=Y)

    scrollbar.config(command=listNodes.yview)


    CreatePlaylistBtn = ttk.Button(window, text = "+", command = createlist)
    CreatePlaylistBtn.grid(row=2, column=0, sticky=W, padx = 2)

    #sub = PhotoImage(file = "images/delete_selected.gif")
    DeletePlaylistBtn = ttk.Button(window, text = "-", command = deletelist)
    DeletePlaylistBtn.grid(row=2, column=0, sticky=W, padx = 79)

    #OpenPlaylistBtn = ttk.Button(window, text = "Open", command = Open_on_click)
    #OpenPlaylistBtn.grid(row=2, column=0, sticky=W, padx = 22)

    listSelection = Listbox(window, width=45, height=18, font=("Helvetica", 12), bg = "skyblue")
    listSelection.grid(row=1, column=1, sticky=N+S+E+W, padx = 0)

    Add_Song = ttk.Button(window, text = "Add Songs", command = adding_song)
    Add_Song.grid(row=2, column=1, sticky=W, padx = 10)

    #sub = PhotoImage(file = "images/delete_selected.gif")
    Delete_Song = ttk.Button(window, text = "Delete", command = deleting_song)
    Delete_Song.grid(row=2, column=1, sticky=W, padx = 89)


    #refresh = PhotoImage(file = "images/delete_selected.gif")
    play_Song = ttk.Button(window, text = "Play", command = Play_song)
    play_Song.grid(row=2, column=1, sticky=W, padx = 169)

    #Open = PhotoImage(file = "images/delete_selected.gif")
#OpenPlaylistBtn = ttk.Button(window, text = "Open", command = cp.Open_on_click)
#OpenPlaylistBtn.grid(row=2, column=4, sticky=E+W+N)


    path = "D:/Project/SpikePlayer/PlaylistDirs"
    index=0
    file_list = os.listdir(path)
    for item in file_list:
        if len(file_list)!=0:
            listNodes.insert(index,item)
            listNodes.itemconfig(index, fg="blue")
            listNodes.bind('<Double-1>', Open_on_click)
            index+=1


    dir_songs_path = "D:/Project/SpikePlayer/PlaylistDirs/" + file_list[0]
    count=0
    songs_list = os.listdir(dir_songs_path)
    #Queue = songs_list
    for song in enumerate(songs_list):
        if len(songs_list)!=0:
            listSelection.insert(count,song)
            listSelection.itemconfig(count, fg="blue")
            count+=1

    window.mainloop()






def Close():
    window.destroy()
    windowopened = FALSE
mypath = ""

def Open_on_click(*args):
    #print(a)
    global mypath
    global song_list
    global Queue
    song_list=[]
    Queue=[]
    selected_open = listNodes.curselection()
    selected_open = int(selected_open[0])
    selectpath = file_list[selected_open]
    mypath = "D:/Project/SpikePlayer/PlaylistDirs/" + selectpath
    songindex=0
    song_list.clear()
    listSelection.delete(0, END)
    song_list = os.listdir(mypath)
    Queue.clear()
    Queue = song_list
    if len(song_list)!=0:
        for item in enumerate(song_list):
            listSelection.insert(songindex,item)
            listSelection.itemconfig(songindex, fg="blue")
            songindex+=1
    else:
        listSelection.insert(songindex,"No songs! Please add here")
        listSelection.itemconfig(songindex, fg="blue")

def adding_song():
   # print(mypath)
    if(len(mypath)!=None):
        opendialog = filedialog.askopenfilename(initialdir = "D:/", title = "Select the song", filetypes = (("MP3 files", "*.mp3"),("All files","*.*")))
        src = opendialog
        target = mypath
    else:
        tkinter.messagebox.showerror("Error","Please select the playlist to add song")
    if(opendialog):
        try:
            #print(target)
            shutil.copy(src, target)
            tkinter.messagebox.showinfo("Song copied","Your song has been copied to selected playlist, Please refresh to update")
        except:
            tkinter.messagebox.showerror("Error","Please select the playlist to add song")
    else:
        pass




def RefreshList():
    window.destroy()
    Open_Playlist()




def Play_song():
    global mysongpath
    global selected_song_index
    global cache_songs
    selected_song1 = listSelection.curselection()
    selected_song_index = int(selected_song1[0])
    try:
        selected_song1 = song_list[selected_song_index]
        mysongpath=mypath +"/"+ str(selected_song1)
        src = mysongpath
        if(len(cache_songs)==0):
            shutil.copy(src, target)
            cache_songs.append(selected_song1)
        else:
            mixer.music.stop()
            time.sleep(0.5)
            import casper_functions as cf
            cf.play_music(mysongpath)
            os.remove(target + "/" + str(cache_songs[0]))
            cache_songs.pop()
            shutil.copy(src, target)
            cache_songs.append(selected_song1)

    except:
        messagebox.showerror("ERROR","Please select playlist before playing the song")

    #target = "D:/Project/SpikePlayer/cache"
    #cache_songs = os.listdir(target)



def createlist():
    global position
    path = "D:/Project/SpikePlayer/PlaylistDirs/ "
    userinput = easygui.enterbox("Create Playlist Name:")
    try:
        os.mkdir(path + userinput)

        tkinter.messagebox.showinfo("Refersh","Please refresh the window")
    except OSError:
        tkinter.messagebox.error("Error Occured!", "Unble to create the playlist, try again")
    else:
        position = 0
        listNodes.insert(position,userinput)
        listNodes.itemconfig(position, fg="blue")
        position+=1
        file_list.append(userinput)



def deletelist():
    global selected_dir
    path = "D:/Project/SpikePlayer/PlaylistDirs"
    if len(file_list)!=0:
        selected_dir = listNodes.curselection()
        selected_dir = int(selected_dir[0])
        deleteit = file_list[selected_dir]
        try:
            if tkinter.messagebox.askokcancel("Delete", "Do you really want to delete?"):
                file_list.pop(selected_dir)
                listNodes.delete(selected_dir)
                print("not deleted")
                shutil.rmtree(path+"/"+deleteit)
                print("deleted")
                tkinter.messagebox.showinfo("Successfull", "Deleted Sucessfully! Please refresh the window")
            else:
                pass
        except OSError:
            tkinter.messagebox.showerror("Error Occured!", "Unble to delete the playlist, try again")
    else:
        tkinter.messagebox.showerror('Empty!', 'Playlist is Empty')


def deleting_song():
    if len(song_list)!=0:
        selected_song = listSelection.curselection()
        selected_song = int(selected_song[0])
        print(song_list)
        deleteit = song_list[selected_song]
        try:
            if tkinter.messagebox.askokcancel("Delete", "Do you really want to delete?"):
                mixer.music.stop()
                try:
                    if(deleteit==cache_songs[0]):
                        os.remove(target + "/" + cache_songs[0])
                        cache_songs.pop()
                except:
                    song_list.pop(selected_song)
                    listSelection.delete(selected_song)
                    os.remove(mypath + "/" + deleteit)
                    tkinter.messagebox.showinfo("Successfull", "Deleted Sucessfully! Please refresh the window")
                else:
                    song_list.pop(selected_song)
                    listSelection.delete(selected_song)
                    os.remove(mypath + "/" + deleteit)
                    tkinter.messagebox.showinfo("Successfull", "Deleted Sucessfully! Please refresh the window")
            else:
                pass
        except OSError:
            tkinter.messagebox.showerror("Error Occured!", "Unble to delete the song, try again")
    else:
        tkinter.messagebox.showerror('Empty!', 'Please select the song to delete')



