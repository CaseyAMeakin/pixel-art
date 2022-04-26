import numpy as np
import matplotlib.pyplot as plt


#
pallete = np.array(
    [
        [222, 222, 222],  # 0: b
        # [128, 0, 0],  # 1: w
        # [236, 203, 221],  # 1: melanie
        [196, 139, 165],  # 1:
    ],
)


def get_invader_pixels() -> np.ndarray:
    NX, NY = 10, 10
    image_shape = (NX, NY)
    pix = np.ones(image_shape, dtype="int")
    # border
    pix[0:10, 0] = 0.0  # l border
    pix[0:10, 9] = 0.0  # r border
    pix[0, 0:10] = 0.0  # t border
    pix[9, 0:10] = 0.0  # b border

    # bottom half
    pix[6:10, 0:10] = 0.0

    # eyes
    pix[4, 3] = 0.0  # l
    pix[4, 6] = 0.0  # r

    # head
    pix[0:4, 0:3] = 0.0
    pix[3, 2] = 1.0
    pix[0:4, 7:10] = 0.0
    pix[3, 7] = 1.0
    pix[1, 3] = 0.0
    pix[1, 6] = 0.0

    # tentacles
    pix[6, 3] = 1.0
    pix[6, 6] = 1.0
    pix[7, 2] = 1.0
    pix[7, 4:6] = 1.0
    pix[7, 7] = 1.0
    pix[8, 1] = 1.0
    pix[8, 3] = 1.0
    pix[8, 6] = 1.0
    pix[8, 8] = 1.0

    return pix


def pixels_to_rgb(pixels, pallete):
    shape = pixels.shape
    ndims = len(shape)

    if ndims != 2:
        raise Exception(f"Invalid number of dimensions: ndims = {ndims}")

    cpixels = pallete[pixels]
    return cpixels


def main():

    pixels = get_invader_pixels()
    color_pixels = pixels_to_rgb(pixels, pallete)

    imgplot = plt.imshow(color_pixels)
    ax = plt.gca()
    ax.set_xticks(np.arange(-0.5, 10, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, 10, 1), minor=True)
    ax.grid(which="minor", color="k", linestyle="-", linewidth=1)
    plt.savefig("space-invader.png", dpi=600)
    plt.show()


if __name__ == "__main__":
    main()
