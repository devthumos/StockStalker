from tkinter import *
from tkinter.font import *
from tkinter import ttk

# Styles Login
    # Style Frame Label Login
styl_frmlgn = ttk.Style()
styl_frmlgn.configure("frmlgn.TFrame", background="#58636E")
# Se n funfar, taca o background dentro
styl_frmlgn.configure("llogin_top.TLabel", foreground="white", font=Font())
