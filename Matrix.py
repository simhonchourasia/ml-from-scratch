# http://www.code-spot.co.za/2009/10/08/15-steps-to-implemented-a-neural-net/
import Activation

# Implements a class for matrices
class Matrix:
    # Initializes from a list
    def __init__(self, mat):
        if type(mat[0]) != type([]):
            self.matrix = [mat]  # Converts lists such as [1, 2, 3] into row vectors
        else:
            self.matrix = mat
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])


    # Prints a matrix with proper formatting
    def print_matrix(self):
        for r in range(self.rows):
            for c in range(self.cols):
                print(round(self.matrix[r][c], 10), end=' ')
            print()


# Finds the transpose of a matrix
    def transpose(self):
        ret = [[0 for i in range(self.rows)] for j in range(self.cols)]
        for r in range(self.rows):
            for c in range(self.cols):
                ret[c][r] = self.matrix[r][c]
        return Matrix(ret)


    # Adds two matrices
    def add(self, other):
        return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)])


    # Multiplies matrix by a scalar
    def mult_scalar(self, k):
        return Matrix([[self.matrix[i][j] * k for j in range(self.cols)] for i in range(self.rows)])


    # Multiplies matrices
    def mult_matrix(self, other):
        if self.cols != other.rows:
            return False  # Check if the matrices are compatible
        ret = [[0 for j in range(other.cols)] for i in range(self.rows)]
        for r in range(self.rows):
            for c in range(other.cols):
                for k in range(other.rows):
                    ret[i][j] += self.matrix[r][k] + other.matrix[k][c]
        return Matrix(ret)


    # Performs Hadamard multiplication on matrices (component-wise)
    def mult_hadamard(self, other):
        if (self.rows != other.rows) or (self.cols != other.cols):
            return False  # Check if the matrices are compatible
        return Matrix([[self.matrix[i][j] * other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)])


    # Performs Kronecker multiplication on a row and a column vector
    # Here, self should be the row vector, and other should be the column vector
    def mult_kronecker(self, other):
        if self.rows != 1 or other.cols != 1:
            return False # Check if self is a row vector and other is a column vector
        return Matrix([[self.matrix[0][i]*other.matrix[j][0] for j in range(other.rows)] for i in range(self.cols)])


    # Performs horizontal concatenation of two matrices with the same number of rows
    def concat_horizontal(self, other):
        if self.rows != other.rows:
            return False  # Check if the matrices are compatible
        ret = [[0 for j in range(self.cols+other.cols)] for i in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols + other.cols):
                if j < self.cols:
                    ret[i][j] = self.matrix[i][j]
                else:
                    ret[i][j] = other.matrix[i][j - self.cols]
        return Matrix(ret)


    # Maps every element of a matrix to the result when a function f is applied to every element
    def map(self, f):
        return Matrix([[f(self.matrix[i][j]) for j in range(self.cols)] for i in range(self.rows)])


    # Takes an output vector and converts to a class number
    @staticmethod
    def output_to_class(vect):
        mx = max(vect)
        return vect.index(mx)


    # Takes a class number and converts to an output vector
    @staticmethod
    def class_to_output(num, mx):
        ret = [0 for i in range(mx)]
        ret[num] = 1
        return ret


# Feeds forward in the neural network
# Takes input matrix, weight matrix, and bias matrix as input
# Returns output matrix and a net matrix
def feed_forward(inp, weights, bias, activation=lambda x: Activation.Functions.sigmoid(x)):
    net = mult_matrix(weights, concat_horizontal(inputs, bias))
    output = net.map(activation)
    return [output, net]


## TESTING
test1 = Matrix([[1, 2, 3], [4, 5, 60]])
test1.print_matrix()
test1.transpose().print_matrix()
test2 = Matrix([1, 2, 3, 4]) # row vector
test2.print_matrix()
test2.transpose().print_matrix()
test1.map(lambda x:2**x).print_matrix()
