from openpyxl import load_workbook
# import database model
from app import db

def seeder():
  #Load the excel file
  workbook=load_workbook(filename='')
  
  #loop the sheets in the workbook
  for sheet_name in workbook.sheetnames:
    sheet=workbook[sheet_name]
    
    #loop rows in the sheet
    for row in sheet.iter_rows(min_row=2):
      #create a title model for each row
      
