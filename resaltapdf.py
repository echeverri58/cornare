import fitz
import os

# Crea una lista de palabras a buscar
palabras = ["San Luis", "energía", "pch", "PCH", "hidroeléctrica"]

os.mkdir('separados')
path= r"/content/PDF/"
path2 = r"/content/separados"
files = os.listdir(path)

for file in files:
    doc=fitz.open(path+'/'+file)
    for page in doc:
        text = page.get_text()
        # Busca cada palabra en la lista en el texto de la página
        for palabra in palabras:
            result = text.find(palabra)
            if result != -1:
                doc.save(path2+'/'+file)
                print(file)
                pass