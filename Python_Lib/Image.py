import cv2

def image(img):
          image,s = barcode(img)
          image,x = qrcode(img)
          if s =='0':
                    return image,x
          else: return image,s
          return image,s

def qrcode(img):
          try:
                    qcd = cv2.QRCodeDetector()
                    retval, decoded_info, points, straight_qrcode = qcd.detectAndDecodeMulti(img)
                    img = cv2.polylines(img, points.astype(int), True, (0, 255, 0), 3)

                    for s, p in zip(decoded_info, points):
                              img = cv2.putText(img, s, p[0].astype(int),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                              return img,s
          except:return img,'0'

def barcode(img):
          try:      
                    bd = cv2.barcode.BarcodeDetector()
                    retval, decoded_info, decoded_type, points = bd.detectAndDecode(img)
                    img = cv2.polylines(img, points.astype(int), True, (0, 255, 0), 3)
                    for s, p in zip(decoded_info, points):
                              img = cv2.putText(img, s, p[1].astype(int),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                    return img,s
          except:return img,'0'
if __name__ == "__main__":
          cap = cv2.VideoCapture(1)
          while 1:
                    _,img = cap.read()

                    img,j = image(img)

                    if _ == False:
                              break
                    cv2.imshow("j",img)
                    cv2.waitKey(1)