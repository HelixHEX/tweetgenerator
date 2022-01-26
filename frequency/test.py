list_string = ['maNgo', 'BanAna', 'PytHoN iS Love', 'Cat iS not doG']

correct_case = [str.upper(word[0])+str.lower(word[1:])
                for word in sum([sentence.split() for sentence in list_string], [])
                if len(word) > 1]

# print the list of word with desired case
print(correct_case)