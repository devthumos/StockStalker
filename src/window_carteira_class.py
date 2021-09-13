from tkinter import *
from tkinter.font import *
from tkinter import ttk


class Carteira():


    def __init__(cls):
        wndcarteira = Tk()
        wndcarteira.title("ActionStalker")
        wndcarteira.geometry("800x500+100+100")

        # Frame principal "mainframe"
        mainframe = ttk.Frame(wndcarteira)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        wndcarteira.columnconfigure(0, weight=1)
        wndcarteira.rowconfigure(0, weight=1)

        # Frame "lbl_lgin_frm" que conterá label e button, label "LOGIN", button "Config"
            # Frame lbl_lgin_frm
        lbl_lgin_frm = Frame(mainframe, bg="#58636E")
        lbl_lgin_frm.pack(fill=X)
        lbl_lgin_frm.columnconfigure(0, weight=1)
        lbl_lgin_frm.rowconfigure(0, weight=1)
            # Label "CARTEIRA STALKER"
        lbl_log = Label(lbl_lgin_frm, text="CARTEIRA STALKER", background="#58636E", fg="white",
                            font=Font(family="Comic Sans Ms", size=15, weight="bold"))
        lbl_log.grid(row=0, column=0, sticky=(N, S, W, E))
            # Label "img_sett"
        lbl_sett = Label(lbl_lgin_frm, text="img_sett", background="#58636E", fg="white",
                        font=Font(family="Comic Sans Ms", size=15, weight="bold"))
        lbl_sett.grid(row=0, column=1, sticky=(E))
        lbl_sett.grid_configure(padx=5)

        # Frame "rgst_cod" que conterá labels, button, Entry Widgets
            # Frame rgst_cod
        rgst_cod = Frame(mainframe)
        rgst_cod.pack(fill=X)
        rgst_cod.columnconfigure(0, weight=1)
        rgst_cod.rowconfigure(0, weight=1)
            # Frame "space_frm" responsável pelo espaçamento dentro do Frame "rgst_cod"
        space_frm = Frame(rgst_cod)
        space_frm.pack()
            # Label text="Código" e Entry "cod_entry"
        cls.codvar = StringVar()
        ttk.Label(space_frm, text="Código",
                  font=Font(family="Comic Sans Ms", size=10, weight="normal")).grid(row=0, column=0, sticky=(E))
        cod_entry = Entry(space_frm, width=10, textvariable=cls.codvar)
        cod_entry.grid(row=0, column=1, sticky=(W))
            # Label text="Tipo" e Entry "type_entry", É PRA SER UM TOGGLE E NAO UM WIDGET ENTRY
        cls.typevar = StringVar()
        ttk.Label(space_frm, text="Tipo",
                  font=Font(family="Comic Sans Ms", size=10, weight="normal")).grid(row=0, column=2, sticky=(E))
        type_entry = Entry(space_frm, width=10, textvariable=cls.typevar)
        type_entry.grid(row=0, column=3, sticky=(W))
            # Button "rgst_btn" e Legendas, não vou fazer as legendas agora
        rgst_btn = Button(space_frm, text="Registrar", bg="#58636E", fg="white", command=cls.registrar)
        rgst_btn.grid(row=1, column=1, columnspan=3, sticky=(N, S, W, E))

        # Combobox


        # POLIMENTOS
            # Espaçamento dentro do frame space_frm
        for child in space_frm.winfo_children():
            child.grid_configure(padx=5)
        wndcarteira.mainloop()


    def registrar(cls):
        pass