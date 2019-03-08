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
    import cv2

    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)

    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False
    
    import pdb; pdb.set_trace()


    while rval:
        cv2.imshow("preview", frame)
        rval, frame = vc.read()
        #frame = torch.einsum('ijkl->klj',[Img(frame).imageTensor]).numpy()
        #frame = frame * 255
        #frame = frame.astype('uint8')
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break
    cv2.destroyWindow("preview")
