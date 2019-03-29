import numpy as np
array = [2, 4, 67, 1, 4, 6]
print (np.argsort(array))
taxi = np.genfromtxt('nyc_taxis.csv', delimiter=',', skip_header=True)
print(taxi.dtype)