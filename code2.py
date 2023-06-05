#scan function usable such that on running it, the barcode scanner will open, and 
#on detecting the first barcode, it will print the data of the relevant person from
#the csv file.

import cv2
from pyzbar import pyzbar

def read_barcodes_for_each_frame(frame):
    barcodes_in_frame = pyzbar.decode(frame) #returns empty list if no barcodes found
    s = 0
    for barcode in barcodes_in_frame: #wont run if no barcodes found
        barcode_info = barcode.data.decode('utf-8')
        get_list_from_csv(barcode_info)
        s+=1
    return s,frame

def get_list_from_csv(adm):
    adm = adm[4:]
    import csv
    rows = []
    with open('class 12 project\dataset1.csv','r') as f:
        fc = csv.reader(f)
        for row in fc:
            rows.append(row)
            if row[0]==adm:
                #return row
                print(row)
        #return []
        print('No record found') 


def scan():
    s = 0
    camera = cv2.VideoCapture(0)  #0 for iriun, 1 for laptop camera
    ret, frame = camera.read()    #2
    while ret and s==0:
        ret, frame = camera.read()
        s, frame_with_barcode = read_barcodes_for_each_frame(frame)
        cv2.imshow('Scan the ID card here', frame_with_barcode)
        if cv2.waitKey(1)==27:  #27 is the cv2 order of escape key
            break
    camera.release()
    cv2.destroyAllWindows()

scan()