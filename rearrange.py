import random
import sys 

def rearrange(random_words):
    random.shuffle(random_words)
    return random_words

if __name__ == '__main__':
    user_words = sys.args[1:]
    shuffled_words = rearrange(user_words)
    result = ''
    for word in user_words:
        result += user_words + ' '
        
    print (result)