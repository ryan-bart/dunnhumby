# dunnhumby case study

THIS IS SAVED AS PYTHON FILE SO THE FORMAT IS PRESERVED ON GITHUB. PLEASE DO NOT RUN, WILL NOT WORK. 

casestudy.py was written to display all information requested by the Case Study in the terminal based on user request.   

All information displayed below except for Pasta health plot (option 5 in program).

In order to run on your computer, change the string saved to the 'path' object (line 61) to the path
to your directory containing the Carbo-Loading dataset (.csv files). 

path = 'your path'


Libraries used: os, pandas, numpy, time, matplotlib, glob

 

1. Top 5 products in each category


The top 5 products in each commodity are:

   (sum, dollar_sales)              product_description product_size
0             84645.78     PRIVATE LABEL THIN SPAGHETTI         16oz
1             80414.86  PRIVATE LABEL SPAGHETTI REGULAR         16oz
2             66160.21   PRIVATE LABEL ANGEL HAIR PASTA         16oz
3             61573.90     PRIVATE LABEL SPAGHETTI THIN         32oz
4             60570.79  PRIVATE LABEL SPAGHETTI REGULAR         32oz


*******************************************************************************


                  pasta sauce

   (sum, dollar_sales)        product_description product_size
0            146471.95     RAGU TRADITIONAL PLAIN         26oz
1            115524.62  PREGO REG SPAGHETTI SAUCE         26oz
2             89174.23   RAGU OWS SPAG SAUCE MEAT         26oz
3             80414.19     RAGU SPAGH SAUCE PLAIN         45oz
4             79489.88   RAGU\CHZ CREATION ALFRDO         16oz


*******************************************************************************


                  pancake mixes

   (sum, dollar_sales)                 product_description product_size
0             93321.06           AJ BUTTERMILK PANCAKE MIX         32oz
1             55974.63       AUNT JEM ORIGINAL PANCAKE MIX          2lb
2             50030.20           A/JEM COMPLETE PANCAKE MI         32oz
3             44962.09  PRIVATE LABEL COMPLETE PANCAKE MIX          2lb
4             44004.65           H J PANCK BTRMLK COMP MIX


*******************************************************************************


                  syrups

   (sum, dollar_sales)                 product_description product_size
0             98922.68           AUNT JEMIMA ORIGINL SYRUP         24oz
1             96146.78  PRIVATE LABEL SYRUP PLASTIC BOTTLE         24oz
2             86813.88               MRS BUTTERWORTH SYRUP         24oz
3             66622.01           PRIVATE LABEL MAPLE SYRUP         12oz
4             62945.01        PRIVATE LABEL BUTTERED SYRUP         24oz


*******************************************************************************

2. Top 5 brands in each category



 
 The top 5 brands in each commodity are:

                  pasta

                                   sum
                          dollar_sales
commodity brand
pasta     Private Label  995201.260000
          Barilla        433764.779999
          Creamette      271543.310000
          Mueller        270701.240000
          Ronzoni        213566.480000


*******************************************************************************


                  pasta sauce

                                   sum
                          dollar_sales
commodity   brand
pasta sauce Ragu            1500754.58
            Prego            799932.23
            Classico         438178.47
            Private Label    331062.38
            Bertolli         258090.84


*******************************************************************************


                  pancake mixes

                                     sum
                            dollar_sales
commodity     brand
pancake mixes Aunt Jemima      206698.12
              Hungry Jack      111435.32
              Private Label     73616.82
              Krusteaz          30528.77
              Bisquick          18437.72


*******************************************************************************


                  syrups

                                   sum
                          dollar_sales
commodity brand
syrups    Aunt Jemima        359668.92
          Private Label      352930.86
          Mrs Butterworth    159165.47
          Log Cabin          130904.45
          Karo               120430.98


*******************************************************************************

3. Pasta sales driving force:


Top ten zip codes with highest AVERAGE ORDER VALUE over past 2 years:

                avg_order_value
store_zip_code
40059                  1.389915
37215                  1.380647
30307                  1.374349
38501                  1.368398
30324                  1.365107
40243                  1.358440
62263                  1.351082
37205                  1.343082
30005                  1.339060
37830                  1.327771

Top ten zip codes with highest total sales over past 2 years:

                total_sales
store_zip_code
37211              36754.94
47150              33497.97
40502              32530.89
30024              28128.24
30004              25871.67
30062              24305.35
30064              23544.57
30022              23272.44
40216              22279.84
37221              22112.52

Total Pasta Sales Over Past 2 Years: 2851930.56

Top ten grossing pasta brands:
                       total_sales
brand
Private Label            995201.26
Barilla                  433764.78
Creamette                271543.31
Mueller                  270701.24
Ronzoni                  213566.48
Private Label Premium    208815.78
San Giorgio              124194.64
Hodgson Mills             80520.98
No Yolks                  66295.52
Private Label Value       41127.23

Pasta sales volume: 44.79%

Pasta Sauce sales volume: 36.81%

Combined Pasta and Sauce sales volume: 81.6%

4. Repeat rate for each commodity

pasta:
TOTAL CUSTOMERS:
411601
REPEAT CUSTOMERS:
283513
REPEAT RATE:
0.689

pasta sauce:
TOTAL CUSTOMERS:
362305
REPEAT CUSTOMERS:
253174
REPEAT RATE:
0.699

pancake mixes:
TOTAL CUSTOMERS:
130580
REPEAT CUSTOMERS:
52130
REPEAT RATE:
0.399

syrups:
TOTAL CUSTOMERS:
256514
REPEAT CUSTOMERS:
130420
REPEAT RATE:
0.508

5. Health of pasta

I CREATE AND DISPLAY A PLOT OF WEEKLY SALES VS. WEEK OVER LENGTH OF DATASET.  NOT SEEN HERE. 

For the purpose of this case study,
Health is being compared to the rate of change of weekly sales for a given number of weeks (4weeks/mo).
Each value has an assocated time span.
The larger the value, the more aggressive the change is in a postive direction
The smaller the value (more negative), the less aggressive the change is and if negative,
the more negative the value is, the more aggresive the change is in a negative direction.

3 Month Health: 90.90818181809135
6 Month Health: 49.613478260941086
1 Year Health: 93.85960784320609





