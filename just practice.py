import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

df =pd.DataFrame()
csv_file = "C:\python codes\passport project\PassportSeva_1_1.csv"

def introduction():
    msg='''
Passport is one of the most basic requirements if you want to travel outside of India. In order to support the needs of passport of citizen, Government of India has established regional passport offices across the India in different cities.

The dataset contains the data generated in this regional passport seva kendra and the data is categorized in the different categories. 

In this project we are going to analyze the same dataset using Python Pandas on windows machine but the project can be run on any machine which support Python and pandas. Besides pandas we have also used matplotlib python module for visualization of this dataset.
 
The whole project is divided into four major parts, i.e., reading, analysis, visualization and export. All these parts are further divided into menus for easy navigation.

           NOTE: Python is case-SENSITIVE so type exact Column Name wherever required. \n\n\n\n'''
    for x in msg:
        print(x,end ='')
        time.sleep(0.002)
    wait = input('Press ENTER to continue.....')         

def made_by():
    msg=''' Passport Management System made by              : VITARNA SHARMA
            class                                 : Xll-C
            School Name                           : MEERUT PUBLIC GIRL'S SCHOOL
            session                               : 2021-22
            

            Thanks for evaluating my Project.\n\n\n'''

    for x in msg:
        print(x, end='')
        time.sleep(0.002)
    wait = input('Press ENTER to continue.....')



def read_csv_file():
    df =pd.read_csv(csv_file)
    print(df)

# name of function      : clear
# purpose               : clear output screen
def clear():
    for x in range(65):
               print()



def data_analysis_menu():
        df = pd.read_csv(csv_file)
        while True:
            clear()
            print('\n\nData Analysis MENU ')
            print('_'*100)
            print('1.  Data summary of all passport served in different places\n')
            print('2.  Show data related to Specific Column present in csv file\n')
            print('3.  enter a new entry\n')
            print('4.  Delete a entry\n')
            print('5.  RPO Report \n')
            print('6.  Scheme Type Report \n')
            print('7.  Exit (Move to main menu)\n')
            ch = int(input('Enter your choice:'))
            if ch == 1:
                print(df)
                wait = input()
            if ch == 2:
                print(df.columns)
                col_name = input('Enter Column Name that You want to print : ')
                print(df[col_name])
                wait = input()
            if ch==3:
                a = input('Enter service Name :')
                b = input('Enter New Rpo Name :')
                c = input(' Enter New Scheme Type :')
                d= int(input('Enter Total LastWeekCount :'))
                e = int(input('Enter LastMonthCount :'))
                f = int(input('Enter YearTillDate :'))
                g = input('Enter Date of Entry')
                data={'ServiceName':a,'RpoName':b,'SchemeType':c,'LastWeekCount':d,'LastMonthCount':e,'YearTillDate':f,'Date':g}
                df = df.append(data,ignore_index=True)
                print(df)
                wait=input()
            
            if ch==4:
                index_no =int(input('Enter the Index Number that You want to delete :'))
                df = df.drop(df.index[index_no])
                print(df)
                print('\n\n\n Press enter to continue....')
                wait = input()
            
            if ch==5:
                print(df.columns)
                print(df['RpoName'].unique())
                rp= input('Enter Rpo Name ')
                g = df.groupby('RpoName')
                print('Rpo Name ', rp)
                print(g['YearTillDate'].sum())
                print('\n\n\n Press enter to continue....')
                wait=input()
            
            if ch==6:
                df1=df.SchemeType.unique()
                print('Available Schemes :',df1)
                print('\n\n')
                schName =input('Enter Scheme Type :')
                df1=df[df.SchemeType==schName]
                print(df1)
                print('\n\n\n Press enter to continue....')
                wait = input()

            if ch == 7:
                break


# name of function      : graph
# purpose               : To generate a Graph menu
def graph():
    df = pd.read_csv(csv_file)
    while True:
        clear()
        print('\nGRAPH MENU ')
        print('_'*100)
        print('1.  LINE Graph On Total Passport Served In Different States/Cities\n')
        print('2.  Bar Graph On Total Passport Served In Different States/Cities\n')
        print('3.  Bar Graph On RPO Report by user defined condition\n')
        print('4.  Bar Graph On Scheme Type by user defined condition\n')
        print('5.  Exit (Move to main menu)\n')
        ch = int(input('Enter your choice:' ))
        
        if ch==1:
            g = df.groupby('RpoName')
            x = df['RpoName'].unique()
            y = g['YearTillDate'].sum()
            plt.xticks(rotation='vertical')
            plt.xlabel('Regional Offices')
            plt.ylabel('Total Passport served')
            plt.title('Passport served')
            plt.grid(True)
            plt.plot(x, y)
            plt.show()
        
        if ch==2:
            g = df.groupby('RpoName')
            x = df['RpoName'].unique()
            y = g['YearTillDate'].sum()
            plt.xticks(rotation='vertical')
            plt.xlabel('Regional Offices')
            plt.ylabel('Total Passport served')
            plt.title('Passport served')
            plt.bar(x, y)
            plt.grid(True)
            plt.show()
            wait = input()
        
        if ch==3:
            rponames=df['RpoName'].unique()
            print(rponames)
            rpo=input('Enter RpoName as shown It is Case Sensitive : ')
            x = df[df.RpoName==rpo].SchemeType
            y = df[df.RpoName==rpo].LastWeekCount
            plt.bar(x,y)
            plt.xticks(rotation='vertical')
            plt.grid(True)
            plt.title(rpo)
            plt.xlabel('Scheme Types')
            plt.show()
            wait= input()
        
        if ch==4:
            schemes = df.SchemeType.unique()
            print('Available Schemes :',schemes)
            print('\n')
            schName = input('Enter Scheme Type Name :')
            names = df[df.SchemeType==schName].RpoName
            counting = df[df.SchemeType==schName].LastMonthCount
            plt.xticks(rotation='vertical')
            plt.grid(True)
            plt.title(schName)
            plt.xlabel('Regional Passport Office')
            plt.ylabel('No. Of applications')
            plt.bar(names,counting)
            plt.show()

        if ch==5:
            break


# function name          : export_menu
# purpose                : function to generate export menu
def export_menu():   
    df = pd.read_csv(csv_file)
    while True:
        clear()
        print('\n\nEXPORT MENU ')
        print('_'*100)
        print()
        print('1.  CSV File\n')
        print('2.  Exit (Move to main menu)')
        ch = int(input('Enter your Choice : '))

        if ch==1:
            df.to_csv('C:/python codes/passport project/newPassport.csv')
            print('\n\nCheck your new file "newPassport.csv"  on given location')
            wait = input()

        if ch == 2:
            break
        
def main_menu():
           clear()
           introduction()
           while True:
                      clear()
                      print('MAIN MENU ')
                      print('_'*100)
                      print()
                      print('1.  Read CSV File\n')
                      print('2.  Data Analysis Menu\n')
                      print('3.  Graph Menu\n')
                      print('4.  Export Data\n')
                      print('5.  Exit\n')
                      choice = int(input('Enter your choice :'))
        
                      if choice==1:
                                 print('We need to add two number')
                                 read_csv_file()
                                 wait=input()
        
                      if choice==2:
                                 print('We need to subtract two number')
                                 data_analysis_menu()
                                 wait=input()
        
                      if choice==3:
                                 graph()
                                 wait=input()    
        
                      if choice==4:
                                 export_menu()
                                 wait=input()     
        
                      if choice==5:
                                 break
           clear()
           made_by()

# call your main menu
main_menu()


