e = 2.7182818284590452353602874713527


# Contains different activation functions and their derivatives
# Contained as static functions
class Functions:
    def __init__(self):
        pass

    @staticmethod
    def tanh(x):
        return 2 / (1 + e**(-2 * x)) - 1

    @staticmethod
    def d_tanh(x):  # Derivative of tanh
        return 1 - (2 / (1 + e**(-2 * x)) - 1)**2

    @staticmethod
    def sigmoid(x):
        return 1 / (1 + e**(-x))

    @staticmethod
    def d_sigmoid(x):  # Derivative of sigmoid
        return (1 / (1 + e**(-x))) * (1 - (1 / (1 + e**(-x))))

    @staticmethod
    def ReLu(x):
        return max(x, 0)

    @staticmethod
    def d_ReLu(x):  # Derivative of ReLu
        if x < 0:
            return 0
        return 1


    @staticmethod
    def leakyReLu(x, a):  # Takes another paramter a
        if x > 0:
            return x
        return a*x


    @staticmethod
    def d_leakuReLu(x, a):  # Derivative of leaky ReLu
        if x >= 0:
            return 1
        return a
