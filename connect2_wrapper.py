import torch
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
from connect2 import Connect2Game
from model import c_model

class Connect2GameWrapper:
    def __init__(self):
        self.game = Connect2Game()
        self.game_history = torch.zeros((4, 4))
        self.board = (self.game.get_init_board(), np.random.choice([1, -1]))
        self.winner = 0

    def play_game(self):
        for n in range(4):
            valid = self.game.get_valid_moves(self.board[0])
            indices_of_ones = torch.nonzero(valid == 1).squeeze()

            if indices_of_ones.shape != torch.Size([]):
                random_element = np.random.choice(indices_of_ones)
            else:
                random_element = indices_of_ones

            self.board = self.game.get_next_state(self.board[0], self.board[1], random_element)
            self.game_history[n, :] = self.board[0]

            if self.game.is_win(self.board[0], self.board[1]):
                self.winner = self.board[1]

    def generate_n_games(self, n):
        all_game_history = torch.zeros((n, 4, 4))
        all_winners = torch.zeros((1, n))
        for n in range(n):
            self.__init__()  
            self.play_game()
            all_game_history[n, :, :] = (self.game_history.clone())
            all_winners[:, n] = (self.winner)

        return all_game_history, all_winners

if __name__ == "__main__":
    game_wrapper = Connect2GameWrapper()
    x, y = game_wrapper.generate_n_games(10)