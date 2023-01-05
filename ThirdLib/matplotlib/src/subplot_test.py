import numpy as np
import matplotlib.pyplot as plt

def display_multiple_img(images, rows = 1, cols=1):
    figure, ax = plt.subplots(nrows=rows, ncols=cols, figsize=(6.4, 6.4))
    for ind,title in enumerate(images):
        ax.ravel()[ind].imshow(images[title])
        ax.ravel()[ind].set_title(title)
        ax.ravel()[ind].set_axis_off()
    plt.tight_layout()
    plt.show()

total_images = 4
images = {'Image'+str(i): np.random.rand(100, 100) for i in range(total_images)}

display_multiple_img(images, 2, 2)