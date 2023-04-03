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


while len(all_flavor_names) > 0:
  single_flavor = all_flavor_names.pop()
  single_flavor_sales_2016 = all_flavor_sales_2016.pop()
  single_flavor_sales_2017 = all_flavor_sales_2017.pop()
  pcnt_change = int(((single_flavor_sales_2017/single_flavor_sales_2016)*100)-100)
  print("The percent change from 2016 to 2017 for", single_flavor, "is", pcnt_change,"%")
