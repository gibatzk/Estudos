import xmltodict
import os 
import json

def pegar_infos(nome_arquivo):
    print(f"Pegou as informações {nome_arquivo}")
    with open (f'nfs/{nome_arquivo}', "rb") as arquivo_xml:
        dic_arquivo = xmltodict.parse(arquivo_xml)
        print(json.dumps(dic_arquivo, indent=4))

lista_arquivos = os.listdir("nfs")

for arquivo in lista_arquivos:
    pegar_infos(arquivo)
    break

