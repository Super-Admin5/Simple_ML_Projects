import cv2 as cv
import numpy as np 

blank = np.zeros((500,500,3), dtype = 'uint8' )
blank[:]= 0,225,0
cv.rectangle(blank,(250,250),(500,500),225,0,0)
cv.imshow('blank',blank)
cv.waitKey(0)