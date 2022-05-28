# import numpy as np
# import cv2

# img = cv2.imread("assets/2.png")
# pts = np.array([[10,150],[150,100],[300,150],[350,100],[310,20],[35,10]])
# rect = cv2.boundingRect(pts)
# x,y,w,h = rect
# croped = img[y:y+h, x:x+w].copy()
# pts = pts - pts.min(axis=0)
# mask = np.zeros(croped.shape[:2], np.uint8)
# cv2.drawContours(mask, [pts], -1, (255, 255, 255), -1, cv2.LINE_AA)
# dst = cv2.bitwise_and(croped, croped, mask=mask)
# bg = np.ones_like(croped, np.uint8)*255
# cv2.bitwise_not(bg,bg, mask=mask)
# dst2 = bg+ dst
# cv2.imwrite("croped.png", croped)
# cv2.imwrite("mask.png", mask)
# cv2.imwrite("dst.png", dst)
# cv2.imwrite("dst2.png", dst2)

# cv2.show()



import numpy as np
import cv2

def remove_noise(file_path, display=False):
    medical_image = pydicom.read_file(file_path)
    image = medical_image.pixel_array
    
    hu_image = transform_to_hu(medical_image, image)
    brain_image = window_image(hu_image, 40, 80) 
    
    segmentation = morphology.dilation(brain_image, np.ones((1, 1)))
    labels, label_nb = ndimage.label(segmentation)
    
    label_count = np.bincount(labels.ravel().astype(np.int))
    label_count[0] = 0

    mask = labels == label_count.argmax()
 
    mask = morphology.dilation(mask, np.ones((1, 1)))
    mask = ndimage.morphology.binary_fill_holes(mask)
    mask = morphology.dilation(mask, np.ones((3, 3)))
    masked_image = mask * brain_image
    return masked_image

def thresholding(imagefile):
    image1 = cv2.imread(imagefile)
    img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

    ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
    ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
    ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
    ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
    ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)

    cv2.imshow('Binary Threshold', thresh1)
    cv2.imshow('Binary Threshold Inverted', thresh2)
    cv2.imshow('Truncated Threshold', thresh3)
    cv2.imshow('Set to 0', thresh4)
    cv2.imshow('Set to 0 Inverted', thresh5)

    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()
