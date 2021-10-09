from tkinter import *
from tkinter.font import *
from tkinter import ttk
from src.MySQL.registro import RegistroMySQL
from src.Web_Scraping.statusinvest import Webscrapper


class WindowCarteira:
    def __init__(cls, user):
        cls.object_registro = RegistroMySQL()
        cls.user = user
        wndcarteira = Tk()
        wndcarteira.title("ActionStalker")
        wndcarteira.geometry("925x300+100+100")

        # Frame principal "mainframe"
        mainframe = ttk.Frame(wndcarteira)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        wndcarteira.columnconfigure(0, weight=1)
        wndcarteira.rowconfigure(0, weight=1)

        # Frame "lbl_lgin_frm" que conterá label e button, label "LOGIN", button "Config"
        # Frame lbl_lgin_frm
        lbl_lgin_frm = Frame(mainframe, bg="black")
        lbl_lgin_frm.pack(fill=X)
        lbl_lgin_frm.columnconfigure(0, weight=1)
        lbl_lgin_frm.rowconfigure(0, weight=1)
        # Label "CARTEIRA STALKER"
        lbl_log = Label(lbl_lgin_frm, text="CARTEIRA STALKER", background="black", fg="white",
                        font=Font(family="Arial Black", size=20, weight="bold"))
        lbl_log.pack()
        lbl_log.pack_configure()
        # Label "img_sett"
        # lbl_sett = Label(lbl_lgin_frm, text="img_sett", background="black", fg="white",
        #                  font=Font(family="Comic Sans Ms", size=15, weight="bold"))
        # lbl_sett.grid(row=0, column=1, sticky=(E))
        # lbl_sett.grid_configure(padx=5)

        # Frame "rgst_cod" que conterá labels, button, Entry Widgets
        # Frame rgst_cod
        rgst_cod = Frame(mainframe)
        rgst_cod.pack(fill=X)
        rgst_cod.columnconfigure(0, weight=1)
        rgst_cod.rowconfigure(0, weight=1)
        # Frame "space_frm" responsável pelo espaçamento dentro do Frame "rgst_cod"
        space_frm = Frame(rgst_cod)
        space_frm.pack()
        space_frm.pack_configure(padx="0 70")
        # Label text="Código" e Entry "cod_entry"
        cls.codvar = StringVar()
        ttk.Label(space_frm, text="Código", foreground="black",
                  font=Font(family="Arial Black", size=12, weight="bold", underline=True)).grid(row=0, column=0, sticky=(E))
        cod_entry = Entry(space_frm, width=51, textvariable=cls.codvar)
        cod_entry.grid(row=0, column=1, sticky=(W))
        # Button "rgst_btn" e Legendas, não vou fazer as legendas agora
        rgst_btn = Button(space_frm, text="Registrar", bg="black", fg="white", command=cls.registrar,
                          font=Font(family="Arial Black", size=10, weight="normal")) # TESTE
        rgst_btn.grid(row=1, column=1, sticky=(N, S, W, E))

        # $$##@@ MELHOR UTILIZAR tkinter.scrolledtext PARA APARECER AS IMAGENS DAS EMPRESAS
        # Frame Combobox "cbx_frn" que conterá o combobox e os scrollbars
        # Frame Combobox "cbx_frn"
        cbx_frn = Frame(mainframe, padx="10", pady="10")
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
        registros = cls.object_registro.list_elements(user)
        for indicadores in registros:
            if indicadores[1] == "Fundo de Investimento":
                msg = f"CÓDIGO:{indicadores[0]} | TIPO:{indicadores[1]} | RENTABILIDADE(12M):{indicadores[2]} | RENTABILIDADE(24M):{indicadores[3]} | VOLATILIDADE(12M):{indicadores[4]} | ÍNDICE DE SHARPE(6M):{indicadores[5]} | PATRIMÔNIO LÍQUIDO: {indicadores[6]} | PREÇO DA COTA: {indicadores[7]}"
            elif indicadores[1] == "Tesouro":
                msg = f"CÓDIGO:{indicadores[0]} | TIPO:{indicadores[1]} | VALOR UNITÁRIO:{indicadores[2]} | MIN. 52 SEM.:{indicadores[3]} | MÁX. 52 SEM.:{indicadores[4]} | VALORIZAÇÃO(12M):{indicadores[5]}"
            else:
                msg = f"CÓDIGO:{indicadores[0]} | TIPO:{indicadores[1]} | VALOR ATUAL:{indicadores[2]} | MIN. 52 SEM.:{indicadores[3]} | MÁX. 52 SEM.:{indicadores[4]} | DIVIDEND YIELD:{indicadores[5]} | VALORIZAÇÃO (12M):{indicadores[6]}"
            cls.cbx.insert(END, msg)

        # POLIMENTOS
        # Espaçamento dentro do frame "space_frm" que é child do frame "rgst_cod"
        for child in space_frm.winfo_children():
            child.grid_configure(padx=5)
            """# Espaçamento dentro do frame comboxox "cbx_frn"
        for child in cbx_frn.winfo_children():
            child.pack_configure(pady=10, padx=5)"""

        wndcarteira.bind("<Return>", cls.registrar)

        # Startando o Loopping
        wndcarteira.mainloop()

    def into_wbscrapper(cls) -> tuple:
        wb = Webscrapper()
        indicadores = wb.main(cls.codvar.get())

        return indicadores, cls.get_msg(indicadores)

    def get_msg(cls, indicadores: list) -> str:
        if indicadores[1] == "Fundo de Investimento":
            msg = f"CÓDIGO:{cls.codvar.get().replace('-', ' ').title()} | TIPO:{indicadores[1]} | RENTABILIDADE(12M):{indicadores[0][0]} | RENTABILIDADE(24M):{indicadores[0][1]} | VOLATILIDADE(12M):{indicadores[0][2]} | ÍNDICE DE SHARPE(6M):{indicadores[0][3]} | PATRIMÔNIO LÍQUIDO: {indicadores[0][4]} | PREÇO DA COTA: {indicadores[0][5]}"
        elif indicadores[1] == "Tesouro":
            msg = f"CÓDIGO:{cls.codvar.get().replace('-', ' ').title()} | TIPO:{indicadores[1]} | VALOR UNITÁRIO:{indicadores[0][0]} | MIN. 52 SEM.:{indicadores[0][1]} | MÁX. 52 SEM.:{indicadores[0][2]} | VALORIZAÇÃO(12M):{indicadores[0][3]}"
        else:
            msg = f"CÓDIGO:{cls.codvar.get().upper()} | TIPO:{indicadores[1]} | VALOR ATUAL:{indicadores[0][0]} | MIN. 52 SEM.:{indicadores[0][1]} | MÁX. 52 SEM.:{indicadores[0][2]} | DIVIDEND YIELD:{indicadores[0][3]} | VALORIZAÇÃO (12M):{indicadores[0][4]}"

        return msg

    def registrar(cls, *args):
        stt = cls.into_wbscrapper()
        if cls.object_registro.registrar_registros(cls.codvar.get(), stt[0], cls.user) != False:
            cls.cbx.insert(0, stt[1])
        cls.codvar.set("")
