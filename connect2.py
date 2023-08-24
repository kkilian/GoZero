import torch

class Connect2Game:

    def __init__(self):
        self.columns = 4
        self.win = 2

    def get_init_board(self):
        b = torch.zeros((self.columns,), dtype=torch.int)
        return b

    def get_board_size(self):
        return self.columns

    def get_action_size(self):
        return self.columns

    def get_next_state(self, board, player, action):
        b = board.clone().detach()
        b[action] = player
        return (b, -player)

    def has_legal_moves(self, board):
        return (board == 0).any()

    def get_valid_moves(self, board):
        valid_moves = torch.zeros(self.get_action_size(), dtype=torch.int)

        for index in range(self.columns):
            if board[index] == 0:
                valid_moves[index] = 1

        return valid_moves

    def is_win(self, board, player):
        count = 0
        for index in range(self.columns):
            if board[index] == player:
                count = count + 1
            else:
                count = 0

            if count == self.win:
                return True

        return False

    def get_reward_for_player(self, board, player):
        if self.is_win(board, player):
            return 1
        if self.is_win(board, -player):
            return -1
        if self.has_legal_moves(board):
            return None

        return 0

    def get_canonical_board(self, board, player):
        return player * board
