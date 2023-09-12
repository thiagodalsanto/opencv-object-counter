import os
import tkinter as tk

def run_ball_identifier():
    os.chdir(os.path.join(script_dir, 'ball_identifier'))
    os.system('python main.py')
    os.chdir(script_dir)

def run_chicken_counter():
    os.chdir(os.path.join(script_dir, 'chicken_counter'))
    os.system('python main.py')
    os.chdir(script_dir)

def on_exit_click():
    root.quit()

# Obtém o diretório atual do script
script_dir = os.path.dirname(os.path.abspath(__file__))

root = tk.Tk()
root.title("Escolha uma aplicação")

# Largura fixa da janela
window_width = 450
root.geometry(f"{window_width}x165")

# Define um estilo para os botões
button_font = ('Arial', 14)
button_bg = '#007acc'  # Cor de fundo
button_fg = 'white'    # Cor do texto

label = tk.Label(root, text="Qual das duas aplicações deseja rodar?", font=('Arial', 16))
label.pack()

button_ball_identifier = tk.Button(root, text="Ball Identifier", command=run_ball_identifier, font=button_font, bg=button_bg, fg=button_fg, width=window_width, wraplength=150, justify='center')
button_ball_identifier.pack()

button_chicken_counter = tk.Button(root, text="Chicken Counter", command=run_chicken_counter, font=button_font, bg=button_bg, fg=button_fg, width=window_width, wraplength=150, justify='center')
button_chicken_counter.pack()

button_exit = tk.Button(root, text="Sair", command=on_exit_click, font=button_font, bg=button_bg, fg=button_fg, width=window_width)
button_exit.pack()

root.mainloop()
