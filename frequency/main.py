import sys, time, string, re
# PUNCTUATION = '''!()-[]{};:'"\…,—’‘<>./?@#$%‼^&*_~”„“‥'''
punc = '''!"#$%&'()…*+,-./:;<=>?@[\]^—_`{|}~'''

def histogram(file_name):
    words_list = []
    with open(file_name) as f:
        for line in f:
            words_list += line.translate(str.maketrans('', '', punc)).lower().split()
        print(words_list)
    hist = []
    words_list.sort()
    pointer = 0
    for word in words_list:
        if pointer != 0 and hist[pointer-1][0] == word:
            hist[pointer-1][1] += 1
        else:
            hist.append([word, 1])
            pointer += 1
    return hist

def frequency(word, histogram):
    for list in histogram:
        if list[0] == word:
            return f"{word}: {list[1]}" 

def unique(histogram):
    return len(histogram)

if __name__ == '__main__':
    start_time = time.time()
    hist = histogram('./text.txt')
    end_time = time.time()
    # print(hist)
    print(f"Histogram created in: {(end_time-start_time) * 1000}")
    

    # start_time = time.time()
    # freq = frequency('gatsby', hist)
    # end_time = time.time()
    # print(freq)
    # print(f"Frequency created in: {(end_time-start_time) * 1000}")

    start_time = time.time()
    uniq = unique(hist)
    end_time = time.time()
    print(uniq)
    print(f"Unique created in: {(end_time-start_time) * 1000}")