import nltk
from nltk.chat.util import Chat, reflections
import requests


nltk.download('punkt')

pares = [
    (
        r"oi|olá|e aí|salve|opa|mano|ow|eae|ei|chat",
        ["Oi, tudo bem?", "Olá, como posso ajudar?", "E aí, o que você precisa?"]
    ),
    (
        r"tudo bem|tudo certo|tranquilo|de boa|suave",
        ["Que bom saber disso!", "Fico feliz em ouvir isso!", "Ótimo!"]
    ),
    (
        r"qual é o seu nome?|como você se chama?|quem é você?",
        ["Eu sou um chatbot, mas você pode me chamar de Chatfloyd!", "Sou um assistente virtual."]
    ),
    (
        r"o que você pode fazer?|quais são suas funções?|o que você sabe fazer?",
        ["Posso apenas responder perguntas básicas, por enquanto.","não muita coisa, kkkkk"]
    ),
    (
        r"adeus|tchau|falou|até mais",
        ["Até logo!", "Tchau! Volte sempre!", "Até a próxima!"]
    ),

]


def chatbot():
    print("Olá! Eu sou o Chatfloyd. Como posso ajudá-lo?")
    chat = Chat(pares, reflections)

    while True:
        user_input = input("Você: ")
        response = chat.respond(user_input)

       
        if not response:
            response = "Desculpe, não entendi. Pode tentar perguntar de outra forma?"
        
        print(f"ChatBot: {response}")
        
        # Verifica se o usuário deseja encerrar a conversa
        if "adeus" in user_input.lower() or "tchau" in user_input.lower():
            print("ChatBot: Até logo! Tenha um ótimo dia!")
            break
if __name__ == "__main__":
    chatbot()
