from selenium import webdriver
from selenium.webdriver.common.by import By

from openpyxl import load_workbook #import the package that lets you read the spreadsheet
workbook = load_workbook(filename="Statistics_MAT_raw_texts.xlsx") # load the spreadsheet
sheet = workbook.active # load the appropriate sheet

driver = webdriver.Edge() # Create a new instance of the Chrome driver

print ("These rows need to be deleted as there is no rating to be found:")

for RowNumber in range(2,2860): # loop through each row
    RowNumberString = str(RowNumber) # make row number a string so it can be concatenated
    NameCell= "C" + RowNumberString # concatenate row and column, making name cell
    Filename = str (sheet[NameCell].value) #find the value in that cell and store it as a variable
    FileCode = Filename[-7:] #get the IMDB ID by getting the last 7 characters of the value
    webLink = ("https://www.imdb.com/title/tt" + FileCode + "/") #create weblink for selenium
    try:
        driver.get(webLink) # Open the IMDB website
        Rating = driver.find_element(By.CLASS_NAME,'sc-4dc495c1-1.lbQcRY') # find the rating on IMDB
        RatingText = Rating.text # put rating into text form
        RatingCell = "B" + RowNumberString # concatenate row and column, making rating cell
        sheet[RatingCell].value = RatingText # put in ratings for each film
        workbook.save('Statistics_MAT_raw_texts.xlsx') # save the input
    except:
        print (RowNumber) # show which row needs to be deleted by hand later

driver.close() # close the browser window
