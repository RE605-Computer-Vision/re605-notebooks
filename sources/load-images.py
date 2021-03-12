import cv2 as cv 

def main():
    img = cv.imread("../images/cat-image.jpg")
    while True:
        cv.imshow("Cat Image", img)
        key = cv.waitKey(1)
        if key == ord('x'):
            cv.destroyAllWindows()
            break

if __name__ == "__main__":
    main()
