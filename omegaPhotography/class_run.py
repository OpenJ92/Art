from class_text import TEXT
from class_bulk import MASK_BULK,  TEMPORALimg_BULK_Omega
from class_image import IMAGE
import cv2
import numpy as np

class RUN():
    def __init__(self, pdfPATH, vidPATH = 0):
        self.vidPATH = vidPATH
        self.pdfPATH = pdfPATH

    def runv2(self):
        cv2.namedWindow("preview")
        vc0 = cv2.VideoCapture('testmov/red.mov')
        vc1 = cv2.VideoCapture('testmov/green.mov')
        vc2 = cv2.VideoCapture('testmov/blue.mov')
        
        vc0.set(cv2.CAP_PROP_FRAME_WIDTH, 128)
        vc0.set(cv2.CAP_PROP_FRAME_HEIGHT, 128)
        vc0.set(cv2.CAP_PROP_FPS, 30)
        vc0.set(cv2.CAP_PROP_BUFFERSIZE, 100)

        vc1.set(cv2.CAP_PROP_FRAME_WIDTH, 128)
        vc1.set(cv2.CAP_PROP_FRAME_HEIGHT, 128)
        vc1.set(cv2.CAP_PROP_FPS, 30)
        vc1.set(cv2.CAP_PROP_BUFFERSIZE, 100)

        vc2.set(cv2.CAP_PROP_FRAME_WIDTH, 128)
        vc2.set(cv2.CAP_PROP_FRAME_HEIGHT, 128)
        vc2.set(cv2.CAP_PROP_FPS, 30)
        vc2.set(cv2.CAP_PROP_BUFFERSIZE, 100)


        if vc0.isOpened(): # try to get the first frame
            rval, frame = vc0.read()
        else:
            rval = False

        mask_bulk, temporalIMG_bulk = self.setupv2(frame)

        while rval:
            cv2.imshow("EotMoS", frame)
            rval0, frame0 = vc0.read()
            rval1, frame1 = vc1.read()
            rval2, frame2 = vc2.read()

            frame = self.constructFramev2(frame0, frame1, frame2, mask_bulk, temporalIMG_bulk)

            import pdb;pdb.set_trace()
            
            #import pdb;pdb.set_trace()

            key = cv2.waitKey(20)
            if key == 27:
                break
        cv2.destroyWindow("preview")


    def setupv2(self, frame):
        image = IMAGE(frame)
        text = TEXT(self.pdfPATH)
        mask_bulk = MASK_BULK(text, image)
        temporalIMG_bulk = TEMPORALimg_BULK_Omega(image)
        return mask_bulk, temporalIMG_bulk

    def constructFramev2(self, frame0, frame1, frame2, mask_bulk, temporalIMG_bulk):
        temporalIMG_bulk.updateBULK_(frame0, frame1, frame2)
        _frame = np.einsum('ijkl , ijkl -> ijkl', mask_bulk.BULK_, temporalIMG_bulk.BULK_)
        frame = np.einsum('ijkl -> ijk', _frame)
        return frame


