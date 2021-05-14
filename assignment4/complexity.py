import matplotlib.pyplot as plt
import numpy as np

def convolution_complexity(n, m, j, k):
    return n*m*j*k

def fft_complexity(n, m, j, k):
    #fft(n,m) + fft(j,k) + convolution(j, k, j, k) + fft(n,m)
    # = 2 * fft(n,m) + fft(j,k) + convolution(j, k, j, k)
    return 2 * n * m * np.log2( n* m) + j * k * np.log2(j * k) + n * m

for size in [100, 1000, 10000, 100000, 1000000]:
    fft_complexity_arr = []
    convolution_complexity_arr = []
    threshold = list(range(1,20))
    for x in threshold:
        fft_complexity_arr.append(fft_complexity(size, size, x, x))
        convolution_complexity_arr.append(convolution_complexity(size, size, x, x))

    plt.plot(fft_complexity_arr)
    plt.plot(convolution_complexity_arr)
    plt.title('image of size(' + str(size) + ', ' + str(size) + ') pixels')
    plt.xticks([x for x in threshold if x % 2 == 1], [x for x in threshold if x % 2 == 1])
    plt.ylabel('Count of multiplication')
    plt.xlabel('Filter size k')
    plt.show()