s='panashe'

#Dictionary experiment
dict={}
for letter in s:
    if letter not in dict:
        dict[letter]=1
    else:
        dict[letter]+=1

dict

word_list=[]
word_dict={}

def first_non_repeating_letter(s):
    for letter in s:
        if letter not in word_list:
            word_dict[letter]=1
            word_list.append(letter)
        elif letter in word_dict:
            word_dict[letter]+=1

    for letter in word_list:
        if word_dict[letter]==1:
            return letter

first_non_repeating_letter(s)













