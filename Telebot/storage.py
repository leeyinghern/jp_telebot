IN_MEMORY_STORE = {}
USER_ANSWERS = {}
WRONG_ANSWERS = {}

def get_current_state(user_id, game_mode):
    try:
        return IN_MEMORY_STORE[user_id].get(game_mode)

    except:
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
