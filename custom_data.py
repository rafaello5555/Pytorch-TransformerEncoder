import os
from torch.utils.data import Dataset 
from IPython.display import Markdown as md

class Custom_Data(Dataset):
    def __init__(self, root_dir, train=True):
        self.root_dir = os.path.join(root_dir, "train" if train else "test")
        self.neg_files = [os.path.join(self.root_dir, "neg", f) \
        for f in os.listdir(os.path.join(self.root_dir, "neg")) if f.endswith('.txt')]


        self.pos_files = [os.path.join(self.root_dir, "pos", f) \
        for f in os.listdir(os.path.join(self.root_dir, "pos")) if f.endswith('.txt')]

        self.files = self.neg_files + self.pos_files 
        self.labels = [0] * len(self.neg_files) + [1] * len(self.pos_files)
        self.pos_count = len(self.pos_files)



    def __len__(self):
        return len(self.files)



    def __getitem__(self, index):
        file_path = self.files[index]
        label = self.labels[index]
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return label, content




start_index = train_dir.pos_count



#for i in range(-10, 10):
    #print(train_dir[start_index + i])

label = {0: " negative review", 1: "positive review"}

num_class = len(set([label for (label, text) in train_dir]))
print("Number of classes:", num_class)

