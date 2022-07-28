from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

#This is compatable with spacy.3.0
class ENGSN:
    ISO_639_1 = 'en_core_web_sm'

bot = ChatBot('CodeWorks', tagger_language = ENGSN)
bot.storage.drop()

#English Corpus
EN_bot = ChatterBotCorpusTrainer(bot)

EN_bot.train(
    "chatterbot.corpus.english",
    "chatterbot.corpus.english.greetings"
)

#Gernal information

#CodeWorks Information
codeWorks_information = ListTrainer(bot)

codeWorks_information.train([
    'What is CodeWorks?',
    'CodeWorks is a virtual and in-person 5 week, 4 days a week, 7 hours a day workshop where managers and '
    'employees(Your child) choose their path and learn and make code within that path. While also following weekly '
    '‘Sprints’ which are weekly objectives that the Managers and employees show their progress throughout the week. '
    'Everyday each employee is put into advisory groups to have check-ins, team-building, and supplemental skills '
    'development. This program includes Tools of the trade related to collaboration, remote work & specific '
    'technologies, Professional skills & career exploration, Financial literacy, Socio-emotional learning. These are '
    'provided throughout the 5 week process. The final sprint in week 5 every group and manager will present a major '
    'project that.',
    'When did CodeWorks first begin? ',
    'CodeWorks had its first run in the summer of 2017.',
    'When did CodeWorks start?',
    'CodeWorks had its first run in the summer of 2017.'
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
    'What is UB Class about?',
    'UB class is about the current events in Baltimore and discussing how do you want to improve the community, '
    'also what can you do if you have an opportunity to make a change in Baltimore and in your neighborhoods.',
    'Will they talk about any sensitive topics?',
    'The UB class will not talk about very sensitive topics only topics that are going on inside of Baltimore at this '
    'present moment.',
    'Does UB Class grant a college credit?',
    'Yes, UB classes do grant one transferable college credit.',
    'Who is the UB class manager?',
    'Miss Jodie Fair is the class Manager.'
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
