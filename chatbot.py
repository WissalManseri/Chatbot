from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot
chatbot = ChatBot('My Chatbot')

# Train the chatbot using the English corpus
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

# Run the chatbot
while True:
    # Get a user input
    user_input = input('You: ')

    # Get a response from the chatbot
    bot_response = chatbot.get_response(user_input)

    # Print the chatbot response
    print('Bot: ', bot_response)
