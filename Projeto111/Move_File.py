import os
import shutil

from_dir = "C:/Program Files"
to_dir = "C:/Users/Leandro Oliveira/Desktop/Arquivos_Documentos"

list_of_files = os.listdir(from_dir)
print(list_of_files)

# Cria o arquivo de texto na pasta "Arquivos_Documentos"
text_file_path = os.path.join(to_dir, "lista.txt")
with open(text_file_path, "w") as file:
    file.write("\n".join(list_of_files))

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    # print(name, extension)
