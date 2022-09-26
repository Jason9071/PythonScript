import random
import string

def get_random_string(length):
    letters = string.ascii_letters + string.punctuation + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def main() :
    words = []
    totalNumber = 5000
    i = 0
    while i < 5000 :
        words.append(get_random_string(random.randint(3, 6)))
        i = i + 1
        
    words_txt = "["
    f = open("words.txt", "w", encoding="utf-8")

    for word in words :
        words_txt = words_txt + '"' + word + '", '
        
    
    words_txt = words_txt[0:len(words_txt)-2]
    words_txt = words_txt + ']'

    f.write(words_txt)
    f.close()
    
    
main()