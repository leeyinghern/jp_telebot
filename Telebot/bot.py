import telebot
# from telebot import TeleBot, types
from state import States
import keyboards
import storage
from storage import IN_MEMORY_STORE, USER_ANSWERS, WRONG_ANSWERS
import datetime as dt
from Vocab import vocab

token = '1638595494:AAH8urA10YAMc8lYbI5hngdfuwD9SPGaFBQ'
TG_URL = 'https://api/telegram.org/bot{}/{}'

bot = telebot.TeleBot(token)

@bot.message_handler(commands = ['start'])
def welcome_menu(message):
    storage.del_user_state(message.from_user.id)
    hour = dt.datetime.now().hour
    hour_text = 'こんばんは！' if hour > 18 else 'こんにちは！' if hour > 12 and hour < 18 else 'おはいよございます！'
    welcome_message = f"""  
    {hour_text}
    Please select one of the following games to proceed!
    Good luck, and have fun!
    """
    keyboard = keyboards.welcome_menu_games_list()
    bot.send_message(chat_id=message.from_user.id, text = welcome_message, reply_markup=keyboard)

#### VOCAB PRACTICE


# ###### PARTICLE PRACTICE
# @bot.callback_query_handler(func= lambda callback: 'particle_practice' in callback.data )
# def get_particle_questions(callback):
#     storage.set_user_state(callback.from_user.id, 0, "PARTICLE")
#     USER_ANSWERS[callback.from_user.id] = 0
#     WRONG_ANSWERS[callback.from_user.id] = []
#     markup = telebot.types.ReplyKeyboardMarkup()
#     markup.add(telebot.types.KeyboardButton(text = "Start Game"))
#     bot.send_message(chat_id = callback.from_user.id, text = "Press the Start Game button whenever you're ready!", reply_markup = markup)

# @bot.message_handler(func = lambda message: storage.get_current_state.get("PARTICLE") == States.PARTICLE_START_QUIZ)
# def start_particle_quiz(message):
#     bot.send_photo(caption = vocab.questions['question0'], chat_id = message.from_user.id, photo = vocab.questions['image0'], reply_markup=keyboards.remove_keyboard())
#     storage.set_user_state(message.from_user.id, USER_ANSWERS[message.from_user.id] +1 , "VOCAB")


#### OTHER DECORATORS
@bot.message_handler(func = lambda message: True)
def wrong(message):
    storage.del_user_state(message.from_user.id)
    bot.send_message(chat_id = message.from_user.id, text = 'Something went wrong. Type /start to continue', reply_markup=keyboards.remove_keyboard())

@bot.callback_query_handler(func = lambda callback: True)
def wrong_callback(callback):
    storage.del_user_state(message.from_user.id)
    bot.send_message(chat_id = callback.from_user.id, text = 'Something went wrong. Type /start to continue', reply_markup=keyboards.remove_keyboard())


bot.polling()
