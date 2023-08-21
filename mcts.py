class Node:
    def __init__(self, prob, player):
        
        self.prob = prob

        self.visit_count = 0
        self.value = 0

        self.children = {}

        self.player = player
        self.board_state = None
    
    def expanded(self):
        return len(self.children) > 0