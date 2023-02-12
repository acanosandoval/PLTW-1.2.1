def monitor():
  try:
    
    val1 = 12
    val2 = 17

    alkilines = list(range(val1, val2+1))
    print(alkilines)

    current = get_alkalinity()
    mesg = "Alkalinity OK"

    if (current < alkilines[0]):
      mesg = "Alkalinity too low!"
    elif (current > alkilines[5]):
      mesg = "Alkalinity too high!"
    
  except:
    print("Unexpected alkalinity error") 
    
  return mesg

# Function to simulate actual fish tank monitoring
def get_alkalinity():
  return 15