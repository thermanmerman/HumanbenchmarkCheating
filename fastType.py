import cv2
import pytesseract
import pyscreenshot as ImageGrab
import time
#pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Owner\AppData\Local\Tesseract-OCR\tesseract.exe"

im=ImageGrab.grab(bbox=(400,350,1500,550))
#im.show()
im.save('C:\\Users\\Owner\\Desktop\\Python_projects\\im.jpg')
time.sleep(2)
# Grayscale, Gaussian blur, Otsu's threshold
image = cv2.imread('C:\\Users\\Owner\\Desktop\\Python_projects\\im.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3,3), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Morph open to remove noise and invert image
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
invert = 255 - opening

# Perform text extraction
data = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')
print(data)

cv2.imshow('thresh', thresh)
cv2.imshow('opening', opening)
cv2.imshow('invert', invert)
cv2.waitKey()




#cap = ImageGrab.grab(bbox =(400,350,1500,550))

#'C:\\Users\\Owner\\Desktop\\Python_projects\\im.png'