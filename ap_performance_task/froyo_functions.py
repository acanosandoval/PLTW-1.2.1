# gets the flavor names from a text file
def get_flavors(file_name):
  sales_file = open(file_name, "r")

  flavors = []
  for line in sales_file:
    flavor_name = ""
    index = 0

    # gets the name of the flavor up until colon of each line
    while (line[index] != ":"):
      flavor_name = flavor_name + line[index] 
      index = index + 1
    
    # adds the name of that flavor to the flavors list
    flavors.append(flavor_name)

  sales_file.close()

  return flavors

# gets the sales from a text file
def get_sales(file_name):
  sales_file = open(file_name, "r")

  sales = []
  for line in sales_file:
    flavor_sales = ""
    index = 0

    # skips the text until the colon
    while (line[index] != ":"):
      index = index + 1
    index = index + 1
    
    # gets the sales of the flavor
    while (line[index] != "\n"):
      flavor_sales = flavor_sales + line[index]
      index = index + 1

    # adds the sales of that flavor to the sales list
    sales.append(int(flavor_sales))
   
  sales_file.close()

  return sales

# finds the percent change in sales of each flavor between two years
def sales_percent_change(names, year1_sales, year2_sales):
  pcnt_list = []
  while len(names) > 0:
    single_flavor = names.pop()
    single_flavor_year1_sales = year1_sales.pop()
    single_flavor_year2_sales = year2_sales.pop()
    pcnt_change = int(((single_flavor_year2_sales/single_flavor_year1_sales)*100)-100)
    pcnt_list.append(pcnt_change)
    print("The percent change for", single_flavor, "is", pcnt_change,"%")
  return pcnt_list

# evaluates the flavor's change in sales as an increase or decrease
def inc_or_dec_check(pcnt_chnge, name):
  if pcnt_chnge > 20:
    print("Increase your stock of", name, "frozen yogurt.")
  elif pcnt_chnge < -20:
    print("Decrease your stock of", name, "frozen yogurt.")
  else:
    print("Keep the current stock of", name, "frozen yogurt.")