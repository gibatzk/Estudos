url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
print(url)

indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
print(url_base)

url_parametros = url[indice_interrogacao+1:]
print(url_parametros)