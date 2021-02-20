IN_MEMORY_STORE = {}
USER_ANSWERS = {}
WRONG_ANSWERS = {}

def get_current_state(user_id, game_mode):
    try:
        if IN_MEMORY_STORE.get(user_id).get(game_mode):
           return IN_MEMORY_STORE.get(user_id).get(game_mode)
        else:
           return set_user_state(user_id, 0, game_mode)
    except AttributeError:
        pass

def set_user_state(user_id,state, game_mode):
    try:
        IN_MEMORY_STORE[user_id] = IN_MEMORY_STORE[user_id].update({game_mode:state})
    except KeyError:
        IN_MEMORY_STORE[user_id] = {game_mode:state}
    except AttributeError:
        pass

def del_user_state(user_id):
    try:
        del IN_MEMORY_STORE[user_id]
    except:
        pass
    return None


# def get_current_state(user_id):
#     return IN_MEMORY_STORE.get(user_id)

# def set_user_state(user_id,state):
#     IN_MEMORY_STORE[user_id] = state
