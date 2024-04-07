import numpy as np
from PIL import Image

def calculate_2dft(input):
    ft = np.fft.ifftshift(input)
    ft = np.fft.fft2(ft)
    return np.fft.fftshift(ft)

if __name__ == "__main__":
    print("Loading flag data...")
    source_image = Image.open('source.png').convert('L')
    source_image.load()
    print("Source data loaded.")

    print("Applying transformation to source data...")
    transformed_data = calculate_2dft(np.array(source_image))
    print("Data transformed.")

    print("Creating challenge files...")
    real_part = transformed_data.real
    imag_part = transformed_data.imag
    np.savetxt("r.csv", real_part, delimiter=',')
    np.savetxt("i.csv", imag_part, delimiter=',')
    print("Challenge files created.")
