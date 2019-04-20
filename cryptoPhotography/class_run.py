from class_text import TEXT
from class_bulk import MASK_BULK, TEMPORALimg_BULK, STATICimg_BULK, TEMPORALimg_BULK_Omega
from class_image import IMAGE
import cv2
import numpy as np

class RUN():
    def __init__(self, pdfPATH, vidPATH = 0):
        self.vidPATH = vidPATH
        self.pdfPATH = pdfPATH

    def run(self):
        cv2.namedWindow("preview")
        vc = cv2.VideoCapture(self.vidPATH)
        vc.set(cv2.CAP_PROP_FRAME_WIDTH, 128)
        vc.set(cv2.CAP_PROP_FRAME_HEIGHT, 128)
        vc.set(cv2.CAP_PROP_FPS, 30)
        vc.set(cv2.CAP_PROP_BUFFERSIZE, 100)

        if vc.isOpened(): # try to get the first frame
            rval, frame = vc.read()
        else:
            rval = False

        mask_bulk, temporalIMG_bulk = self.setup(frame)

        while rval:
            cv2.imshow("EotMoS", frame)
            rval, frame = vc.read()

            frame = self.constructFrame(frame, mask_bulk, temporalIMG_bulk)

            key = cv2.waitKey(20)
            if key == 27:
                break
        cv2.destroyWindow("preview")

    def setup(self, frame):
        image = IMAGE(frame)
        text = TEXT(self.pdfPATH)
        mask_bulk = MASK_BULK(text, image)
        temporalIMG_bulk = TEMPORALimg_BULK(image)
        return mask_bulk, temporalIMG_bulk

    def constructFrame(self, frame, mask_bulk, temporalIMG_bulk):
        temporalIMG_bulk.updateBULK_(frame)
        _frame = np.einsum('ijkl , ijkl -> ijkl', mask_bulk.BULK_, temporalIMG_bulk.BULK_)
        frame = np.einsum('ijkl -> ijk', _frame)
        return frame

    def constructFrame2(self, frame, mask_bulk, temporalIMG_bulk, counter):
        temporalIMG_bulk.updateBULK_2(frame, counter)
        _frame = np.einsum('ijkl , ijkl -> ijkl', mask_bulk.BULK_, temporalIMG_bulk.BULK_)
        frame = np.einsum('ijkl -> ijk', _frame)
        return frame

