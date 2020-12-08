# import the necessary packages
from PIL import Image
import pytesseract
import cv2
import os
import re

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time


def main():
    
    classes = []

    while True:
        name = input("Enter name of class (-1 to continue):")
        if name == "-1":
            break
        classes.append( {"name":name, "students":[]} )
        
    for thisClass in classes:
        print("Scan students in for class: ", thisClass["name"])
        thisClass["students"] = getNames()

    for thisClass in classes:
        print("Class: ", thisClass["name"])
        for student in thisClass["students"]:
            print("\t", student)
        print()


    driver = login()

    for thisClass in classes:
        print("You named this class: ", thisClass["name"])
        input("Choose which class to submit these students, then press enter to continue")
        for student in thisClass["students"]:
            nameInput = driver.find_element_by_id("attendeeName")
            if student: #if the array is empty, it will skip
                name = student[0] + " " + student[1]
                nameInput.send_keys(name)
                time.sleep(3)
                nameInput.send_keys(u'\ue007')
                time.sleep(3)
        print("Class attendence submitted")
        
    input("Press Enter to Close.")

 
    cv2.destroyAllWindows()



def getNames():
    cv2.namedWindow("getCards")
    vc = cv2.VideoCapture(0)

    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    img_counter = 0

    
    names = []
    while rval:
        cv2.imshow("getCards", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break
        if key == ord(" "): # On space, print OK and save frame as image
            
            text = pytesseract.image_to_string(frame)
            re.sub('[^A-Za-z ]+', '', text)
            arr = text.split()
            names.append(arr)
            for i in range(len(arr)):
                print(i, ": ", arr[i])
            print()

    #close video
    cv2.destroyWindow("getCards")
    
    return names

def login():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://langhorne.perfectmind.com/SocialSite/MemberRegistration/MemberSignIn")


    driver.find_element_by_id("textBoxUsername").send_keys("justin.smith")
    driver.find_element_by_id("textBoxPassword").send_keys("REDACTED")
    driver.find_element_by_id("buttonLogin").click()

    time.sleep(5)
    
    driver.get("https://langhorne.perfectmind.com/Schedule/Checkin")
    driver.maximize_window()

    return driver

if __name__ == "__main__":
    main()
