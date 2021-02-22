import cv2

img = '~.png'
src = cv2.imread(img, cv2.IMREAD_COLOR)
dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_'+img, dst)
