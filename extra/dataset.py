import numpy as np
import matplotlib.pyplot as plt
from data import CreateDataLoader

from .less_dumb_opts import Opt, CycleOpt


def load_conditional_gan_dataset():
    # This is the pix2pix one that I downloaded...
    loader = CreateDataLoader(Opt())
    return loader.load_data()


def display(tensor, ax=None, batch_index=0):
    if ax is None:
        ax = plt
    ax.axis('off')
    image = tensor.numpy()[batch_index]
    image = np.rollaxis(image, 0, 3)
    unnormalized = (.5 * image + .5)
    ax.imshow(unnormalized)


def load_cyclegan_dataset():
    loader = CreateDataLoader(CycleOpt())
    return loader.load_data()
