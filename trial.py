import pyautogui
import time
#to find out position of various 
#time.sleep(1)
#print(pyautogui.position())
s=""
n=0
with open('websites.txt','r') as file:    
    for line in file:       
        for word in line.split():          
            s=s+" "+word
            n+=1
            if(n==100):
                #click on message box
                pyautogui.click(x=581, y=373,duration=1)
                #type in msg box
                pyautogui.typewrite(s)
                #click on submit
                pyautogui.click(x=668, y=641,duration=1)
                time.sleep(900)
                #click on refresh
                pyautogui.click(x=89, y=50,duration=1)
                time.sleep(5)
                n=0
                s=""
#click on refresh
pyautogui.click(x=89, y=50,duration=1)
time.sleep(10)
if(len(s)>0):
    #click on message box
    pyautogui.click(x=581, y=373,duration=1)
    #type in msg box
    pyautogui.typewrite(s)
    time.sleep(20)
    #click on submit
    pyautogui.click(x=668, y=641,duration=1)