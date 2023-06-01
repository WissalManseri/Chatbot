from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Création du chatbot
chatbot = ChatBot('My Chatbot')

# Entraînement avec des exemples personnalisés
trainer = ListTrainer(chatbot)
trainer.train([
    "Bonjour",
    "Bonjour, comment ça va?",
    "Ça va bien, merci. Et toi?",
    "Je vais bien, merci.",
    "Qu'est-ce que tu fais?",
    "Je suis un chatbot, je peux répondre à des questions et avoir des conversations.",
    "Quel est ton nom?",
    "Je m'appelle My Chatbot.",
])

# Entraînement avec des corpus de données prédéfinis en anglais
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train("chatterbot.corpus.english")

# Fonction pour obtenir une réponse du chatbot
def get_bot_response(user_input):
    bot_response = chatbot.get_response(user_input)
    return bot_response

# Boucle principale de conversation avec l'utilisateur
print('Bonjour, je suis My Chatbot. Comment puis-je vous aider aujourd\'hui?')
while True:
    user_input = input('You: ')
    if user_input.lower() == 'quit':
        print('Au revoir!')
        break
    bot_response = get_bot_response(user_input)
    print('My Chatbot:', bot_response)
