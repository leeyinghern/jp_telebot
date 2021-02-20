from telebot import TeleBot, types
from state import States
import keyboards
import storage
from storage import IN_MEMORY_STORE, USER_ANSWERS, WRONG_ANSWERS
import datetime as dt
from Vocab import vocab

token = '1638595494:AAH8urA10YAMc8lYbI5hngdfuwD9SPGaFBQ'
TG_URL = 'https://api/telegram.org/bot{}/{}'

bot = TeleBot(token, parse_mode='HTML')

@bot.message_handler(commands = ['start'])
def welcome_menu(message):
    hour = dt.datetime.now().hour
    hour_text = 'こんばんは！' if hour > 18 else 'こんにちは！' if hour > 12 and hour < 18 else 'おはいよございます！'
    welcome_message = f"""  
    <b> {hour_text} </b>
    Please select one of the following games to proceed!
    Good luck, and have fun!
    """
    keyboard = keyboards.welcome_menu_games_list()
    bot.send_message(chat_id=message.from_user.id, text = welcome_message, reply_markup=keyboard)

#### VOCAB PRACTICE
@bot.callback_query_handler(func= lambda callback: 'vocab_practice' in callback.data )
def get_vocab_questions(callback):
    storage.set_user_state(callback.from_user.id, 0, "VOCAB")
    USER_ANSWERS[callback.from_user.id] = 0
    WRONG_ANSWERS[callback.from_user.id] = []
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton(text = "Start Game"))
    bot.send_message(chat_id = callback.from_user.id, text = "Press the Start Game button whenever you're ready! Or send any message to continue.", reply_markup = markup)

@bot.message_handler(func= lambda message: storage.get_current_state(message.from_user.id).get('VOCAB') == States.VOCAB_START_QUIZ)
def start_vocab_quiz(message):
    bot.send_photo(caption = vocab.questions['question0'], chat_id = message.from_user.id, photo = vocab.questions['image0'], reply_markup=keyboards.remove_keyboard())
    storage.set_user_state(message.from_user.id, USER_ANSWERS[message.from_user.id] +1 , "VOCAB")

@bot.message_handler(func= lambda message: storage.get_current_state(message.from_user.id).get("VOCAB") > 0 )
def next_question(message):
    try:
        current_state = storage.get_current_state(message.from_user.id)
        prev_state = current_state - 1
        prev_ans = message.text
        if prev_ans in vocab.questions[f'answers{prev_state}']:
            USER_ANSWERS[message.from_user.id]+=1
        else:
            WRONG_ANSWERS[message.from_user.id].append({'Your Answer': prev_ans, "Correct Answer": vocab.questions[f'answers{prev_state}']})
        bot.send_photo(caption = vocab.questions[f'question{current_state}'], chat_id = message.from_user.id, photo = vocab.questions[f'image{current_state}'])
        storage.set_user_state(message.from_user.id, current_state+1, "VOCAB")

    except KeyError:
        storage.set_user_state(message.from_user.id, 0, "VOCAB")
        bot.send_message(text = 'Quiz finished! Well done! Calculating your result...', chat_id = message.from_user.id)
        bot.send_animation(chat_id = message.from_user.id, animation = 'https://i.pinimg.com/originals/fd/3c/cd/fd3ccd7b49e366b4206f5ac7f8fa8dac.gif',
        caption= f"Your score is {USER_ANSWERS[message.from_user.id]}/9. Thanks for playing!")
        if WRONG_ANSWERS[message.from_user.id]:
            mistakes = ""
            for index, item in enumerate(WRONG_ANSWERS[message.from_user.id]):
                mistakes = mistakes + "For Qustion: " + str(index + 1) + " Your Answer was: " + str(item['Your Answer']) + " The correct Answer(s) are: " + str([i for i in item['Correct Answer']]) + '\n' + '\n'
            bot.send_message(text = mistakes, chat_id = message.from_user.id)
        


###### PARTICLE PRACTICE
@bot.callback_query_handler(func= lambda callback: 'particle_practice' in callback.data )
def get_particle_questions(callback):
    storage.set_user_state(callback.from_user.id, 0, "PARTICLE")
    USER_ANSWERS[callback.from_user.id] = 0
    WRONG_ANSWERS[callback.from_user.id] = []
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton(text = "Start Game"))
    bot.send_message(chat_id = callback.from_user.id, text = "Press the Start Game button whenever you're ready!", reply_markup = markup)

@bot.message_handler(func = lambda message: storage.get_current_state.get("PARTICLE") == States.PARTICLE_START_QUIZ)
def start_particle_quiz(message):
    bot.send_photo(caption = vocab.questions['question0'], chat_id = message.from_user.id, photo = vocab.questions['image0'], reply_markup=keyboards.remove_keyboard())
    storage.set_user_state(message.from_user.id, USER_ANSWERS[message.from_user.id] +1 , "VOCAB")


#### OTHER DECORATORS
@bot.message_handler(func = lambda message: True)
def wrong(message):
    bot.send_message(chat_id = message.from_user.id, text = 'Something went wrong. Type /start to continue', reply_markup=keyboards.remove_keyboard())

@bot.callback_query_handler(func = lambda callback: True)
def wrong_callback(callback):
    bot.send_message(chat_id = callback.from_user.id, text = 'Something went wrong. Type /start to continue', reply_markup=keyboards.remove_keyboard())


bot.polling()