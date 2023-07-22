import torch
import os
from transformers import TextDataset
from transformers import GPT2Tokenizer
import torch.utils.data as data

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
path_to_folders='SecLists-master'

def get_dataset(target_path='dataset.pt'):
    list_of_datasets = []
    total_files=0
    for subdir, dirs, files in os.walk(path_to_folders):
        for file in files:
            path=os.path.join(subdir, file)
            try :
                if path.endswith('.txt'):
                    list_of_datasets.append(TextDataset(tokenizer=tokenizer,file_path=path, block_size=128))
                    total_files+=1
            except:
                continue

    multiple_json_dataset = data.ConcatDataset(list_of_datasets)
    print('total txt files included : ', total_files)
    
    
    torch.save(multiple_json_dataset, target_path)
    return target_path
def main():
    path_to_data=get_dataset()
    print(path_to_data)
    
if __name__ == "__main__":
    main()
