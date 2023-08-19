import torch 
from torch import nn 
import numpy as np
import torch.nn.functional as F

import numpy as np
np.set_printoptions(suppress=False)
import torch
import torch.nn  as nn
import torch.nn.functional as F
torch.set_printoptions(sci_mode=False)
import math

import torch
import torch.nn as nn
import torch.nn.functional as F

class c_model(nn.Module):
    def __init__(self, board_size):
        super(c_model, self).__init__()
        self.size = board_size
        self.fc1 = nn.Linear(in_features=self.size, out_features=16)
        self.fc2 = nn.Linear(in_features=16, out_features=16)
        self.sublayer = nn.Linear(in_features=16, out_features=128)
        self.action_head = nn.Linear(in_features=128, out_features=16)
        self.value_head = nn.Linear(in_features=128, out_features=1)

    def forward(self, x):
        x = x.view(-1, 16)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.sublayer(x))
        action_logits = self.action_head(x)
        value_logit = self.value_head(x)
        return torch.tanh(value_logit) #for now return just value network output

    def predict(self, board):
        board = torch.FloatTensor(board.astype(np.float32))
        self.eval()
        with torch.no_grad():
            v = self.forward(board)
        return v.item()
