import froyo_functions as froyo_func

data_2016 = "ap_performance_task/2016_sales_data"
data_2017 = "ap_performance_task/2016_sales_data"

flavor_names_2016 = froyo_func.get_flavors(data_2016)
flavor_sales_2016 = froyo_func.get_sales(data_2016)

print("The flavor names in 2016 were:", flavor_names_2016)
print("The flavor sales in 2016 were:", flavor_sales_2016)