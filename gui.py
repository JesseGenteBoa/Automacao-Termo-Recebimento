from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
from tkinter.filedialog import askopenfilename
import geradorFormularios
import clicksign


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"Imagens")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("535x270")
window.configure(bg = "#FFFFFF")
window.title("Automação Termo de Recebimento")


def validarEntrada(P):
    P = P.strip()
    if len(P) > 8 or len(P) < 8:
        pass
    return True


vcmd = (window.register(validarEntrada), '%P')

def selecionarArquivo():
    global caminho_arq
    caminho_arq = askopenfilename(title="Selecione um arquivo Excel")


def gerarPdf():
    data = entry_1.get()
    if caminho_arq == "":
        selecionarArquivo()
    geradorFormularios.gerarFormularios(caminho_arq, data)


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 270,
    width = 535,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    410.0,
    58.0,
    image=image_image_1
)

entry_1 = Entry(
    cursor="xterm",
    bg="#ffffff",
    fg="#000000",
    insertwidth=2,
    relief="sunken",
    highlightthickness=1.3,
    highlightbackground="#000000",
    highlightcolor="#000000",
    font=("Inter", 12 * -1),
    validate="key",
    validatecommand=vcmd
)

entry_1.place(
    x=97.0,
    y=50.0,
    width=163.0,
    height=31.0
)

canvas.create_text(
    47.0,
    57.0,
    anchor="nw",
    text="DATA :",
    fill="#000000",
    font=("Inter", 12 * -1, "bold")
)

button_image_3 = PhotoImage(
    file=relative_to_assets("image_2.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=1,
    highlightthickness=0,
    command=lambda: selecionarArquivo(),
    relief="solid",
    cursor="hand2",
    
)
button_3.place(
    x=41.0,
    y=130.0,
    width=241.0,
    height=98.0
)

button_1 = Button(
    text="Gerar PDFs",
    bg = "#968484",
    borderwidth=1,
    highlightthickness=0,
    command=lambda: gerarPdf(),
    relief="ridge",
    cursor="hand2",
    disabledforeground = "#968484",
    font=("Inter", 10, "bold")
)
button_1.place(
    x=352.0,
    y=125.0,
    width=148.0,
    height=40.0
)

button_2 = Button(
    text="Enviar E-mail",
    bg = "#968484",
    borderwidth=1,
    highlightthickness=0,
    command=lambda: clicksign.enviarEmails(caminho_arq),
    relief="ridge",
    cursor="hand2",
    disabledforeground = "#968484",
    font=("Inter", 10, "bold")
)
button_2.place(
    x=352.0,
    y=195.0,
    width=148.0,
    height=40.0
)
window.resizable(False, False)
window.mainloop()
