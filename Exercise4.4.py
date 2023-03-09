import numpy as np

print("Calculating the integral of root of (1-x^2) from x=-1 to x=1 \n\n")

#Declaring the variables

def calculateIntegral (N_value):
    N = N_value
    h = 2/N
    x = np.linspace(-1,1,N)
    y = np.sqrt(1 - x**2)

    I = h*sum(y)*2
    delta = I - np.pi
    print(f"With an N value of {N_value}: ")
    print('I = {}'.format(I))
    print('delta = {}'.format(delta))

print("Without 1 second constraint:")
print("--------------------------------------\n")
calculateIntegral(100)
print("--------------------------------------\n")
calculateIntegral(1000)
print("--------------------------------------\n")
calculateIntegral(10000)
print("--------------------------------------\n")
calculateIntegral(100000)
print("--------------------------------------\n")
calculateIntegral(1000000)
print("--------------------------------------\n")
calculateIntegral(10000000)
print("--------------------------------------\n")
calculateIntegral(100000000)
print("--------------------------------------\n")

   
               
