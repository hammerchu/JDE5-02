import random

text = './news.txt'
f = open(text, "r")
print(f.read())


def hammer_pickOneMemeber():
    '''example function'''

    teamJDE = ['hammer', 'billy', 'chistina']
    result = random.sample(teamJDE, 1)
    return result
    
def taskTwo():
  text = './news.txt'
  f = open(text, "r")
  txt = f.read()
  
  new_txt = ""

  for char in txt: 
    if not char.isalpha(): 
        new_txt = new_txt + char
    elif char.isupper():
        new_txt = new_txt + chr((ord(char) + 1 - 65) % 26 + 65) # for uppercase Z
    else:
        new_txt = new_txt + chr((ord(char) + 1 - 97) % 26 + 97) # for lowercase z
    

  return (new_txt)
    
if __name__ == "__main__":
    print(hammer_pickOneMemeber())
    # print(taskOne())
    print(taskTwo())
    # print(taskThree())
    # print(taskFour())

    # Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)
    
    # Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz

    # Task-3 - Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I

    # Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob

