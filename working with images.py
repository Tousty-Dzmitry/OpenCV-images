import cv2



img = cv2.imread('1.jpg')

# resizing
wide = 400
f = float(wide) / img.shape[1]
new_size = (wide, int(img.shape[0]*f))
new_img = cv2.resize(img, new_size, interpolation=cv2.INTER_AREA)
cv2.imshow('original', new_img)

gray_image = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)

# drawing
cv2.rectangle(new_img, (170,75),(270,250),(0,255,0),5)
cv2.rectangle(new_img,(10,100),(160,400),(255,0,0),5)




# text
cv2.putText(new_img, 'Horse', (10,70), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 0, 0), 5)
cv2.putText(new_img, 'Gerl', (165,50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0), 5)

# save image
cv2.imwrite('girl and horse.jpg', new_img)


cv2.imshow('image', new_img)
cv2.imshow('image-2', gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()