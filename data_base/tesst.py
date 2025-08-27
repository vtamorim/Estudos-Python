import requests

api_key = "67f2150649fc4ef8873145241252308"
cidade = input("Nome: da cidade:")
url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={cidade}"

resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    print("Temperatura:", dados["current"]["temp_c"], "°C")
    print("Condição:", dados["current"]["condition"]["text"])
else:
    print("Erro ao acessar API:", resposta.status_code)
