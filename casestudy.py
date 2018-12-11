#File: casestudy.py
#

#Source: dunnhumby 2018


import os
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plot1
import time


categories = ['pasta','pasta sauce', 'pancake mixes', 'syrups']
frames = {}


def getData():
    
    os.chdir('C:\dunnhumby - Carbo-Loading CSV')
    files = glob.glob('dh*.csv')

    for fle in files:

        if os.stat(fle).st_size != 0:

            df = pd.read_csv(fle)
            frames[fle] = df

def topProducts():

    #Top 5 products in each commodity.  
    df_3a = pd.DataFrame.merge(frames['dh_transactions.csv'], frames['dh_product_lookup.csv'], on=['upc'])
    table = pd.pivot_table(df_3a, index = ["commodity","upc","product_description"], values = ["dollar_sales"],aggfunc=[np.sum])
    
    print("\n\n The top 5 products in each commodity are:\n")
   
   
    for category in categories:

        table2 = table
        table2 = table2.query('commodity == ["{}"]'.format(category))    
        table2 = table2.sort_values(by=('sum','dollar_sales'),ascending = False)
        table2 = table2.head(5).merge(frames['dh_product_lookup.csv'][['upc','product_description','product_size']], on = ['upc'], how = 'left')
        table2 = table2.drop('upc',1)
        print("                  {}            \n".format(category))
        print(table2)
        print('\n')
        print('*******************************************************************************\n\n')

def topBrands():

    #Top 5 brands in each commodity
    df_3a = pd.DataFrame.merge(frames['dh_transactions.csv'], frames['dh_product_lookup.csv'], on=['upc'])
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

def PastaSales():

    #First, printing out top ten products by sales in the Pasta Category
    df_3a = pd.DataFrame.merge(frames['dh_transactions.csv'], frames['dh_product_lookup.csv'], on=['upc'])
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



    table = pd.pivot_table(df_3a, index = ["commodity","upc","product_description"], values = ["dollar_sales"],aggfunc=[np.sum])
    print("\n\n The top 10 products in Pasta are:\n")
    table2 = table
    table2 = table2.query('commodity == ["pasta"]')    
    table2 = table2.sort_values(by=('sum','dollar_sales'),ascending = False)
    table2 = table2.merge(frames['dh_product_lookup.csv'][['upc','product_description','product_size']], on = ['upc'], how = 'left')
    table2 = table2.head(10)   
    table2 = table2.drop('upc',1)
    print(table2)
    print('\n')
    print('*******************************************************************************\n\n')

    

    df_3a = df_3a.merge(frames['dh_store_lookup.csv'][['store','store_zip_code']], on = ['store'])
    df_3a = df_3a.query('commodity == ["pasta"]')
    zipCodes = df_3a['store_zip_code'].value_counts()
    zipCodes = zipCodes.reset_index()
    zipCodes.columns = ['Zip Code','numTransactions']
    TopTenStorePercentage = zipCodes['numTransactions'].head(10).sum()/zipCodes['numTransactions'].sum()*100
    TopTenStorePercentage = TopTenStorePercentage.round(2)
    print("Top 10 stores (selling pasta) represent {}% transactions".format(TopTenStorePercentage))
    print("\nThere are {} total stores listed".format(zipCodes['Zip Code'].count()))
    print("\nTop Ten Stores w/ number of transactions by Zip Code:")
    print(zipCodes.head(10))


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


def __main__():

    answer = 'start'
    getData()
    while answer != 'exit':
        print("\nThe following options will allow you to navigate through this case study")
        time.sleep(3)
        print("\nSelect from the following options:")
        time.sleep(1)
        print("""1.Type "1" to see top 5 products in each category.""")
        print("""2.Type "2" to see top 5 brands in each category.""")
        print("""3.Type "3" to see top 10 pasta products, total pasta and pasta sauce sales volumes, and top ten pasta-selling stores (customer locations).""")
        print("""4.Type "4" to see the repeat rate for each category.""")
        print("""\nType "exit" to exit.""")
        answer = input("Pleae enter your selection:")

        if answer == '1':
            topProducts()
        elif answer == '2':
            topBrands()
        elif answer == '3':
            PastaSales()
        elif answer == '4':
            calcRepeatRate()
        elif answer == 'exit':
            break
        else:
            input("Invalid Selection. Press Enter to try again.")
            
            
__main__()
#topProducts()
#topBrands()
#PastaSales()
#calcRepeatRate()


  