from sklearn import svm

TRAINING_DATA_FILE = "train.csv"
NUM_CATEGORIES = 28

def process_training_examples(filename):
    X = []
    y = []
    with open(filename, 'r') as training_data:
        while True:
            line = training_data.readline().rstrip()
            if line == "":
                break
            data = [ float(x) for x in line.split(',') ]
            X.append(data[:-1])
            y.append(int(data[-1]))
    print("We have now processed all {} training examples".format(len(y)))
    return X, y

def train_svm(X, y):
    clf = svm.LinearSVC()
    clf.fit(X, y)
    return clf

def train_kmeans(X, y):
    pass
