import sys, time
PUNCTUATION = '''!()-[]{};:'"\…,’‘<>.—o—/?@#$%‼^&*_~”„“‥\n'''

def histogram(file_name):
    words_list = []
    with open(file_name) as f:
        for line in f:
            current_line = ''
            for character in line:
                if character not in PUNCTUATION:
                    current_line += character
            words_list += current_line.lower().split()
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

if __name__ == '__main__':
    start_time = time.time()
    hist = histogram('./text.txt')
    end_time = time.time()
    print(hist)
    print(f"Histogram created in: {(end_time-start_time) * 1000}")
    start_time = time.time()
    freq = frequency('gatsby', hist)
    end_time = time.time()
    print(freq)
    print(f"Frequency created in: {(end_time-start_time) * 1000}")