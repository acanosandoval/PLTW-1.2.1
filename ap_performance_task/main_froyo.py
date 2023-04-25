import froyo_functions as froyo_func
import tkinter as tk

# import the data
data_2016 = "ap_performance_task/2016_sales_data"
data_2017 = "ap_performance_task/2017_sales_data"

# creates separate lists for flavor names and sales in both years
all_flavor_names1 = froyo_func.get_flavors(data_2016)
all_flavor_names2 = froyo_func.get_flavors(data_2016)
all_flavor_sales_2016 = froyo_func.get_sales(data_2016)
all_flavor_sales_2017 = froyo_func.get_sales(data_2017)

# prints the lists
print("The flavor names in 2016 and 2017 were:", all_flavor_names1)
print("The flavor sales in 2016 were:", all_flavor_sales_2016)
print("The flavor sales in 2017 were:", all_flavor_sales_2017)

# calculates the percent change of sales for each flavor from year 1 to year 2
pcnts = froyo_func.sales_percent_change(all_flavor_names1, all_flavor_sales_2016, all_flavor_sales_2017)
#REMOVEEEEEEEEEEEEEEEEEEBELOW+
print(pcnts)

# displays whether a flavor stock should be increased, decreased, or kept at the current rate based on the sales data
n = 0
for n in all_flavor_names2:
    n += 1
    current_flavor_check = all_flavor_names2.index()
    current_pcnt_check = pcnts.pop()
    froyo_func.inc_or_dec_check(current_pcnt_check, current_flavor_check)