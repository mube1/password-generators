
import torch
from transformers import GPT2LMHeadModel


def get_model(model_path=None):
    if model_path:
        return torch.load(model_path)
    
    return GPT2LMHeadModel.from_pretrained('gpt2')
    

