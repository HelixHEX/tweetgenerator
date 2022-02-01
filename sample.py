import random, sys, time
from histogram import histogram

def sample(hist, count):
  ranum = random.randint(0, count)
  index = 0
  for word_list in hist:
    index += word_list[1]
    if index >= ranum:
      return word_list[0]
  return "error"

      


if __name__ == '__main__':
  debug = True
  file = sys.argv[1]
  hist_result = histogram(file)
  hist = hist_result['hist']
  count = hist_result['count']
  if not debug:
    start_time = time.time()
    sample_result = sample(hist, count)
    end_time = time.time()
    print(sample_result)
    print(f"Code completed in: {(end_time-start_time) }")
  else:
    print('---------------------------')
    words = []
    word = ''
    start_time = time.time()
    for i in range(100000):
      sample_result = sample(hist, count)
      word = sample_result
      words.append([word])
    end_time = time.time() 
    print(words)
    print(word)
    print(f"Code completed in: {(end_time-start_time) }")
   

    
