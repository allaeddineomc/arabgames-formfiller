#from os import listdir
#from os.path import isfile, join
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from PIL import Image, ImageEnhance, ImageFilter
#import pytesseract
import urllib.request
import csv
import time
import os

username=input("login username")
passwd=input("login password")
link=input("link to arabgames form")

def login(driver):
    driver.get(link)
    time.sleep(10)
    name_input = driver.find_elements(By.XPATH,'//*[@id="A10"]')[0]
    name_input.send_keys(username)
    pass_input = driver.find_elements(By.XPATH,'//*[@id="A11"]')[0]
    pass_input.send_keys(passwd)
    subm_input = driver.find_elements(By.XPATH,'//*[@id="A12"]')[0]
    subm_input.click()
     
def read_csv_file(filename):
    matrix = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            matrix.append(row)
    return matrix
    
def fill(data,driver):
    create_new_button = driver.find_elements(By.XPATH,'//*[@id="A10"]')[0]
    create_new_button.click()
    for row in range(len(data)+1):
        os.system("rm -rf *picture.jpg")
        print(data)[row]
        
        email = data[row][1].upper()
        function = data[row][2]
        family_name_fr = data[row][3].upper()
        name_fr = data[row][4].upper()
        family_name_ar = data[row][6]
        name_ar = data[row][5]
        bith_date = data[row][5]
        phone_number = data[row][8]
        cni_number = data[row][9]
        cni_immission_date = data[row][10]
        cni_expiration_date = data[row][11]
        other_info = data[row][13].upper()
        countery= data[row][12]
        nationality = data[row][14]
        picture = data[row][15]
        cni_picture = data[row][16]
        birth_countery = data[row][17]
        
        try:
            urllib.request.urlretrieve(picture, "./picture.jpg")
            urllib.request.urlretrieve(cni_picture, "./cni_picture.jpg")
        except Exception:
            print ("downloading image failed")
        try:
            time.sleep(2)
            email_field = driver.find_elements(By.XPATH,'//*[@id="A55"]')[0]
            family_name_fr_field = driver.find_elements(By.XPATH,'//*[@id="A11"]')[0]
            name_fr_field = driver.find_elements(By.XPATH,'//*[@id="A7"]')[0]
            family_name_ar_field = driver.find_elements(By.XPATH,'//*[@id="A14"]')[0]
            name_ar_field = driver.find_elements(By.XPATH,'//*[@id="A15"]')[0]
            bith_date_field = driver.find_elements(By.XPATH,'//*[@id="A33"]')[0]
            phone_number_field = driver.find_elements(By.XPATH,'//*[@id="A49"]')[0]
            cni_number_field = driver.find_elements(By.XPATH,'//*[@id="A8"]')[0]
            cni_immission_date_field = driver.find_elements(By.XPATH,'//*[@id="A22"]')[0]
            cni_expiration_date_field = driver.find_elements(By.XPATH,'//*[@id="A9"]')[0]
            other_info_field = driver.find_elements(By.XPATH,'//*[@id="A58"]')[0]
            function_field = driver.find_elements(By.XPATH,'//*[@id="A23"]')[0]
            doctype_field = driver.find_elements(By.XPATH,'//*[@id="A6"]')[0]
            nationality_field = driver.find_elements(By.XPATH,'//*[@id="A57"]')[0]
            male_filed= driver.find_elements(By.XPATH,'//*[@id="A12_1"]')[0]
            female_field= driver.find_elements(By.XPATH,'//*[@id="A12_2"]')[0]        
            countery_field = driver.find_elements(By.XPATH,'//*[@id="A19"]')[0]
            picture_field = driver.find_elements(By.XPATH,'//*[@id="A24"]')[0]
            cni_picture_field = driver.find_elements(By.XPATH,'//*[@id="A36"]')[0]
            birth_countery_field = driver.find_elements(By.XPATH,'//*[@id="A151"]')[0]
        except Exception:
            print ("can't find all fields")
            
        try:
            email_field.send_keys(email)
            family_name_fr_field.send_keys(family_name_fr)
            name_fr_field.send_keys(name_fr)
            family_name_ar_field.send_keys(family_name_ar)
            name_ar_field.send_keys(name_ar)
            bith_date_field.send_keys(bith_date)
            birth_countery_field.select_by_visible_text(birth_countery)
            phone_number_field.send_keys(phone_number)
            address_field.send_keys(address)
            cni_number_field.send_keys( cni_number)
            cni_immission_date_field.send_keys(cni_immission_date)
            cni_expiration_date_field.send_keys(cni_expiration_date)
            other_info_field.send_keys(other_info)
            function_field.select_by_visible_text(function)
            if "man" in gender:
                male_field.click()
            if "women" in gender:
                female_field.click()
            doctype_field.selectByIndex(2);
            countery_field.select_by_visible_text(countery)
            nationality_field.select_by_visible_text(nationality)
            picture_field.send_keys(os.path.dirname(os.path.realpath("picture.jpg")))
            cni_picture_field.send_keys(os.path.dirname(os.path.realpath("cni_picture.jpg")))
        except Exception:
            print("not all fields have been filled")

        done=input("verify than press return key ")
        
        try:
            send_button = driver.find_elements(By.XPATH,'//*[@id="A64"]')[0]
            send_button.click()
        except Exception:
            print ("validation failed") 

def extract(path):
   files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    matrix = []
    for i in range(len(files)+1):
        img=image.open("r", files[i])
        
        email_paper = (img.crop((,,,))).filter(ImageFilter.MedianFilter())
        email_paper = (((ImageEnhance.Contrast(email_paper))enhance(2)).convert('1')).save('email_paper.jpg')
        family_name_fr_paper = (img.crop((,,,))).filter(ImageFilter.MedianFilter())
        family_name_fr_paper = (((ImageEnhance.Contrast(family_name_fr_paper))enhance(2)).convert('1')).save('family_name_fr_paper.jpg')
        name_fr_paper = (img.crop((,,,))).filter(ImageFilter.MedianFilter())
        name_fr_paper = (((ImageEnhance.Contrast(name_fr_paper))enhance(2)).convert('1')).save('name_fr_paper.jpg')
        family_name_ar_paper = (img.crop((,,,))).filter(ImageFilter.MedianFilter())
        family_name_ar_paper = (((ImageEnhance.Contrast(family_name_ar_paper))enhance(2)).convert('1')).save('family_name_ar_paper.jpg')
        name_ar_paper = (img.crop((,,,))).filter(ImageFilter.MedianFilter())
        name_ar_paper = (((ImageEnhance.Contrast(name_ar_paper))enhance(2)).convert('1')).save('name_ar_paper.jpg')
        bith_date_paper = (img.crop((,,,))).filter(ImageFilter.MedianFilter())
        bith_date_paper = (((ImageEnhance.Contrast(bith_date_paper))enhance(2)).convert('1')).save('bith_date_paper.jpg')
        phone_number_paper = (img.crop((,,,))).filter(ImageFilter.MedianFilter())
        phone_number_paper = (((ImageEnhance.Contrast(phone_number_paper))enhance(2)).convert('1')).save('phone_number_paper.jpg')
        address_paper = (img.crop((,,,))).filter(ImageFilter.MedianFilter())
        address_paper = (((ImageEnhance.Contrast(address_paper))enhance(2)).convert('1')).save('address_paper.jpg')
        cni_number_paper = (img.crop((,,,))).filter(ImageFilter.MedianFilter())
        cni_number_paper = (((ImageEnhance.Contrast(cni_number_paper))enhance(2)).convert('1')).save('cni_number_paper.jpg')
        cni_immission_date_paper = (img.crop((,,,))).filter(ImageFilter.MedianFilter())
        cni_immission_date_paper = (((ImageEnhance.Contrast(cni_immission_date_paper))enhance(2)).convert('1')).save('cni_immission_date_paper.jpg')
        cni_expiration_date_paper = (img.crop((,,,))).filter(ImageFilter.MedianFilter())
        cni_expiration_date_paper = (((ImageEnhance.Contrast(cni_expiration_date_paper))enhance(2)).convert('1')).save('cni_expiration_date_paper.jpg')
        pointure_paper = (img.crop((,,,))).filter(ImageFilter.MedianFilter())
        pointure_paper = (((ImageEnhance.Contrast(pointure_paper))enhance(2)).convert('1')).save('pointure_paper.jpg')
        pontalon_paper = (img.crop((,,,))).filter(ImageFilter.MedianFilter())
        pontalon_paper = (((ImageEnhance.Contrast(pontalon_paper))enhance(2)).convert('1')).save('pontalon_paper.jpg')
        tshirt_paper = (img.crop((,,,))).filter(ImageFilter.MedianFilter())
        tshirt_paper = (((ImageEnhance.Contrast(tshirt_paper ))enhance(2)).convert('1')).save('tshirt_paper .jpg')
        
        email = pytesseract.image_to_string(Image.open('email_paper.jpg'))
        family_name_fr = pytesseract.image_to_string(Image.open('family_name_fr_paper.jpg'))
        name_fr = pytesseract.image_to_string(Image.open('name_fr_paper.jpg'))
        family_name_ar = pytesseract.image_to_string(Image.open('family_name_ar_paper.jpg'))
        name_ar = pytesseract.image_to_string(Image.open('name_ar_paper.jpg'))
        bith_date = pytesseract.image_to_string(Image.open('bith_date_paper.jpg'))
        phone_number = pytesseract.image_to_string(Image.open('phone_number_paper.jpg'))
        address = pytesseract.image_to_string(Image.open('address_paper.jpg'))
        cni_number = pytesseract.image_to_string(Image.open('cni_number_paper.jpg'))
        cni_immission_date = pytesseract.image_to_string(Image.open('cni_immission_date_paper.jpg'))
        cni_expiration_date = pytesseract.image_to_string(Image.open('cni_expiration_date_paper.jpg'))
        pointure = pytesseract.image_to_string(Image.open('pointure_paper.jpg'))
        pontalon = pytesseract.image_to_string(Image.open('pontalon_paper.jpg'))
        tshirt = pytesseract.image_to_string(Image.open('tshirt_paper.jpg'))

        os.system ("rm -rf *_paper.jpg")        
        row=["",email,family_name_fr,name_fr,name_ar,family_name_ar,bith_date,phone_number,address,cni_number,cni_immission_date,cni_expiration_date,"","",pointure,pontalon,tshirt,"",""]
        matrix.append(row)
    return matrix
       
def main():
    method=input("'paper' or 'csv' ? ")
    if method == "csv" or "" :
        driver = webdriver.Firefox()
        csvpath=input("path to csv file: ")
        data = read_csv_file(csvpath)
        login(driver)
        fill(data,driver)
        driver.close()
    if method == "paper" :
        driver = webdriver.Firefox()
        imagespath=input("path to images folder: ")
        data = extract(imagespath)
        login()
        fill(data)
        driver.close()
main()
