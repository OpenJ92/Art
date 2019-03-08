import string
import numpy as np

class MASK_BULK():
    def __init__(self, textInstance, imageInstance):
        self.textInstance = textInstance
        self.imageInstance = imageInstance
        self.printable = string.printable
        self.translateBULKLOC_ = {self.printable[i] : i for i in range(len(self.printable))}
        self.BULK_ = self.constructBULK()

    def constructBULK(self):
        BULK_ = np.zeros(shape = (self.imageInstance.image.shape[0], self.imageInstance.image.shape[1], 3, len(self.printable))).astype('uint8')

        for i in range(BULK_.shape[0]):
            for j in range(BULK_.shape[1]):
                letter = next(self.textInstance.cycletext)
                try:
                    BULK_[i,j, :, self.translateBULKLOC_[letter]] = np.array([1,1,1])
                except:
                    pass
        return BULK_


class TEMPORALimg_BULK():
    def __init__(self, imageInstance):
        self.printable = string.printable
        self.BULK_ = np.zeros(shape = (imageInstance.image.shape[0], imageInstance.image.shape[1], 3,len(self.printable))).astype('uint8')

    def updateBULK_(self, frame):
        self.BULK_ = np.roll(self.BULK_, 1, axis = 3)
        self.BULK_[:, :, :, 0] = frame

class STATICimg_BULK():
    def __init__(self, imageInstance):
        pass
