import torch
import torchvision.transforms as transforms
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

from main import device

class Img():

    def __init__(self, _input):
        self._input = _input
        self.msize = 512 if torch.cuda.is_available() else 128
        self.loader = transforms.Compose([transforms.Resize(self.msize), transforms.ToTensor()])
        self.unloader = transforms.ToPILImage()
        self.imageTensor = self.buildImgTensor()
        
    def buildImgTensor(self):
        if isinstance(self._input, str):
            image = Image.open(self._input) 
            image = self.loader(image).unsqueeze(0)
           
        if isinstance(self._input, type(np.array([]))):
            image = Image.fromarray(self._input.astype('uint8'), 'RGB')
            image = self.loader(image).unsqueeze(0)

        return image.to(device, torch.float)
    
    def show(self):
        image = self.imageTensor.cpu().clone()
        image = image.squeeze(0)
        image = self.unloader(image)
        plt.imshow(image)
        plt.pause(0.001)

if __name__ == '__main__':
    pass
    
