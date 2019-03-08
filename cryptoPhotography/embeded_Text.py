import cv2 as cv
import numpy as np
from functools import reduce
import os
import string
import PyPDF2

# Goal of project:
#       1. Link an arbitrary directory of images to a Bulk image object (make Class)
#           a. Write method that accesses elements by location in (x,y,char)
#           b. Write method on Class that constructs new image from text.
#               - Image should be it's own class with link to directory from which it was created
#       2. Construct text Class that takes in path to document -- .pdf, .docx, etc...
#          and converts said document into string.

class BULK():

    def __init__(self, img_path, pdf_path):
        self.img_path_ = img_path
        self.text_ = TEXT(pdf_path).extract_text()
        self.elements_ = os.listdir(img_path)
        self.characters_ = string.printable
        self.bulk_ = {self.characters_[i]: cv.imread(img_path + '/' + self.elements_[i % len(self.elements_)]) for i in range(0,len(self.characters_))}

    def bulk(self):
        return self.bulk_

    def path(self):
        return [self.path_ + '/' + file for file in self.elements_]

    def construct_Image(self):
        img = IMAGE(self.bulk()['a'].shape)
        for i in range(0, self.bulk()['a'].shape[0]):
            for j in range(0, self.bulk()['a'].shape[1]):
                try:
                    img.img()[i][j] = self.bulk()[self.text_[(i*self.bulk()['a'].shape[1] + j) % len(self.text_)]][i][j]
                except:
                    img.img()[i][j] = np.array([0,0,0])
        return img

class TEXT():

    def __init__(self, path):
        self.path_ = path

    def extract_text(self):
        pdfFileObj = open(self.path_, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        str_ = ''
        for page in range(0,pdfReader.numPages):
            print(page)
            str_ += pdfReader.getPage(page).extractText()
        return str_

class IMAGE():

    def __init__(self, shape):
        self.img_ = np.zeros(shape)

    def img(self):
        return self.img_

    def display(self):
        cv.imshow('Test_A', self.img())
        cv.waitKey(0)
        cv.destroyWindow('Test_A')

    def save(self, name):
        cv.imwrite('test_imgaes/complete_images/' + name + '.jpeg', self.img())
