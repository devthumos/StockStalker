from tkinter import *
from tkinter.font import *
from tkinter import ttk
from src.MySQL.registro import RegistroMySQL
from src.Web_Scraping.statusinvest import Webscrapper


class WindowCarteira():


    def __init__(cls):
        cls.object_registro = RegistroMySQL()

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
        cod_entry = Entry(space_frm, width=30, textvariable=cls.codvar)
        cod_entry.grid(row=0, column=1, sticky=(W))
        # Button "rgst_btn" e Legendas, não vou fazer as legendas agora
        rgst_btn = Button(space_frm, text="Registrar", bg="#58636E", fg="white", command=cls.registrar) # TESTE
        rgst_btn.grid(row=1, column=1, sticky=(N, S, W, E))

        # Frame Combobox "cbx_frn" que conterá o combobox e os scrollbars
        # Frame Combobox "cbx_frn"
        cbx_frn = Frame(mainframe)
        cbx_frn.pack(fill=BOTH)
        cbx_frn.columnconfigure(0, weight=1)
        cbx_frn.rowconfigure(0, weight=1)
        # Combobox, POR ENQUANTO VAI SER COM LIST
        cls.cbx = Listbox(cbx_frn)
        # Scrollbar Vertical e Scrollbar Horizontal
        scrl_vrtcl = Scrollbar(cbx_frn, orient=VERTICAL, command=cls.cbx.yview)
        scrl_hrntl = Scrollbar(cbx_frn, orient=HORIZONTAL, command=cls.cbx.xview)
        scrl_vrtcl.pack(side=RIGHT, fill=Y)
        scrl_hrntl.pack(side=BOTTOM, fill=X)
        # Configurando os Scollbars na Combobox
        cls.cbx.configure(yscrollcommand=scrl_vrtcl.set)
        cls.cbx.configure(xscrollcommand=scrl_hrntl.set)
        cls.cbx.pack(fill=BOTH, expand=True)

        # Pré adicionando todos os elementos do banco de dados na listbox
        # VAMO VER
        registros = cls.object_registro.list_elements()
        for i in registros:
            str_statement = f"CÓDIGO:{i[0]} | TIPO:{i[1]} | {i[6]}:{i[2]} | {i[7]}:{i[3]} | {i[8]}:{i[4]} | {i[9]}:{i[5]}"
            cls.cbx.insert(END, str_statement)

        # POLIMENTOS
        # Espaçamento dentro do frame "space_frm" que é child do frame "rgst_cod"
        for child in space_frm.winfo_children():
            child.grid_configure(padx=5)
            """# Espaçamento dentro do frame comboxox "cbx_frn"
        for child in cbx_frn.winfo_children():
            child.pack_configure(pady=10, padx=5)"""

        # Startando o Loopping
        wndcarteira.mainloop()


    def into_wbscrapper(cls):
        wb = Webscrapper()
        indicadores = wb.main(cls.codvar.get())
        msg = f"CÓDIGO:{cls.codvar.get()} | TIPO:{indicadores[1]} | {indicadores[0][0][0]}:{indicadores[0][0][1]} | {indicadores[0][1][0]}:{indicadores[0][1][1]} | {indicadores[0][2][0]}:{indicadores[0][2][1]} | {indicadores[0][3][0]}:{indicadores[0][3][1]}"
        return indicadores, msg

    # TESTE, EMPRESA DEVE SER COLOCADA A PARTIR DO WEBSCRAPPER
    def registrar(cls, *args):
        stt = cls.into_wbscrapper()
        if cls.object_registro.registrar_registros(cls.codvar.get(), stt[0]) != False:
            cls.cbx.insert(0, stt[1])
