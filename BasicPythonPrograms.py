#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### Sidrah Hashmi ###100915053


######################################### program 1: Table.py##########################################

a1 = 1
a2 = 2
a3 = 3
a4 = 4
a5 = 5
b1 = 2
b2 = 3
b3 = 4
b4 = 5
b5 = 6



print("a b a**b")
print(a1, b1, a1**b1)
print(a2, b2, a2**b2)
print(a3, b3, a3**b3)
print(a4, b4, a4**b4)
print(a5, b5, a5**b5)

########################################## end ########################################################

######################################## program 2: SumOfDigits.py#####################################

num1 = int(input("Enter a number from 0 to 1000: "))

sum1 = (num1%10)
sum2 = (num1//10)

total = (sum2+sum1)

print("The sum of the digits is", total)

######################################### end #########################################################

######################################## program 3: NumYearsDays.py####################################

min = int(input("Enter the number of minutes: "))

# number of minutes in a year
year = min // 525600
day = min // 1440
remainmin = day / 525600

print(min, "minutes is approximately", year, "years and,", day, "days")


########################################### end #######################################################

########################################## program 4: Health.py########################################

w = int(input("Enter weight in pounds: "))
h = int(input("Enter height in inches: "))

k = w*0.45359237

m = h*0.0254

bmi = (k/(m)**2)

print("BMI is ", bmi)

########################################## end ########################################################

########################################## program 5: Payroll.py#######################################

name = input("Enter your name: ")
hours = float(input("Enter number of hours worked in a week: "))
rate = float(input("Enter hourly pay rate: "))
fed_tax = float(input("Enter federal tax withholdding rate: "))
st_tax = float(input("Enter state tax withholding rate: "))

gross = float(hours)*float(rate)
fed_percent = float(fed_tax)*100
fed_withholding = float(gross)*float(fed_tax)
st_percent = float(st_tax)*100
st_withholding = float(gross)*float(st_tax)
deduction = float(fed_withholding)+float(st_withholding)
net = float(gross) - float(deduction)

print(" ")
print("Employee Name:", str(name))
print("Hours Worked:", str(hours))
print("Pay Rate: $", str(rate))
print("Gross Pay: $", str(round(gross,2)))
print("Deductions:")
print("    Federal Withholding (", str(fed_percent), "%): $", str(round(fed_withholding,2)))
print("    State Withholding(", str(st_percent), "%): $", str(round(st_withholding,2)))
print("    Total Deduction: $", str(round(deduction,2)))
print("Net pay: $", str(round(net,2)))

########################################### end #######################################################

