import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import threading
from pygame import mixer
from mutagen.mp3 import MP3
import os
import easygui
import time
import playlist_window as pw
import Main as main
#from PIL import ImageTk,Image

def redirect(path):
    main.play_music(path)
