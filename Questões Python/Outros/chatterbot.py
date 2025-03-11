import chatterbot


bott = chatterbot.ChatBot('Buddy', logic_adapters  = [ 'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter'],)