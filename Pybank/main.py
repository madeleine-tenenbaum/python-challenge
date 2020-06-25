
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
    #print(total_months) 
    #print(total_profit)   
    
    #Find the changes in "Profit/Losses" over the entire period
    profit_change = [profit[i] - profit[i-1] for i in range(2,len(profit))]
    #print(profit_change)

    #Find the average of the changes in "Profit/Losses" over the entire period, convert profit change to absolute values
    absolute_profit_change = map(abs,profit_change)
   
    #print(list(absolute_profit_change))
    average_profit_change=sum(absolute_profit_change)/total_months
    #print(average_profit_change)

    #Find the greatest increase in profits (date and amount) over the entire period
    max_profit=max(profit_change)
    #print(max_profit)
    
    #max_profit_date=row(0) while row(1) in datareader == max_profit
    #print(max_profit_date)

    # Find the greatest decrease in losses (date and amount) over the entire period
    min_profit = min(profit_change)
    #print(min_profit)

    print("Financial Analysis")
    print("--------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: {total_profit}")
    print(f"Average Change: {average_profit_change}")
    print(f"Greatest Increase in Profits: max_profit_date , ({max_profit})")
    print(f"Greatest Decrease in Profits: min_profit_date , ({min_profit})")