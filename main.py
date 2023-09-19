import requests
from bs4 import BeautifulSoup

# URL do perfil do Smite Guru
url = "https://smite.guru/profile/710732108-Auzysss"

# Enviar uma solicitação GET para a página
response = requests.get(url)

# Verificar se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Analisar o conteúdo da página com BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Encontrar as divs que contêm as informações de KDA e Kills
    kda_div = soup.find("div", class_="tsw__grid__title", text="KDA")
    kills_div = soup.find("div", class_="tsw__grid__title", text="Kills")
    
    # Extrair os valores de KDA e Kills
    if kda_div and kills_div:
        kda = kda_div.find_next("div", class_="tsw__grid__stat").text
        kills = kills_div.find_next("div", class_="tsw__grid__stat").text
        print(f"KDA: {kda}")
        print(f"Kills: {kills}")
    else:
        print("Não foi possível encontrar todas as informações desejadas.")
else:
    print("Falha ao acessar a página.")
