IN_MEMORY_STORE = {}
USER_ANSWERS = {}
WRONG_ANSWERS = {}

def get_current_state(user_id, game_mode):
    try:
<<<<<<< HEAD
        return IN_MEMORY_STORE[user_id].get(game_mode)

    except AttributeError as a:
        print('Attribute Error ' + str(a))
=======
        if IN_MEMORY_STORE.get(user_id).get(game_mode):
           return IN_MEMORY_STORE.get(user_id).get(game_mode)
        else:
           set_user_state(user_id, 0, game_mode)
           return IN_MEMORY_STORE.get(user_id).get(game_mode)
    except AttributeError:
>>>>>>> d8d813bd97d0707c1d10181d9d7bb1d5208a9eae
        IN_MEMORY_STORE[user_id] = {game_mode:0}
        return IN_MEMORY_STORE.get(user_id).get(game_mode)

def set_user_state(user_id,state, game_mode):
    try:
        IN_MEMORY_STORE[user_id].update({game_mode:state})
    except KeyError:
        IN_MEMORY_STORE[user_id] = {game_mode:state}
        return IN_MEMORY_STORE

def del_user_state(user_id):
    try:
        del IN_MEMORY_STORE[user_id]
    except:
        pass
    return None
<<<<<<< HEAD
=======

# def get_current_state(user_id):
#     return IN_MEMORY_STORE.get(user_id)

# def set_user_state(user_id,state):
#     IN_MEMORY_STORE[user_id] = state
>>>>>>> d8d813bd97d0707c1d10181d9d7bb1d5208a9eae
