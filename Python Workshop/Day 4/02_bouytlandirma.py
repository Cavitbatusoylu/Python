import cv2

image = cv2.imread("wallhaven-jx632y.jpg")

if image is None:
    print("Görüntü bulunamadı.")
    exit()

new_width = 400
new_height = int(image.shape[0] * (new_width / image.shape[1]))

resized_image = cv2.resize(image, (new_width, new_height))
cv2.imwrite("Resized_image.png", resized_image)

rotated_90 = cv2.rotate(resized_image, cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite("Rotated_90.png", rotated_90)

cropped_image = resized_image[50:250, 50:250]

cv2.imshow("Cropped Image", cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()