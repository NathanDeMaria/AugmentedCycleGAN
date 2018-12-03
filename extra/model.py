import numpy as np
import imageio
import torch


def load_secret():
    p = 'images/armen.jpg'
    secrets = imageio.imread(p)
    right_sized = np.rollaxis(secrets[50:306, 50:306], -1, 0)[None]
    scaled = (((right_sized / 255) - .5) / .5).astype(np.float32)
    torch_secret = torch.from_numpy(scaled).type(torch.FloatTensor)
    return {
        'A': torch_secret, 'A_paths': [p], 'B_paths': [p],  # Just for the shape, all ignored
        'B': torch_secret,
    }
