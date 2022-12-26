import random

text = './news.txt'
f = open(text, "r")
print(f.read())


def hammer_pickOneMemeber():
    '''example function'''

    teamJDE = ['hammer', 'billy', 'chistina']
    result = random.sample(teamJDE, 1)
    return result


if __name__ == "__main__":
    print(hammer_pickOneMemeber())
    # print(taskOne())
    # print(taskTwo())
    # print(taskThree())
    # print(taskFour())

    # Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)
    print("a", (f2.count("a")))
    print("e", (f2.count("e")))
    print("i", (f2.count("i")))
    print("o", (f2.count("o")))
    print("u", (f2.count("u")))

    taskone = f2.count("a") + f2.count("e") + f2.count("i") + f2.count("o") + f2.count("u")
    print(taskone)

    # Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz
    def taskthree(text,n):
      ans = ""
      for i in range(len(text)):
        ch = text[i]
        
        if ch==" ":
        ans+=" " 
        elif (ch.isupper()):
        ans += chr((ord(ch) + n-65) % 26 + 65)
        else:
        ans += chr((ord(ch) + n-97) % 26 + 97)
      return ans

    text = "I am a boy"
    n = 1
    print(taskthree(text,n))

    # Task-3 - Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I
    taskthree = 'I am a boy'
    print(taskthree[::-1])
    # Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob
    def rw(t4):
      return ' '.join(word[::-1] for word in t4.split())
    t4 = 'I am a boy'
    print(rw(t4))