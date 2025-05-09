import cv2

image = cv2.imread("wallhaven-jx632y.jpg")

if image is None:
    print("Görüntü dosyası bulunamadi.")
    exit()

cv2.imshow("Görüntü", image)

cv2.waitKey(0)

cv2.destroyAllWindows()

h, w, c = image.shape
print("Görüntü boyutu: {w}x{h}piksel, {c} kanal")

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite("goruntu_gri.jpg", image)