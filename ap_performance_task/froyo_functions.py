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