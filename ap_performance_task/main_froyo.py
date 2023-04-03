import froyo_functions as froyo_func

# import the data
data_2016 = "ap_performance_task/2016_sales_data"
data_2017 = "ap_performance_task/2017_sales_data"

# creates separate lists for flavor names and sales in both years
all_flavor_names = froyo_func.get_flavors(data_2016)
all_flavor_sales_2016 = froyo_func.get_sales(data_2016)
all_flavor_sales_2017 = froyo_func.get_sales(data_2017)

# prints the lists
print("The flavor names in 2016 and 2017 were:", all_flavor_names)
print("The flavor sales in 2016 were:", all_flavor_sales_2016)
print("The flavor sales in 2017 were:", all_flavor_sales_2017)

# calculates the percent change of sales for each flavor from year 1 to year 2
froyo_func.sales_percent_change(all_flavor_names, all_flavor_sales_2016, all_flavor_sales_2017)