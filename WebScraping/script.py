import re
import requests


PATRON_TELEFONO = r'itemprop="telephone">[0-9]*'

# Genera una lista de los numeros de telefono y lo envia de vuelkta para concatenarlo en la lista final


def concatenacion_datos(telefonos):
    lista_telefonos = ''
    for telefono in telefonos:
        telefono = telefono.replace('itemprop="telephone">', '')
        lista_telefonos += telefono + "\n"
    return lista_telefonos


def obtencion_de_datos():
    # La url es una busqueda sencilla de Páginas amarillas
    sitio_web = "https://www.paginasamarillas.es/search/all-ac/all-ma/all-pr/all-is/all-ci/all-ba/all-pu/all-nc/1?what=casa+pepe&aprob=0.0&nprob=1.0"
    numeros_telefono = ''
    pagina_nula = False
    pagina = 1
    while not pagina_nula:
        # Reemplaza la parte que le idica a la web en que pagina de la paginación esta por la pagina que estamos comprobando actualmente. Esta hecho de tal manera que si estamos en la pagina numero 1 no sustituya nada
        sitio_web = sitio_web.replace(
            "/" + str(pagina-1) + "?", "/" + str(pagina) + "?")
        resultado = requests.get(sitio_web)
        # Comprobamos que la pagina que estamos visitando tenga datos dentro. Si no tiene se acaba el while y muestra los datos. Si tiene se obtienen y se continuea a la funcion de concatenacios
        if 'Lo sentimos pero no hemos encontrado lo que estabas buscando.' in str(resultado.text):
            pagina_nula = True
        else:
            telefonos = list(
                set(re.findall(PATRON_TELEFONO, str(resultado.text))))
            numeros_telefono += concatenacion_datos(telefonos)
            pagina += 1
    print(numeros_telefono)


obtencion_de_datos()
