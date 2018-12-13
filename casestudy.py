#File: casestudy.py
#Description: Dunnhumby case study #1

#Source: dunnhumby 2018


import os
import glob
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plot1

#defining list containing all categories and dictionary to store imported dataframes. 
categories = ['pasta','pasta sauce', 'pancake mixes', 'syrups']
frames = {}

#Main function
def __main__():

    getData()

    ProductData = cleanData(frames['dh_product_lookup.csv'])
    
    answer = 'start'

    while answer != 'exit':
        print("\nThe following options will allow you to navigate through this case study")
        time.sleep(1)
        print("\nSelect from the following options:")
        time.sleep(1)
        print("""1.Type "1" to see top 5 products in each category.""")
        print("""2.Type "2" to see top 5 brands in each category.""")
        print("""3.Type "3" to review sales driving force.""")
        print("""4.Type "4" to see the repeat rate for each category.""")
        print("""5.Type "5" to see the Health of the Pasta category.""")
        print("""\nType "exit" to exit.""")
        answer = input("Please enter your selection:")

        if answer == '1':
            topProducts(ProductData)
        elif answer == '2':
            topBrands(ProductData)
        elif answer == '3':
            AvgSalesByLocation(frames['dh_transactions.csv'], frames['dh_store_lookup.csv'], ProductData)
            TotalSalesByLocation(frames['dh_transactions.csv'], frames['dh_store_lookup.csv'], ProductData)
            TopGrossingBrands(frames['dh_transactions.csv'], ProductData)
            PastaSales(ProductData)
        elif answer == '4':
            calcRepeatRate()
        elif answer == '5':
            PastaHealth(frames['dh_transactions.csv'], ProductData)
        elif answer == 'exit':
            break
        else:
            input("Invalid Selection. Press Enter to try again.")

#glob together all files containing "dh" and ".csv" from specified directory.  Import each file into dict as dataframe, key is file name including extension. 
def getData():
    
    path = 'C:\dunnhumby - Carbo-Loading CSV'
    os.chdir(path)
    files = glob.glob('dh*.csv')

    for fle in files:
        if os.stat(fle).st_size != 0:
            df = pd.read_csv(fle)
            frames[fle] = df


#row cleaning function for dh_product_lookup.csv. 
def cleanProductDataByRow(row):
    cell = str(row["product_size"])
    cell = cell.replace(' ','')
    cell = cell.strip('N')
    cell = cell.strip('P')
    cell = cell.lower()
    if "ounce" in cell:
        cell = cell.replace("ounce","oz")
    if "#" in cell:
        cell = "NaN"
    return cell
    
#clean product lookup dataframe. returns frame. 
def cleanData(frame):
    frame["Convert"] = ''
    frame['Convert'] = frame.apply(cleanProductDataByRow, axis =1)
    frame['product_size'] = frame['Convert']
    del frame['Convert']
    return frame


#Prints out top 5 products for each category when called. 
def topProducts(ProductData):
 
    df_3a = pd.DataFrame.merge(frames['dh_transactions.csv'], ProductData, on=['upc'])
    table = pd.pivot_table(df_3a, index = ["commodity","upc","product_description"], values = ["dollar_sales"],aggfunc=[np.sum])
    print("\n\n The top 5 products in each commodity are:\n")
   
    for category in categories:
        table2 = table
        table2 = table2.query('commodity == ["{}"]'.format(category))    
        table2 = table2.sort_values(by=('sum','dollar_sales'),ascending = False)
        table2 = table2.head(5).merge(ProductData[['upc','product_description','product_size']], on = ['upc'], how = 'left')
        table2 = table2.drop('upc',1)
        print("                  {}            \n".format(category))
        print(table2)
        print('\n')
        print('*******************************************************************************\n\n')


#Prints out top 5 brands for each category when called. 
def topBrands(ProductData):

    df_3a = pd.DataFrame.merge(frames['dh_transactions.csv'], ProductData, on=['upc'])
    table = pd.pivot_table(df_3a, index = ["commodity","brand"], values = ["dollar_sales"], aggfunc=[np.sum])
    table.round(2)

    print("\n\n The top 5 brands in each commodity are:\n")
    for category in categories:
        table2 = table
        table2 = table2.query('commodity == ["{}"]'.format(category))    
        table2=table2.sort_values(by=('sum','dollar_sales'),ascending = False)
        print("                  {}            \n".format(category))
        print(table2.head(5))
        print('\n')
        print('*******************************************************************************\n\n')


#Prints out top 10 pasta products, pasta and pasta sauce sales volume compared to total, and top ten stores based on transactions.
def PastaSales(ProductData):

    #First, printing out top ten products by sales in the Pasta Category
    df_3a = pd.DataFrame.merge(frames['dh_transactions.csv'], ProductData, on=['upc'])
    comms = df_3a['commodity'].value_counts()
    comms = comms.reset_index()
    comms.columns = ['commodity','numTransactions']
    totalTrans = comms['numTransactions'].sum()
    pastaCount = comms.iat[0,1]/totalTrans*100
    pastaCount = pastaCount.round(2)
    pastaSauceCount = comms.iat[1,1]/totalTrans*100
    pastaSauceCount = pastaSauceCount.round(2)
    print("\nPasta sales volume: {}%".format(pastaCount))
    print("\nPasta Sauce sales volume: {}%".format(pastaSauceCount))
    print("\nCombined Pasta and Sauce sales volume: {}%".format(pastaCount+pastaSauceCount))


def TopGrossingBrands(frame, ProductData):

    frame = frame.merge(ProductData[['upc','commodity','brand']], on =['upc'])
    frame = frame.query("commodity == ['pasta']")
    frame = pd.pivot_table(frame, index = ["brand"], values =["dollar_sales"], aggfunc=[np.sum])
    frame.columns = ['total_sales']
    frame['total_sales'] = frame['total_sales'].round(2)
    frame = frame.sort_values(['total_sales'], ascending = False)
    print("\nTop ten grossing pasta brands:")
    print(frame.head(10))


def AvgSalesByLocation(frame1, frame2, ProductData):
    
    frame1 = frame1.merge(ProductData[['upc','commodity']], on =['upc'])
    frame1 = frame1.merge(frame2[['store','store_zip_code']], on=['store'])
    frame1 = frame1.query("commodity == ['pasta']")
    frame1 = pd.pivot_table(frame1, index = ["store_zip_code"], values = ["dollar_sales"])
    frame1.columns = ['avg_order_value']
    frame3 = frame1.sort_values(['avg_order_value'], ascending = False)
    print("\nTop ten zip codes with highest AVERAGE ORDER VALUE over past 2 years:\n")
    print(frame3.head(10))


def TotalSalesByLocation(frame1, frame2, ProductData):
    
    frame1 = frame1.merge(ProductData[['upc','commodity']], on =['upc'])
    frame1 = frame1.merge(frame2[['store','store_zip_code']], on=['store'])
    frame1 = frame1.query("commodity == ['pasta']")
    totalSales = frame1['dollar_sales'].sum()
    frame1 = pd.pivot_table(frame1, index = ["store_zip_code"], values = ["dollar_sales"], aggfunc =[np.sum])
    frame1.columns = ['total_sales']
    frame3 = frame1.sort_values(['total_sales'], ascending = False)
    print("\nTop ten zip codes with highest total sales over past 2 years:\n")
    print(frame3.head(10))
    print("\nTotal Pasta Sales Over Past 2 Years: {}".format(totalSales.round(2)))


 

#Prints out repeat rate for each category when called. 
def calcRepeatRate():
    
    for category in categories: 
        
        df_3a = pd.DataFrame.merge(frames['dh_transactions.csv'], frames['dh_product_lookup.csv'], on=['upc'])
        table = df_3a.query('commodity == ["{}"]'.format(category))
        AllCustomers = table['household'].nunique()
        print("{}: ".format(category))
        
        #value_counts returns unique values and relative frequencies. 
        customers = table['household'].value_counts()
        customers = customers.reset_index()
        customers.columns=['household','freq']
        oneTimeCustomers = customers['freq'].value_counts()
        oneTimeCustomers = oneTimeCustomers.reset_index()
        oneTimeCustomers.columns = ['customerTrips','numCustomers']
        oneTimeCustomers = oneTimeCustomers['numCustomers'][0]
        repeatRate = (AllCustomers-oneTimeCustomers)/AllCustomers
        repeatRate =repeatRate.round(3)
        print("TOTAL CUSTOMERS:")
        print(AllCustomers)
        print("REPEAT CUSTOMERS:")
        print(AllCustomers - oneTimeCustomers)
        print("REPEAT RATE:")
        print(repeatRate)
        print("")

def PastaHealth(frame, ProductData):

    frame = frame.merge(ProductData[['upc','commodity']], on =['upc'])
    frame = frame.query("commodity == ['pasta']")
    frame = pd.pivot_table(frame, index = ["week"], values =["dollar_sales"], aggfunc=[np.sum])
    frame.reset_index()
    frame.columns = ['weekly sales']
    x = frame.index
    y = frame['weekly sales']
    plot1.scatter(x,y)
    plot1.plot(x,y)
    plot1.suptitle('Pasta Health')
    plot1.xlabel('week')
    plot1.ylabel('weekly sales($)')
    print("\n\nFor the purpose of this case study,")
    print("Health is being compared to the rate of change of weekly sales for a given number of weeks (4weeks/mo).")
    print("Each value has an assocated time span.")
    print("The larger the value, the more aggressive the change is in a postive direction")
    print("The smaller the value (more negative), the less aggressive the change is and if negative,")
    print("the more negative the value is, the more aggresive the change is in a negative direction.\n")
    print("3 Month Health: {}".format((frame['weekly sales'].iloc[-1]-frame['weekly sales'].iloc[-12])/11))
    print("6 Month Health: {}".format((frame['weekly sales'].iloc[-1]-frame['weekly sales'].iloc[-24])/23))
    print("1 Year Health: {}".format((frame['weekly sales'].iloc[-1]-frame['weekly sales'].iloc[-52])/51))

    plot1.show()

            
__main__()



  