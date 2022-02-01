import sys
import time
import string
import re
# PUNCTUATION = '''!()-[]{};:'"\…,—’‘<>./?@#$%‼^&*_~”„“‥'''
punc = '''!"#$%&'()…*+,-./:;<=>?@[\]^—_`{|}~'''

# def create_list(file):
#     words = []
#     for line in file:
#         words += line.translate(str.maketrans('', '', punc)).lower().split()


def histogram(file_name):
    file_s_time = time.time()
    words_list = []
    with open(file_name) as f:
        for line in f:
            words_list += line.translate(str.maketrans('','', punc)).lower().split()
    file_e_time = time.time()
    hist_s_time = time.time()
    
    hist = []
    words_list.sort()
    pointer = 0
    count = 0
    for word in words_list:
        if pointer != 0 and hist[pointer-1][0] == word:
            hist[pointer-1][1] += 1
            count += 1
        else:
            hist.append([word, 1])
            pointer += 1
            count += 1
    hist_e_time = time.time()
    file_time = (file_e_time - file_s_time) 
    hist_time = (hist_e_time - hist_s_time) 
    return {"hist": hist, "file_time": file_time, "hist_time": hist_time, "count": count}


def frequency(word, histogram):
    for list in histogram:
        if list[0] == word:
            return f"{word}: {list[1]}"


def unique(histogram):
    return len(histogram)


if __name__ == '__main__':
    start_time = time.time()
    res = histogram('./text.txt')
    end_time = time.time()
    print(res['hist'])
    print(f"Stats: file - {res['file_time']} | hist - {res['hist_time']}")
    print(f"Histogram created in: {(end_time-start_time) }")

    start_time = time.time()
    freq = frequency('gatsby', res['hist'])
    end_time = time.time()
    print(freq)
    print(f"Frequency created in: {(end_time-start_time) }")

    start_time = time.time()
    uniq = unique(res['hist'])
    end_time = time.time()
    print(uniq)
    print(f"Unique created in: {(end_time-start_time) }")
