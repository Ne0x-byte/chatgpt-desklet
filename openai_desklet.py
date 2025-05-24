import os
import tkinter as tk
from tkinter import scrolledtext
from openai import OpenAI

# Puedes reemplazar esta línea si prefieres poner la clave directo
api_key = os.getenv("OPENAI_API_KEY") or "AQUÍ_TU_CLAVE_API_SI_NO_USAS_VARIABLE"

client = OpenAI(api_key=api_key)

def enviar():
    entrada = entrada_usuario.get()
    entrada_usuario.delete(0, tk.END)
    chat.insert(tk.END, "Tú: " + entrada + "\n", "user")

    try:
        respuesta = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Puedes usar gpt-4 si tu cuenta lo permite
            messages=[
                {"role": "user", "content": entrada}
            ]
        )
        contenido = respuesta.choices[0].message.content
        chat.insert(tk.END, "AI: " + contenido + "\n\n", "ai")
        chat.yview(tk.END)
    except Exception as e:
        chat.insert(tk.END, "Error: " + str(e) + "\n", "error")
        chat.yview(tk.END)

# Interfaz gráfica con tkinter
ventana = tk.Tk()
ventana.title("OpenAI Desklet")

chat = scrolledtext.ScrolledText(ventana, width=80, height=20, wrap=tk.WORD)
chat.tag_config("user", foreground="blue")
chat.tag_config("ai", foreground="green")
chat.tag_config("error", foreground="red")
chat.pack(padx=10, pady=10)

entrada_usuario = tk.Entry(ventana, width=80)
entrada_usuario.pack(padx=10, pady=5)
entrada_usuario.bind("<Return>", lambda event: enviar())

boton_enviar = tk.Button(ventana, text="Enviar", command=enviar)
boton_enviar.pack(pady=5)

ventana.mainloop()
