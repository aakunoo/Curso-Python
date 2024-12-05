import requests  # modulo para hacer peticiones a la web

miRequest = requests.get("https://www.movistar.es")

print(miRequest.status_code)  # Devuelve 200 si la petición ha sido correcta
# Devuelve los headers de la petición en un diccionario
print(miRequest.headers)
print(miRequest.text)  # Devuelve el contenido de la página web
