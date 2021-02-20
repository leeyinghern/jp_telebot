from telebot import types

def next_back_keyboard(page_id=1):
    markup = types.InlineKeyboardMarkup()
    back_button = get_back_button(page_id)
    next_button = get_next_button(page_id)
    if back_button:
        markup.add(back_button)
    if next_button:
        markup.add(next_button)
    return markup

def get_back_button(page_id):
    if page_id == 1:
        return
    return types.InlineKeyboardButton(text = "Back", callback_data='{}'.format(page_id-1))

def get_next_button(page_id):
    if page_id == len(photos):
        return
    return types.InlineKeyboardButton(text='Next', callback_data='{}'.format(page_id+1))

def get_id(page_id=1):
    return PHOTOS[page_id]


def welcome_menu_games_list():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text = 'Vocab れんしゅ', callback_data = 'vocab_practice'))
    # markup.add(types.InlineKeyboardButton(text = 'Particle れんしゅ', callback_data = 'particle_practice'))
    return markup

def remove_keyboard():
    markup = types.ReplyKeyboardRemove()
    return markup

# def return_to_start():
#     markup = types.ReplyKeyboardMarkup()
#     markup.add(types.KeyboardButton(text = 'Return to Main Menu'))
#     return markup