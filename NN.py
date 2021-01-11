import Matrix
import Dataset
import Activation



def findIno(w, i, b):
    addb = lambda x:x+b
    return i.mult_matrix(w).addConstant(b)

def train(inputs, output, epochs, lr, weights, bias):
    # uses sigmoid activation function
    sigmoid = Activation.Functions.sigmoid
    d_sigmoid = Activation.Functions.d_sigmoid
    
    for epoch in range(epochs):
        inp = inputs
        # Perceptron layer
        ino = findIno(weights, inp, bias)
        # Feed forward
        outo = ino.map(sigmoid)

        error = outo.subtract(output)
        sum_error = error.sumAll()

        # Chain rule
        d_error_d_outo = error
        d_outo_d_ino = outo.map(d_sigmoid)

        d_error_d_ino = d_error_d_outo.mult_hadamard(d_outo_d_ino)

        inp = inp.transpose()
        derivative = mult_matrix(inpt, d_error_d_ino)

        # Backpropogation
        weights = weights.subtract(derivative.mul_scalar(lr))

        for i in range(len(d__error_d_ino.matrix)):
            bias -= lr * d_error_d_ino[i][0]

    return [weights, bias]


# Predict with model
def predict(model, inp):
    weights = model[0]
    bias = model[1]
    return inp.mult_matrix(weights).map(lambda x:x+bias).map(lambda y:sigmoid(y))


