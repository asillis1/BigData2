import os
import string
import pprint

def filler_words():
    """turn file of filler words into list of words"""
    f = open('folder_1/filler.txt')
    filler_words_list = []
    for line in f:
        word = line.strip()
        filler_words_list.append(word)
    return filler_words_list

def only_letters(word):
    """returns True only if string is only made out of letters or spaces. 
    Will use this to clean Reddit text before creating a histogram"""
    abecedary = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',' ']
    for letter in word:
        if letter not in abecedary:
            return False
    return True

def create_histogram(filename):
    """Creates a dictionary with the keys being every unique word in the Reddit posts and the values being their frequency"""
    filler_words_list = filler_words()
    hist = {}
    fp = open(filename, encoding='latin-1')
    strippables = string.punctuation + string.whitespace
    for line in fp:
        line = line.replace('-', ' ')
        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()
            if word not in filler_words_list and only_letters(word):
                hist[word] = hist.get(word, 0) + 1
    return hist

d = create_histogram('folder_1/post_text.txt')

def invert_dictionary(d):
    """Creates a dictionary with key value being the number of times a word appears in the Reddit posts and the value being a list of words
    that appear in the Reddit post with that frequency"""
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

def order_words_by_frequency(d):
    """Creates a list of the unique words in the Reddit posts ordered in descending order by frequency"""
    word_freq_list = []
    for word, freq in d.items():
        t = (freq, word)
        word_freq_list.append(t)
    sorted_list = sorted(word_freq_list,reverse=True)
    return sorted_list

def most_frequent_words(limit):
    """prints the most frequent words in the Reddit posts. The 'limit' parameter stands for how many 
    words will be printed. If limit = 10, then will print top 10 words"""
    word_freq_list = order_words_by_frequency(d)
    count = 0
    for pair in word_freq_list:
        print(pair)
        count += 1
        if count == limit:
            break

def main():
    reddit_file = 'folder_1/post_text.txt'
    #pprint.pprint(create_histogram(reddit_file)) #uncomment to print full histogram
    d = create_histogram(reddit_file)
    #pprint.pprint(invert_dictionary(d)) #uncomment to print full inverted histogram
    #pprint.pprint(order_words_by_frequency(d)) #uncomment to print full list of letters with their frequency
    top_words = 20
    pprint.pprint(most_frequent_words(top_words))

if __name__ == "__main__":
    main()