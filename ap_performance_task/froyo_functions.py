# gets the sales from a text file
def get_sales(file_name):
  sales_file = open(file_name, "r")

  sales = []
  for line in sales_file:
    leader_score = ""
    index = 0

    # skips the text until the colon
    while (line[index] != ":"):
      index = index + 1
    index = index + 1
    
    # gets the sales of the flavor
    while (line[index] != "\n"):
      leader_score = leader_score + line[index] 
      index = index + 1

    # adds the sales of that flavor to the sales list
    sales.append(int(leader_score))
   
  sales_file.close()

  return sales