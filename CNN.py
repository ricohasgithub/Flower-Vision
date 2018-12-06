import torch
import torch.nn as nn

import numpy as np

from torch.utils.data import Dataset
from torchvision import transforms, utils

class net (torch.nn):
    
    '''
        
    '''
    
    def __init__(self, in_dim = 112 * 112, out_dim = 101):
        super(net, self).__init__()
        
        