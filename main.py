from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


#This is compatable with spacy.3.0
class ENGSN:
    ISO_639_1 = 'en_core_web_sm'

bot = ChatBot('Jack', tagger_language = ENGSN)


#Gernal information

#CodeWorks Information
codeWorks_information = ListTrainer(bot)

codeWorks_information.train([
    'How are you?',
    'I am good.',
    'That is good to hear.',
    'Thank you',
    'You are welcome.',
])

#Staff Information
staff_information = ListTrainer(bot)

staff_information.train([
    'Where are you from?',
    'Germany.',
    'That is good to hear.',
    'Thank you',
    'You are welcome.',
])

#Covid-19
covid_19 = ListTrainer(bot)

covid_19.train([
    'Where are you from?',
    'Germany.',
    'That is good to hear.',
    'Thank you',
    'You are welcome.',
])

#Equipment Questions
equipment_question = ListTrainer(bot)

equipment_question.train([
    'Where are you from?',
    'Germany.',
    'That is good to hear.',
    'Thank you',
    'You are welcome.',
])

#Information about Programming
about_Programming = ListTrainer(bot)

about_Programming.train([
    'Where are you from?',
    'Germany.',
    'That is good to hear.',
    'Thank you',
    'You are welcome.',
])

#Track Specific Question

#Python Question
py_question = ListTrainer(bot)

py_question.train([
    'Where are you from?',
    'Germany.',
    'That is good to hear.',
    'Thank you',
    'You are welcome.',
])

#Game Development
game_Dev = ListTrainer(bot)

game_Dev.train([
    'Where are you from?',
    'Germany.',
    'That is good to hear.',
    'Thank you',
    'You are welcome.',
])

#Web Development
web_dev = ListTrainer(bot)

web_dev.train([
    'Where are you from?',
    'Germany.',
    'That is good to hear.',
    'Thank you',
    'You are welcome.',
])

#UB Class
ub_class = ListTrainer(bot)

ub_class.train([
    'Where are you from?',
    'Germany.',
    'That is good to hear.',
    'Thank you',
    'You are welcome.',
])

#SEL
SEL = ListTrainer(bot)

SEL.train([
    'Where are you from?',
    'Germany.',
    'That is good to hear.',
    'Thank you',
    'You are welcome.',
])





while True:
    user = input('You: ')
    bot_input = bot.get_response(user)
    print('Bot: ', bot_input)
