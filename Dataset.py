import csv
import random

class Dataset:
    def __init__(self, labels = ['default'], lst = [[0]], num_outputs = 0):
        self.shape = (len(lst)-1, len(lst[0]))  # First row should have labels
        self.labels = labels
        self.input_count = len(lst[0]) - num_outputs
        self.output_count = num_outputs
        self.outputs = [row[-num_outputs:] for row in lst]
        self.inputs = [row[:-num_outputs] for row in lst]
        self.train_x = []
        self.train_y = []
        self.val_x = []
        self.val_y = []
        self.test_x = []
        self.test_y = []


    # Prints out the first few values of the dataset
    def head(self, num = 5):
        print(self.labels)
        for i in range(min(num, self.shape[0])):
            print(self.inputs[i] + self.outputs[i])


    # Reads data from csv
    # The outputs must be at the end of each row in the csv
    # Number of outputs must be specified
    def read_from_csv(self, filename, num_outputs):
        # First reset current values
        self.inputs = []
        self.outputs = []
        
        self.output_count = num_outputs
        with open(filename, mode='r') as f:
            reader = csv.reader(f, delimiter=',')
            line_num = 0
            for row in reader:
                if line_num == 0:
                    self.labels = row
                    self.input_count = len(row) - num_outputs
                    line_num += 1
                else:
                    self.inputs.append(row[:-num_outputs])
                    self.outputs.append(row[-num_outputs:])
                    line_num += 1
            # print("I looked through " + str(line_num) + " lines.")
            self.shape = (line_num - 1, len(self.labels))
        f.close()


    # Splits the dataset into the given ratios
    # ratios should be a list in the form [train, val, test]
    # train/(train+val+test) will be training
    # val/(train+val+test) will be validation
    # test/(train+val+test) will be testing
    def train_test_split(self, ratios):
        train, val, test = ratios
        train_n = train/(train+val+test)
        val_n = val/(train+val+test)
        test_n = test/(train+val+test)
        train_threshold = train_n
        val_threshold = train_threshold + val_n
        test_threshold = val_threshold + test_n
        
        # Reset the current values
        self.train_x = []
        self.train_y = []
        self.val_x = []
        self.val_y = []
        self.test_x = []
        self.test_y = []
        # Assign rows to train, val, test; randomly but weighted
        for i in range(self.shape[0]):
            rand = random.random()
            if rand < train_threshold:
                self.train_x.append(self.inputs[i])
                self.train_y.append(self.outputs[i])
            elif rand < val_threshold:
                self.val_x.append(self.inputs[i])
                self.val_y.append(self.outputs[i])
            else:  # Goes into testing
                self.test_x.append(self.inputs[i])
                self.test_y.append(self.outputs[i])

# TESTING
iris = Dataset()
iris.read_from_csv('iris.csv', 1)
print(iris.shape)
iris.head()
iris.train_test_split([5, 2, 3])
print(len(iris.train_x))
print(len(iris.val_x))
print(len(iris.test_x))
