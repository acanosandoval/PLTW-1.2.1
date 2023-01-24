# Module pwalgorithms

# get words from password dictionary file
def get_dictionary():
  words = []
  dictionary_file = open("c:/Users/acanosandoval/Documents/Comp Sci Python/PLTW-CompSci/a213/dictionary.txt")
  for line in dictionary_file:
    # store word, omitting trailing new-line
    words.append(line[:-1])
  dictionary_file.close()
  return words

# analyze a one-word password
def one_word(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    guesses += 1
    if (w == password):
      return True, guesses
  return False, guesses

# analyze a two-word password
def two_word(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w1 in words:
    for w2 in words:
        phrase = w1 + w2
        print("Guessing...", phrase)
        guesses = guesses + 1
        if (phrase == password):
            return True, guesses
  return False, guesses

def two_words_and_digit(password):
  words = get_dictionary()
  nums = "1234567890"
  guesses = 0
  # get each word from the dictionary file
  for w1 in words:
    for w2 in words:
        for d1 in nums:
          for d2 in nums:
            print("Guessing...", phrase)
          phrase = d1 + w1 + w2 + d2
      guesses +=  1
      if (phrase == password):
        return True, guesses
  return False, guesses