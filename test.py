import sys
import train

def test(training_file, testing_file):
    X,y = train.process_training_examples(training_file)
    X_test, y_test = train.process_training_examples(testing_file)
    svm = train.train_svm(X, y)
    accuracy = test_with(svm, X_test, y_test)
    print("SVM has classification accuracy of {}%".format(100 * accuracy))


def test_with(classifier, X, y):
    correct_count = 0
    for i in range(len(y)):
        test_vec = X[i]
        label = y[i]
        expected_label = classifier.predict(test_vec)
        if label == expected_label:
            correct_count += 1
        print("Guess: {}\tActual: {}".format(expected_label, label))
    return float(correct_count) / len(y)


def print_usage():
    print("Usage: {} training_data.csv testing_data.csv".format(sys.argv[0]))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print_usage()
        sys.exit(0)
    print("Training data: {}\tTesting data: {}".format(sys.argv[1], sys.argv[2]))
    test(sys.argv[1], sys.argv[2])
