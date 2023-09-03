# url = 'http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'
# print(url)

url = 'bytebank.com/cambio?moedaOrigem=real'
print(url)

# url_base = url[0:19]
# print(url_base)

# url_parametro = url[20:36]
# print(url_parametro)

indice_interrogrcao = url.find('?')
url_base = url[:indice_interrogrcao]
# print(url_base)

url_parametro = url[indice_interrogrcao+1:]
print(url_parametro)