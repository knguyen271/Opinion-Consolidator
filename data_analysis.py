from textblob import TextBlob
from collections import Counter
import nltk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

def getPolarity(text):
    return round(TextBlob(text).polarity, 2)

def getSubjective(text):
    return TextBlob(text).subjectivity

def get_common(comments):
    combined_text = "".join(comments)
    words = combined_text.split()
    word_count = Counter(words)
    most_common, frequency = word_count.most_common(1)[0]
    common = []
    common.append(most_common)
    common.append(frequency)
    return common

def get_average(values):
    total = 0
    for value in values:
        total = total + value
    
    return round((total / len(values)), 2)

def sorter(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2] 
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return sorter(left) + middle + sorter(right)
    
    
def get_frequency(comments):
    all_words =  []
    for comment in comments:
        words = nltk.word_tokenize(comment)
        all_words.extend(words)

    nlp_words = nltk.FreqDist(all_words)
    plot1 = nlp_words.plot(20, color='salmon', title='Word Frequency')
    plt.show()