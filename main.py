import tkinter as tk
import subprocess
import sys
import os

def executar_cadastro():
    # Executa o cadastro.py
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cadastro.py')
    subprocess.run([sys.executable, script_path])

def executar_login():
    # Executa o login.py
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'login.py')
    subprocess.run([sys.executable, script_path])

def sair():
    root.destroy()

# Cria a interface gráfica
root = tk.Tk()
root.title("Reconhecimento Facial")

label_title = tk.Label(root, text="Reconhecimento Facial", font=("Helvetica", 16))
label_title.pack(pady=20)

button_cadastrar = tk.Button(root, text="Cadastrar", width=20, command=executar_cadastro)
button_cadastrar.pack(pady=10)

button_login = tk.Button(root, text="Login", width=20, command=executar_login)
button_login.pack(pady=10)

button_sair = tk.Button(root, text="Sair", width=20, command=sair)
button_sair.pack(pady=10)

root.mainloop()
