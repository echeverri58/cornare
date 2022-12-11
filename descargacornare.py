def descargar_pdf(url):
    import requests # Agregamos la importación de requests aquí
    # Realizamos la petición a la página web
    r = requests.get(url) 
    soup = BeautifulSoup(r.content, "html.parser")
    dom = etree.HTML(str(soup))
    
    # Extraemos la url del mes actual de los editos de CORNARE
    url = dom.xpath('//*[@id="f935fbc7ba2b28a6f"]/div/ul/li[1]/a/@href')
    url2 = str(url)
    url3 = url2.strip("['/']")
    
    # Realizamos la petición a la url del mes actual
    response = requests.get(url3) 
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Buscamos todos los enlaces en la página web
    links = soup.find_all('a')
    
    # Descargamos todos los enlaces que sean PDF
    i = 0
    for link in links:
        if ('.pdf' in link.get('href', [])):
            i += 1
            print("Descargando archivo: ", i)
            response = requests.get(link.get('href'))
            pdf = open("/content/PDF/pdf"+str(i)+".pdf", 'wb') #le decimos que los pdf descargados los guarde en la carpeta PDF
            pdf.write(response.content)
            pdf.close()
            print("Archivo ", i, " descargado")
    print("Se han descargado todos los PDF")
