import numpy as np
import matplotlib.pyplot as plt

def calculate_2dift(input):
    ift = np.fft.ifftshift(input)
    ift = np.fft.ifft2(ift)
    ift = np.fft.fftshift(ift)
    return ift.real

if __name__ == "__main__":
    print("Loading challenge data")
    reals = np.loadtxt("r.csv", delimiter=",", dtype=int)
    imags = np.loadtxt("i.csv", delimiter=",", dtype=int)
    print("Finished loading the data.")

    print("Transforming the data.")
    ft = reals + (imags * 1j)
    ift = calculate_2dift(ft)
    print("Finished transforming the data.")

    plt.set_cmap("gray")
    plt.imshow(ift)
    plt.axis("off")
    plt.show()
