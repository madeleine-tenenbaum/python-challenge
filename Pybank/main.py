
import os
import csv

#Path to csv file
filepath = os.path.join("Resources","02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")


#open and read csv
with open(filepath) as csvfile:
    datareader = csv.reader(csvfile,delimiter=",")
    header = next(datareader)

    #create lists to hold months and profit
    months = []
    profit = []
    profit_change = []

    
    for row in datareader:
        #Create a list of all month data
        months.append(row[0])
        #create a list of all profit data
        profit.append(int(row[1]))
   
   #check unique values in month data and count total
    unique_months = set(months)
    total_months=len(list(unique_months))
    #find sum of profit data
    total_profit=sum(profit)
    
    #check
    print(total_months) 
    print(total_profit)   
    
    #find change in profit between each year 
    profit_change = [profit[i] - profit[i-1] for i in range(2,len(profit))]
    print(profit_change)
        



    
#Find the changes in "Profit/Losses" over the entire period

# #Find the average of the changes in "Profit/Losses" over the entire period

#Find the greatest increase in profits (date and amount) over the entire period

#Find the greatest decrease in losses (date and amount) over the entire period