from class_text import TEXT
from class_bulk import MASK_BULK, TEMPORALimg_BULK, STATICimg_BULK
from class_image import IMAGE
import numpy as np

# A = np.ones(shape = (512,512))

# image = IMAGE(A)
# text = TEXT('./MythOfS.pdf')
# mask_bulk = MASK_BULK(text, image)

import cv2

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

#frame = frame[:256, :256, :]
frame = cv2.resize(frame, dsize=None, fx=0.5, fy=0.5)

image = IMAGE(frame)
text = TEXT('./MythOfS.pdf')
mask_bulk = MASK_BULK(text, image)
temporalIMG_bulk = TEMPORALimg_BULK(image)

counter = 0
while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    frame = cv2.resize(frame, dsize=None, fx=0.25, fy=0.25)
    temporalIMG_bulk.updateBULK_(frame)
    _frame = np.einsum('ijkl , ijkl -> ijkl', mask_bulk.BULK_, temporalIMG_bulk.BULK_)
    frame = np.einsum('ijkl -> ijk', _frame).astype('uint8')
    key = cv2.waitKey(20)
    counter += 1
    print(counter)
    if key == 27:
        break
cv2.destroyWindow("preview")
