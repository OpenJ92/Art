import string
import numpy as np

class MASK_BULK():
    def __init__(self, textInstance, imageInstance):
        self.textInstance = textInstance
        self.imageInstance = imageInstance
        self.printable = string.ascii_letters
        self.translateBULKLOC_ = {self.printable[i] : i for i in range(len(self.printable))}
        self.BULK_ = self.constructBULK_([16,16])

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

    def constructBULK_(self, window_size):
        BULK_ = np.zeros(shape=(self.imageInstance.image.shape[0], self.imageInstance.image.shape[1], 3, len(self.printable))).astype('uint8')
        window_bulk = np.ones(shape=(window_size[0], window_size[1], 3))

        for i in window_size[0] * np.arange(BULK_.shape[0] // window_size[0]):
            for j in window_size[1] * np.arange(BULK_.shape[1] // window_size[1]):
                letter = next(self.textInstance.cycletext)
                try:
                    BULK_[i:i + window_size[0], j:j + window_size[1], :, self.translateBULKLOC_[letter]] = window_bulk
                except Exception as e:
                    BULK_[i:i + window_size[0], j:j + window_size[1], :, np.random.randint(len(self.printable))] = window_bulk
        return BULK_

    def plot_MASK_BULK(self):
        import matplotlib.pyplot as plt
        from mpl_toolkits.mplot3d import Axes3D

        bulk = self.BULK_
        voxels = np.stack([bulk[:,:,0,element] for element in range(bulk.shape[3])])
        
        fig = plt.figure(figsize = (18, 12))
        ax = fig.gca(projection='3d')
        ax.set_axis_off()
        print("Before Voxel Plot")
        ax.voxels(voxels, facecolors='red', edgecolor = 'k')
        plt.show()
        print("After Voxel Plot")

        import pdb;pdb.set_trace();

class TEMPORALimg_BULK():
    def __init__(self, imageInstance):
        self.printable = string.ascii_letters
        self.BULK_ = np.zeros(shape=(imageInstance.image.shape[0], imageInstance.image.shape[1], 3,len(self.printable))).astype('uint8')

    def updateBULK_(self, frame):
        self.BULK_ = np.roll(self.BULK_, 1, axis = 3)
        self.BULK_[:, :, :, 0] = frame

    def updateBULK_2(self, frame, counter):
        len_ = self.BULK_.shape[3]
        self.BULK_[:, :, :, counter % len_] = frame

class TEMPORALimg_BULK_Omega():
    def __init__(self, imageInstance):
        self.printable = string.ascii_letters
        self.BULK_ = np.zeros(shape=(imageInstance.image.shape[0], imageInstance.image.shape[1], 3,len(self.printable))).astype('uint8')

    def updateBULK_(self, frameR, frameB, frameG):
        frame = np.stack([frameR[:,:,0], frameB[:,:,1], frameG[:,:,2]], axis = 2)
        self.BULK_ = np.roll(self.BULK_, 1, axis = 3)
        self.BULK_[:, :, :, 0] = frame

    def updateBULK_2(self, frame, counter):
        len_ = self.BULK_.shape[3]
        self.BULK_[:, :, :, counter % len_] = frame


class STATICimg_BULK():
    def __init__(self, imageInstance):
        pass

if __name__ == "__main__":
    image = IMAGE(frame)
    pass
