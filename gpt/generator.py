
# this module generates texts from gpt model


import sys
# sys.argv

import pandas as pd
import numpy as np
import random
import torch
from torch.utils.data import Dataset, DataLoader
from tqdm import tqdm, trange
import torch.nn.functional as F
from transformers import GPT2Tokenizer

import utils

# get model
model = utils.get_model('gpt2_model')

def simple_generate( model,    tokenizer,    prompt,    entry_count=5,    entry_length=1,    top_p=0.8,    temperature=10):
    # if start_input:
    #     x=start_input
    # else:
    #     x='<|endoftext|>'
    filter_value = -float("Inf")
    generated = torch.tensor(tokenizer.encode(prompt)).unsqueeze(0)
    outputs = model(generated, labels=generated)
    loss, logits = outputs[:2]
    logits = logits[:, -1, :] / (temperature if temperature > 0 else 1.0)

    sorted_logits, sorted_indices = torch.sort(logits, descending=True)
    cumulative_probs = torch.cumsum(F.softmax(sorted_logits, dim=-1), dim=-1)

    sorted_indices_to_remove = cumulative_probs > top_p
    sorted_indices_to_remove[..., 1:] = sorted_indices_to_remove[
        ..., :-1
    ].clone()
    sorted_indices_to_remove[..., 0] = 0

    indices_to_remove = sorted_indices[sorted_indices_to_remove]
    logits[:, indices_to_remove] = filter_value

    next_token = torch.multinomial(F.softmax(logits, dim=-1), num_samples=1)
    generated = torch.cat((generated, next_token), dim=1)
    output_list = list(generated.squeeze().numpy())
    output_text = tokenizer.decode(output_list)
    return output_text

def generate(    model,    tokenizer,    prompt,    entry_count=5,    entry_length=1,    top_p=0.8,    temperature=10.,):
    model.eval()
    generated_num = 0
    generated_list = []

    filter_value = -float("Inf")

    with torch.no_grad():

        for entry_idx in trange(entry_count):

            entry_finished = False
            generated = torch.tensor(tokenizer.encode(prompt)).unsqueeze(0)

            for i in range(entry_length):
                outputs = model(generated, labels=generated)
                loss, logits = outputs[:2]
                logits = logits[:, -1, :] / (temperature if temperature > 0 else 1.0)

                sorted_logits, sorted_indices = torch.sort(logits, descending=True)
                cumulative_probs = torch.cumsum(F.softmax(sorted_logits, dim=-1), dim=-1)

                sorted_indices_to_remove = cumulative_probs > top_p
                sorted_indices_to_remove[..., 1:] = sorted_indices_to_remove[
                    ..., :-1
                ].clone()
                sorted_indices_to_remove[..., 0] = 0

                indices_to_remove = sorted_indices[sorted_indices_to_remove]
                logits[:, indices_to_remove] = filter_value

                next_token = torch.multinomial(F.softmax(logits, dim=-1), num_samples=1)
                generated = torch.cat((generated, next_token), dim=1)

                if next_token in tokenizer.encode("<|endoftext|>"):
                    entry_finished = True

                if entry_finished:

                    generated_num = generated_num + 1

                    output_list = list(generated.squeeze().numpy())
                    output_text = tokenizer.decode(output_list)
                    generated_list.append(output_text)
                    break

            if not entry_finished:
              output_list = list(generated.squeeze().numpy())
              output_text = f"{tokenizer.decode(output_list)}<|endoftext|>"
            #   generated_list.append('\n')
              generated_list.append(output_text)

    return generated_list

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

def main(total_number_of_passwords=1,start_input=None):
    generated = []
    if start_input:
        x=start_input
    else:
        x='<|endoftext|>'
    
    for i in range(total_number_of_passwords):
        x = simple_generate(model.to('cpu'), tokenizer, x,    top_p=0.8,    temperature=10)
        generated.append(x)
        # if '\n' in generated[0][-1]:
        #     continue

    return ''.join([j[0].strip('<|endoftext|>') for j in generated])
  
# Using the special variable 
# __name__
if __name__=="__main__":
    try:
       len_of_passwords=int(sys.argv[1])
    except:
        len_of_passwords=1
    generated_text=main(len_of_passwords)
    print(generated_text)
