from class_text import TEXT
from class_bulk import MASK_BULK,  TEMPORALimg_BULK_Omega
from class_image import IMAGE
import cv2
import skvideo.io
import numpy as np

class RUN():
    def __init__(self, pdfPATH, file_name = 'output', vidPATH = 0):
        self.vidPATH = vidPATH
        self.pdfPATH = pdfPATH
        self.file_name = file_name

    def runv2(self):
        cv2.namedWindow("preview")
        print(self.vidPATH)
        red, blue, green = self.vidPATH

        vc0 = cv2.VideoCapture(red)
        vc1 = cv2.VideoCapture(blue)
        vc2 = cv2.VideoCapture(green)
       
        if vc0.isOpened(): # try to get the first frame
            rval, frame = vc0.read()
        else:
            rval = False

        mask_bulk, temporalIMG_bulk = self.setupv2(frame)
        frames = []
        count = 0

        while rval:
            try:
                # cv2.imshow("EotMoS", frame)
                rval0, frame0 = vc0.read()
                rval1, frame1 = vc1.read()
                rval2, frame2 = vc2.read()

                frame = self.constructFramev2(frame0, frame1, frame2, mask_bulk, temporalIMG_bulk)
                frames.append(frame)
                count += 1

                key = cv2.waitKey(20)
                if key == 27 or not rval0 or not rval1 or not rval2:
                    break
            except Exception as e:
                break

        frames = np.stack(frames, axis = 0)
        skvideo.io.vwrite(self.file_name + ".mp4", frames)

        vc0.release()
        vc1.release()
        vc2.release()
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


