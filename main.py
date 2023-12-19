import os 
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")
print(caminho)

lista_arquivos = os.listdir(caminho)
print(lista_arquivos)