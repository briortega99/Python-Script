#!/usr/bin/env python
# coding: utf-8

# In[25]:


import csv
import os

budget_csv = os.path.join("..", "Resources", "budget_data.csv")
export_file = os.path.join("..", "Analysis.txt")

total_months = 0
net_total = 0
net_change_list = []
month_of_changes = []
increase = ["", 0]
decrease = ["", 9999999999]


with open(budget_csv) as budget_data:
    reader = csv.reader(budget_data)
    header = next(reader)    
    first_row = next(reader)
    total_months += 1
    net_total += int(first_row[1])
    previous_net = int(first_row[1])
    
    for row in reader:
        total_months += 1
        net_total += int(row[1])
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list += [net_change]
        
        if(net_change > increase[1]):
                increase[0] = row[0]
                increase[1] = net_change
                
        if(net_change < decrease[1]):
            decrease[0] = row[0]
            decrease[1] = net_change
        
average_change = sum(net_change_list) / len(net_change_list)

analysis = (
f"Financial Analysis\n"
f"---------------------------\n"
f"Total Months : {total_months}\n"
f"Total : ${net_total}\n"
f"Average Change : ${average_change:.2f}\n"
f"Greatest Increase in Profits : {increase[0]} (${increase[1]})\n"
f"Greatest Decrease in Profits : {decrease[0]} (${decrease[1]})"
)
print(analysis)

with open(export_file, "w") as results:
    results.write(analysis)

