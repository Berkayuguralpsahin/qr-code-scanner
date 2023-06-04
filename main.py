from  flet import *
#INSTALL YOU OPENCV WİTH PIP
import numpy as np
import cv

def main(page:Page):
    
    myresult = Column()


    def readqrcode(e):
        cap = cv.VideoCapture(0)
        while True:
            ret,frame = cap.read()
            if not ret:
                break
            
            gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
            detector = cv.QRCodeDetector()
            data,points,_ = detector.detectorAndDecode(gray)
            
            # AND IF THE OPENCV FOUND YOU QR CODE AND GET TEXT FROM QRCODE
            if data:
                cv.polylines(frame,[np.int32(points)],True,(255,0,0),2,cv.LİNE_AA)
                print(f"QR Code You Data is : {data}")

                #AND PUSH TO TEXT WIDGET IF FOUND

                myresult.controls.append(
                    Text(data,size=25,weight="bold")
                )
                page.update()

                cap.release()
                # AND CLOSE WINDOW WEBCAM IF FOUND TEXT FROM QRCODE
                cv.destroyAllWindows()
                break

               # AND IF YOU PRESS q IN WEBCAM WINDOW THE CLOSE THE WEBCAM
            cv.inshow("QR CODE DETECTion ".frame)
            if cv.waitKey(i) & 0xFF == ord("q"):
                   break
                   # STOP YOU WİNDOW
        if cap.isOpened():
             cap.release()
             cv.destroyAllWindows() 


    page.add(
        Column([
        Text("Qrcode Scanner",size = 30, weight = "bold"),
        ElevatedButton("Read Qr Code",
            bgcolor="blue",color="white",
            on_click=readqrcode
        ),
        # AND SHOW RESULT FROM YOU QR CODE TO TEXT WİDGET    
        
        Divider(),
        myresult


        ])
    )

flet.app(target=main)    