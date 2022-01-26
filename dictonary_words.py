import random, sys, time

def dictionary_words():
    start_time = time.time()
    sentence = ''
    user_num = int(sys.argv[1])
    file = open('/usr/share/dict/words')
    content = file.readlines()
    # print(len(content))
    for i in range(user_num):
        ranum = random.randint(0, len(content)-1)
        sentence += content[ranum].strip()
    
    
    # print(sentence)
    end_time = time.time()
    print(f"Code completed in: {end_time-start_time}")

if __name__ == '__main__':
    dictionary_words()