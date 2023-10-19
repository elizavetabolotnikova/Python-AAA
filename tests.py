from CountVectorizer import *

corpus = [
    'Crock Pot Pasta Never boil pasta again',
    'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]
vectorizer = CountVectorizer()
count_matrix = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
print(count_matrix)

corpus = [
    '1 2 2 5',
    'testing more than 2 rows and numbers',
    'testing more than 2 rows and numbers',
    'testing more than 2 rows and numbers',
    'testing more than 2 rows and numbers'
]
vectorizer = CountVectorizer()
count_matrix = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
print(count_matrix)

corpus = [
    '',
    'test'
]
vectorizer = CountVectorizer()
count_matrix = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
print(count_matrix)
