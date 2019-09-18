from copy import copy

moves = []

def init():
    global moves
    for x1 in range(4):
        for x2 in range(4):
            for x3 in range(4):
                for x4 in range(4):
                    moves.append([x1, x2, x3, x4])

def get_score(env, moves, current_state):
    done = False
    score = 0
    for action in moves:
        new_state, reward, done, info = env.step(action)
        current_state = new_state
        score += reward
        if(done):
            break
    return score

def get_best_move(env, current_state):
    best_action = -1
    max_score = -1
    for actions in moves:
        env2 = copy(env)
        score = get_score(env2, actions, current_state)
        if score > max_score:
            max_score = score
            best_action = actions[0]
    return best_action