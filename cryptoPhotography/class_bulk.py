import string
import numpy as np

class MASK_BULK():
    def __init__(self, tI, iI):
        self.tI = tI
        self.iI = iI
        self.p = string.ascii_letters
        self.trB = {self.p[i] : i for i in range(len(self.p))}
        self.BULK_ = self.constructBULK_([16,16])

    def constructBULK(self):
        BULK_=np.zeros(shape=(self.iI.image.shape[0],self.iI.image.shape[1],3,len(self.p))).astype('uint8')

        for i in range(BULK_.shape[0]):
            for j in range(BULK_.shape[1]):
                letter = next(self.tI.cycletext)
                try:
                    BULK_[i,j, :, self.trB[letter]] = np.array([1,1,1])
                except:
                    pass
        return BULK_

    def constructBULK_(self, w_s):
        BULK_=np.zeros(shape=(self.iI.image.shape[0],self.iI.image.shape[1],3,len(self.p))).astype('uint8')
        window_bulk = np.ones(shape=(w_s[0], w_s[1], 3))

        for i in w_s[0] * np.arange(BULK_.shape[0] // w_s[0]):
            for j in w_s[1] * np.arange(BULK_.shape[1] // w_s[1]):
                letter = next(self.tI.cycletext)
                try:
                    BULK_[i:i+w_s[0],j:j+w_s[1],:,self.trB[letter]]=window_bulk
                except Exception as e:
                    BULK_[i:i+w_s[0],j:j+w_s[1],:,np.random.randint(len(self.p))]=window_bulk
        return BULK_

class TEMPORALimg_BULK():
    def __init__(self, iI):
        self.p = string.ascii_letters
        self.BULK_ = np.zeros(shape=(iI.image.shape[0], iI.image.shape[1], 3,len(self.p))).astype('uint8')

    def updateBULK_(self, frame):
        self.BULK_ = np.roll(self.BULK_, 1, axis = 3)
        self.BULK_[:, :, :, 0] = frame

    def updateBULK_2(self, frame, counter):
        len_ = self.BULK_.shape[3]
        self.BULK_[:, :, :, counter % len_] = frame

class TEMPORALimg_BULK_Omega():
    def __init__(self, iI):
        self.p = string.ascii_letters
        skelf.BULK_ = np.zeros(shape=(iI.image.shape[0], iI.image.shape[1], 3,len(self.p))).astype('uint8')

    def updateBULK_(self, frameR, frameB, frameG):
        frame = np.stack([frameR[:,:,0], frameB[:,:,1], frameG[:,:,2]], axis = 2)
        self.BULK_ = np.roll(self.BULK_, 1, axis = 3)
        self.BULK_[:, :, :, 0] = frame

    def updateBULK_2(self, frame, counter):
        len_ = self.BULK_.shape[3]
        self.BULK_[:, :, :, counter % len_] = frame


class STATICimg_BULK():
    def __init__(self, iI):
        pass

if __name__ == "__main__":
    image = IMAGE(frame)
    pass
