import random
from Point import Point


def activation(sum):
    if sum >= 0:
        return 1
    else:
        return -1


class Perceptron:
    def __init__(self):
        self.weights = []
        self.initWeights()
        self.learningRate = 0.1

    def initWeights(self):
        for i in range(2):
            self.weights.append(random.uniform(-1, 1))

    def makeGuess(self, inputs):
        sum = 0
        for i in range(len(self.weights)):
            sum += inputs[i] * self.weights[i]
        return activation(sum)

    def trainPerceptron(self, inputs, target):
        _guess = self.makeGuess(inputs)
        error = target - _guess

        # weightler optimize ediliyor
        for i in range(len(self.weights)):
            self.weights[i] += error * inputs[i] * self.learningRate


def main():
    points = []
    guesses = []
    perceptron = Perceptron()
    rate = 0
    for i in range(100):
        points.append(Point())
        perceptron.trainPerceptron((points[i].x, points[i].y), points[i].label)
        guesses.append(perceptron.makeGuess((points[i].x, points[i].y)))
        print("Target Value : %d ----- Guess : %d" % (points[i].label, guesses[i]))
        if points[i].label == guesses[i]:
            rate = rate + 1

    print("Right guess rate : %d" % rate)


if __name__ == '__main__':
    main()