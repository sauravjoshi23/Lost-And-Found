import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import string
from nltk.corpus import stopwords
from nltk import word_tokenize

def similarity_check(description, data):

    answers = []

    print('Data in Similarity Check: ', data)

    for i in range(len(data)):
        dict1 = {}
        x = description
        y = data[i]['item_description']

        regular_punct = list(string.punctuation)
        def remove_punctuation(text,punct_list):
            for punc in punct_list:
                if punc in text:
                    text = text.replace(punc, ' ')
            return text.strip()

        # word_tokenize, punctuations, stopwords
        text = remove_punctuation(x ,regular_punct)
        text = word_tokenize(text)
        words=[word.lower() for word in text if word.isalpha()]
        stop_words = set(stopwords.words('english'))
        filtered_sentence = [w for w in words if not w in stop_words]
        x = ' '.join(filtered_sentence)
        x = [x]

        # word_tokenize, punctuations, stopwords
        text = remove_punctuation(y ,regular_punct)
        text = word_tokenize(text)
        words=[word.lower() for word in text if word.isalpha()]
        stop_words = set(stopwords.words('english'))
        filtered_sentence2 = [w for w in words if not w in stop_words]
        y = ' '.join(filtered_sentence2)
        y= [y]

        from sklearn.feature_extraction.text import TfidfVectorizer
        vect = TfidfVectorizer()
        a = vect.fit_transform(x)
        b = vect.transform(y)

        score = cosine_similarity(a, b)

        dict1['category_name'] = data[i]['category_name']
        dict1['item_name'] = data[i]['item_name']
        dict1['item_description'] = data[i]['item_description']
        dict1['founder_name'] = data[i]['founder_name']
        dict1['founder_number'] = data[i]['founder_number']
        print(score)
        if score >= 0.3:
            answers.append(dict1)

    return answers