def click2():
    import cv2

    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    img_counter = 0
    # img = cv2.imread("lenna.png")
    # crop_img = img[y:y+h, x:x+w]
    # cv2.imshow("cropped", crop_img)
    # cv2.waitKey(0)
    import numpy as np
    # import cv2

    # image = cv2.imread('download.jpg')
    # y=0
    # x=0
    # h=100
    # w=200
    # crop = image[y:y+h, x:x+w]
    # cv2.imshow('Image', crop)
    # cv2.waitKey(0)
    while True:
        ret, frame = cam.read()
        frame=cv2.rectangle(frame,(int(frame.shape[0]/2),int(frame.shape[0]/3)),(3*int(frame.shape[1]/4),int(frame.shape[1]/2)),(0,0,255),4)
        cv2.imshow("test", frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 27 or img_counter == 1:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
            image = cv2.imread(img_name)
            y=160
            x=238
            h=162
            w=245
            a = int(frame.shape[0]/2)
            b = int(frame.shape[0]/3)
            c = 3*int(frame.shape[1]/4)
            d = int(frame.shape[1]/2)
            print(a,b,c,d,c-a,d-b)
            print(y,y+h,x,x+w,h,w)
            crop = image[y:y+h, x:x+w]
            cv2.imshow('image', crop)
            cv2.imwrite(img_name, crop)
            # cv2.waitKey(0)
            break# print(frame)

    cam.release()
    cv2.destroyAllWindows()
    return (img_name)
# img_name = click2()
# print(img_name)
