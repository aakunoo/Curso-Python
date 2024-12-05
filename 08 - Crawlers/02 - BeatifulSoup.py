import requests  # modulo para hacer peticiones a la web
from bs4 import BeautifulSoup

miDoc = """

        <html>
            <body>
                <h1> Hola Mundo </h1>
                <p> Este es un párrafo </p>
                <p> Este es otro párrafo </p>
                <a> Es un vinculo </a>
        
            </body>
        </hmtl>
"""

docfinal = BeautifulSoup(miDoc, "html.parser")  # html.parser es fijo.

for i in docfinal.find_all("p"):
    print(i.text)


# Volver aqui cuando mire HTML y CSS
