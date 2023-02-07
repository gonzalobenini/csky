from stockfish import Stockfish
import chess
import os



def ini_engine():
    path = os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__)),'eng'),'stockfish-windows-2022-x86-64-avx2')

    engine = Stockfish(path=path
                            ,parameters={
                                # "UCI_Elo": 2000
                                    "Hash": 4096
                                ,"Threads": 2
                                }
                            )
    # self.load = 0
    engine.set_depth(10)
    # self.board = chess.Board()
    return engine

def calculate_nextmove(engine, board, elo):
    # self.load += 1
    # if self.load <= 4:
        engine.set_fen_position(board)
        engine.set_elo_rating(elo)
        move = engine.get_best_move()
        if move == '':
            print('game over')
            return {"move":'', "fen":''}
        # print(load)
        engine.make_moves_from_current_position([move])

        move += getCastle(board,move)

        board = engine.get_fen_position()
        # self.load -= 1
        response = {"move":move, "fen":board}

        # print(self.engine.get_board_visual())

        print(response)
        return response
    # else:
        # return {"move":'', "fen":''}

def getCastle(fen,move):
    board = chess.Board(fen)
    # print(self.board,move)

    castle = ''
    if board.turn:
        castle += 'w'
    else:
        castle += 'b'

    if (board.is_kingside_castling(chess.Move.from_uci(move))):
        castle += 'k'

    if (board.is_queenside_castling(chess.Move.from_uci(move))):
        castle += 'q'

    if len(castle) == 2:
        return castle
    else:
        return ''






