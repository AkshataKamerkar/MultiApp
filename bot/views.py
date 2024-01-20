from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

def home(request):

    return render(request,'home.html')


# ChatBot config
bot = ChatBot('bot',read_only=False,
              logic_adapters=[
                  {
                      'import_path':'chatterbot.logic.BestMatch',
                   }])

# Alt qna list, must have an even number of elements
custom_training_file_path = 'bot/training_data.txt'

# Read conversation pairs from the custom text file and train the ChatBot
with open(custom_training_file_path, 'r', encoding='utf-8') as file:
    conversations = [line.strip() for line in file.readlines()]

list_trainer = ListTrainer(bot)


# Train the ChatBot using ListTrainer
list_trainer.train(conversations)

chatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)

# list_trainer.train(list_to_train)

chatterbotCorpusTrainer.train('chatterbot.corpus.english')

# Create your views here.
def index(request):
    return render(request, 'index.html')

def getResponse(request):
    userMessage = request.GET.get('userMessage')

    chatResponse = str(bot.get_response(userMessage))
    # This response will be sent back to index.html, specifically to the data of the Ajax request
    return HttpResponse(chatResponse)
