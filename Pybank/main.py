#import dependencies
import os
import csv

#Path to csv file
filepath = os.path.join("Resources","02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")


#open and read csv
with open(filepath) as csvfile:
    datareader = csv.reader(csvfile,delimiter=",")
    header = next(datareader)

    #create lists to hold months, profit and profit change
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

    #Find the change in profit between the first and last period and divide by the number of months-1 for average profit change
    absolute_profit_change = profit[total_months-1]-profit[0]
    average_profit_change = absolute_profit_change/((total_months)-1)
    #print(average_profit_change)

    #Find the greatest increase in profits over the entire period
    max_profit=max(profit_change)
    #print(max_profit)

    #Find the corresponding month for profit increase, remembering there are 2 additional rows at beginning of month and profit data
    index_max = profit_change.index(max_profit)+2
    #print(index_max)
    max_month = months[index_max]
    #print(max_month)

    # Find the greatest decrease in losses over the entire period
    min_profit=min(profit_change)
    #print(min_profit)

    #Find the corresponding month for loss decrease, remembering there are 2 additional rows to month and profit data
    index_min = profit_change.index(min_profit)+2
    #print(index_min)
    min_month = months[index_min]
    #print(min_month)

#print results to terminal
    print("Financial Analysis")
    print("--------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit}")
    print(f"Average Change: ${average_profit_change:0.2f}")
    print(f"Greatest Increase in Profits: {max_month} , (${max_profit})")
    print(f"Greatest Decrease in Profits: {min_month} , (${min_profit})")
    
#print to text file
text_file = open("Analysis/Output.txt", "w")
text_file.writelines(f"Financial Analysis \n-------------------------- \nTotal Months: {total_months} \nTotal: ${total_profit} \nAverage Change: ${average_profit_change:0.2f} \nGreatest Increase in Profits: {max_month} , (${max_profit}) \nGreatest Decrease in Profits: {min_month} , (${min_profit})")
text_file.close()