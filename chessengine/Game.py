# matches = []
# match = {'ipBlack':'','ipWhite':'','currentFen':'','sessionHash':'',Skills}

# crear un objeto juego donde se van a crear sockets para cada jugador y se les va a ir enviando continuamente la jugada
import random

def generate_list(pieces_tpl):
    list = []
    for i in range(5):
        list += pieces_tpl[i]['piece'] * pieces_tpl[i]['prob']
    return list

def update_piece_set(pieces_tpl, piece_took):
    ## p r n b q is the order

    def ret_update_props(pieces_tpl, piece_pos):
        update = pieces_tpl[piece_pos]["updates"].pop(0)
        if len(pieces_tpl[piece_pos]["updates"]) == 0:
            pieces_tpl[piece_pos]["prob"] = 0
        return update

    update = []
    if piece_took == 'p':
        update = ret_update_props(pieces_tpl, 0)
    elif piece_took == 'r':
        update = ret_update_props(pieces_tpl, 1)
    elif piece_took == 'n':
        update = ret_update_props(pieces_tpl, 2)
    elif piece_took == 'b':
        update = ret_update_props(pieces_tpl, 3)
    else:
        update = ret_update_props(pieces_tpl, 4)
    for i in range(5):
        if pieces_tpl[i]['prob'] > 0:
            pieces_tpl[i]['prob'] += update[i]



def generate_random_pieces(color):

    pieces_tpl = ({'piece': 'p', 'prob': 10, 'updates': [
        [-8, 2, 2, 2, 2],
        [-1, 0, 0, 0, 1],
        [-1, 0, 0, 0, 1]
    ]}, {'piece': 'r', 'prob': 20, 'updates': [
        [1, -4, 1, 1, 1],
        [4, -16, 4, 4, 4]
    ]}, {'piece': 'n', 'prob': 21, 'updates': [
        [0, 0, 0, 0, 0],
        [5, 5, -20, 5, 5]
    ]}, {'piece': 'b', 'prob': 21, 'updates': [
        [0, 0, 0, 0, 0],
        [5, 5, 5, -20, 5]
    ]}, {'piece': 'q', 'prob': 28, 'updates': [
        [3, 3, 3, 3, -14],
        [1, 1, 1, 1, -6],
        [2, 2, 2, 2, -8]
    ]})

    def swapPositions(list, pos1, pos2):
        list[pos1], list[pos2] = list[pos2], list[pos1]

    pieces = []
    for i in range(8):
        base_pieces_set = generate_list(pieces_tpl)
        choice = random.randint(0, len(base_pieces_set)-1)
        pieces.append(base_pieces_set[choice])
        #base_pieces_set.remove(choice)
        # del base_pieces_set[choice]
        update_piece_set(pieces_tpl,pieces[-1])
        # print(pieces_tpl)
    if color == 'white':
        for i in range(8):
            pieces[i] = pieces[i].upper()
    else:
        if 'r' in pieces:
            if random.randint(1, 10) < 9:
                if pieces[6] != 'r':
                    swapPositions(pieces,pieces.index('r'),6)
            else:
                if pieces[6] == 'r':
                    piece = random.sample(set(pieces) - set(['r','q']),1)
                    swapPositions(pieces, pieces.index(piece[0]), 6)

    return ''.join(pieces)
