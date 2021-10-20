import cv2
import glob


class resize_img():
    def __init__(self, filename):
        self.filename = filename
        self.img = cv2.imread(self.filename, 0)

    def resize(self, newname):
        resize_img = cv2.resize(self.img, (100, 100))
        cv2.imwrite(newname, resize_img)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()


images = glob.glob("*.jpg")

for image in images:
    img = resize_img(image)
    img.resize("new_"+image)
