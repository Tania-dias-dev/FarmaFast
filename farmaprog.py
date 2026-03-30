import customtkinter as ctk
from PIL import Image
import json

with open("moleculas.json", "r", encoding="utf-8") as f:
    dados = json.load(f)


def calcular():
    dci_final = dci.get().lower()
    peso_texto = peso_valor.get().strip()

    if peso_texto == "":
        posologia_label.configure(text="Por favor introduza o peso.")
        return

    if dci_final == "":
        posologia_label.configure(text="Por favor introduza o dci.")
        return

    try:
        peso = float(peso_texto)
    except:
        posologia_label.configure(text="Peso inválido")
        return

    if peso<0:
        posologia_label.configure(text="Por favor introduza um peso válido.")
        return

    if dci_final in dados:

        m = dados[dci_final]
        dose_diaria = m["dose_diaria"]
        mg = m["mg"]
        ml = m["ml"]
        tomas = m["tomas"]

        doseMaxima_peso = dose_diaria * peso

        resultado_converter = (doseMaxima_peso * ml) / mg

        final_posologia = resultado_converter / tomas

        #resultado_posologia = round(final_posologia, 2)

        posologia_label.configure(text=f"Posologia: {final_posologia:.2f} ml por toma ({tomas} x/dia)")

    else:
        posologia_label.configure(text="Dci não encontrado, por favor introduza um DCI válido")


ctk.set_appearance_mode("dark")

app = ctk.CTk()  # corrigido aqui
app.geometry("500x600")
app.resizable(False, False)
app.title("FarmaFast")
app.configure(background="#1a1a1a")

imagem = ctk.CTkImage(light_image=Image.open("fundo.jpeg"),
                      dark_image=Image.open("fundo.jpeg"),
                      size=(500, 600))

# criar label como fundo
fundo = ctk.CTkLabel(app, image=imagem, text="")
fundo.place(relx=0.5, rely=0.5, anchor="center")


#interior

frame=ctk.CTkFrame(app, corner_radius=20, fg_color="#2b2b2b")


frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.8, relheight=0.9)
frame.grid_columnconfigure(0, weight=1)

titulo= ctk.CTkLabel(frame, text="Calculadora de Dose", font=("Arial",30))
titulo.grid(row=0, column=0, pady=20, sticky="n")


dci_etiqueta=ctk.CTkLabel(frame, text="Introduza DCI:", font=("Arial",20))
dci_etiqueta.grid(row=1, column=0, sticky="w", pady=(20, 5), padx=10)

dci= ctk.CTkEntry(frame, placeholder_text="DCI")
dci.grid(row=2, column=0, sticky="ew", pady=(0, 20), padx=10)

peso_etiqueta = ctk.CTkLabel(frame, text="Peso (kg):", font=("Arial", 20))
peso_etiqueta.grid(row=3, column=0, sticky="w", padx=10, pady=(10, 5))

peso_valor = ctk.CTkEntry(frame, placeholder_text="Peso")
peso_valor.grid(row=4, column=0, sticky="ew", padx=10, pady=(0, 15))

botao_calcular= ctk.CTkButton(frame,text="Calcular", command=calcular)
botao_calcular.grid(row=5, column=0, padx=10, pady=10)


linha = ctk.CTkFrame(frame, height=2, fg_color="gray")
linha.grid(row=6, column=0, sticky="ew", padx=10, pady=10)


resultado_label=ctk.CTkLabel(frame, text="Posologia: ", font=("Arial", 20))
resultado_label.grid(row=10, column=0, sticky="w", padx=10, pady=10 )

posologia_label=ctk.CTkLabel(frame, text="", font=("Arial", 15), fg_color="gray", corner_radius=10)
posologia_label.grid(row=12, column=0, sticky="w", padx=10, pady=10)

















app.mainloop()
