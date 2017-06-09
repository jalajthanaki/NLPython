# The code credit goes to Mattnedrich(https://github.com/mattnedrich/GradientDescentExample)
# I've merely created a wrapper to get readers started.
# This is the amazing video by Siraj Raval : https://www.youtube.com/watch?v=XdM6ER7zTLk

from numpy import *

# y = mx + b
# m is slope, b is y-intercept
# here we are calculating the sum of squared error by using the equation which we have seen in the book.
def compute_error_for_line_given_points(b, m, points):
    totalError = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (m * x + b)) ** 2
    return totalError / float(len(points))

def step_gradient(b_current, m_current, points, learningRate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        # Here we are coding up out partial derivatives equations and
        # generate the updated value for m and b to get the local minima
        b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
        m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))
    # we are multiplying the b_gradient and m_gradient with learningrate
    # so it is important to choose ideal learning rate if we make it to high then our model learn nothing
    # if we make it to small then our training is to slow and there are the chances of over fitting
    # so learning rate is important hyper parameter.
    new_b = b_current - (learningRate * b_gradient)
    new_m = m_current - (learningRate * m_gradient)
    return [new_b, new_m]

def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m
    for i in range(num_iterations):
        # we are using step_gradient function to calculate the actual partial derivatives for error function
        b, m = step_gradient(b, m, array(points), learning_rate)
    return [b, m]

def run():
    # Step 1 : Read data

    # genfromtext is used to read out data from data.csv file.
    points = genfromtxt("/home/jalaj/PycharmProjects/NLPython/NLPython/ch9/gradientdescentexample/data.csv", delimiter=",")

    # Step2 : Define certain hyperparameters

    # how fast our model will converge means how fast we will get the line of best fit.
    # Converge means how fast our ML model get the optimal line of best fit.
    learning_rate = 0.0001
    # Here we need to draw the line which is best fit for our data.
    # so we are using y = mx + b ( x and y are points; m is slop; b is the y intercept)
    # for initial y-intercept guess
    initial_b = 0
    # initial slope guess
    initial_m = 0
    # How much do you want to train the model?
    # Here data set is small so we iterate this model for 1000 times.
    num_iterations = 1000

    # Step 3 - print the values of b, m and all function which calculate gradient descent and errors
    # Here we are printing the initial values of b, m and error.
    # As well as there is the function compute_error_for_line_given_points()
    # which compute the errors for given point
    print "Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m,
                                                                              compute_error_for_line_given_points(initial_b, initial_m, points))
    print "Running..."

    # By using this gradient_descent_runner() function we will actually calculate gradient descent
    [b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)

    # Here we are printing the values of b, m and error after getting the line of best fit for the given dataset.
    print "After {0} iterations b = {1}, m = {2}, error = {3}".format(num_iterations, b, m, compute_error_for_line_given_points(b, m, points))

if __name__ == '__main__':
    run()
