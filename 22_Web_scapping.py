# WEB SCRAPPING

# Internet esta lleno de datos que pueden ser utilizados para diferentes propositos. Para recolectar
# estos datos, necesitamos saber como obtenerlos.

# Web scrapping es el proceso de extraer y recolectar datos desde sitios web y almacenarlos
# localmente o en un servidor.

# En esta seccion usaremos los paquetes beautifulsoup y requests.
# Para obtener datos de sitios web, es necesario conocimiento basico de HTML y CSS. Nuestro objetivo
# son los tags (etiquetas) HTML, clases, y/o ids. 
import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/ml/datasets.php'

datos = requests.get(url) # Usamos requests para obtener datos de la url
status = datos.status_code
if status != 200: exit() # 200 significa que la request se completo con exito

contenido = datos.content # Obtenemos todo el contenido de la pagina
soup = BeautifulSoup(contenido, 'html.parser')
print(soup.title) # <title> El titulo de la pagina </title>
print(soup.title.get_text()) # El titulo sin tags
print(soup.body) # Todo el contenido de la pagina

tablas = soup.find_all('table', {'cellpadding':'3'}) # Aqui estamos enfocando la tabla con un padding de atributo 3
# Podemos seleccionar utilizando id, clase o tag HTML
tabla = tablas[0]
for td in tabla.find('tr').find_all('td'):
    print(td.text)
    
#1. Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').
url = 'http://www.bu.edu/president/boston-university-facts-stats/'

datos = requests.get(url)
if datos.status_code != 200: exit()
contenido = datos.content

sopita = BeautifulSoup(contenido, 'html.parser')

#TO BE CONTINUED