from custom_data import Custom_Data


root_dir = "/Users/rafail/Desktop/new/imdb_dataset"
train_dir = Custom_Data(root_dir=root_dir, train=True)
test_dir = Custom_Data(root_dir = root_dir, train = False)



start_index = train_dir.pos_count



#for i in range(-10, 10):
    #print(train_dir[start_index + i])

label = {0: " negative review", 1: "positive review"}

num_class = len(set([label for (label, text) in train_dir]))
print("Number of classes:", num_class)
