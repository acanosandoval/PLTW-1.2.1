import froyo_functions as froyo_func

# imports the data from the text files
data_2016 = "ap_performance_task/2016_sales_data"
data_2017 = "ap_performance_task/2017_sales_data"

# creates list for flavor names that will be edited in the code
all_flavor_names = froyo_func.get_flavors(data_2016)
# create a permanent list for flavor names that will not be edited in the code
all_flavor_names_perm = froyo_func.get_flavors(data_2016)
# gets the sales data for each flavor from each file
all_flavor_sales_2016 = froyo_func.get_sales(data_2016)
all_flavor_sales_2017 = froyo_func.get_sales(data_2017)

# calculates the percent change of sales for each flavor from year 1 to year 2
pcnts = froyo_func.sales_percent_change(all_flavor_names, all_flavor_sales_2016, all_flavor_sales_2017)

# displays whether a flavor stock should be increased, decreased, or kept at the current rate based on the sales data
all_flavor_names = froyo_func.get_flavors(data_2016)
for n in all_flavor_names_perm:
    current_flavor_check = all_flavor_names.pop()
    current_pcnt_check = pcnts.pop()
    froyo_func.inc_or_dec_check(current_pcnt_check, current_flavor_check)