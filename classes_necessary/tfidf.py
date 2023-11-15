import numpy as np


class CountVectorizer:
    def __init__(self):
        self.word_count = {}

    def fit_transform(self, text):
        for line in text:
            line = line.lower()
            words = line.split()
            for word in words:
                if word in self.word_count:
                    self.word_count[word] += 1
                else:
                    self.word_count[word] = 1

        result = []
        for line in text:
            line = line.lower()
            words = line.split()
            line_count = []
            for word in self.word_count:
                count = words.count(word)
                line_count.append(count)
            result.append(line_count)

        return result

    def get_feature_names(self):
        return list(self.word_count.keys())

    def tf_transform(count_matrix):
        row_sums = np.sum(count_matrix, axis=1)
        tf_matrix = count_matrix / row_sums[:, None]
        return np.round(tf_matrix, 3)

    def idf_transform(count_matrix):
        num_docs = len(count_matrix)
        doc_freq = np.where(count_matrix > 0, 1, 0)
        doc_freq = np.sum(doc_freq, axis=0)
        idf_matrix = np.log((1 + num_docs) / (1 + doc_freq)) + 1
        return np.round(idf_matrix, 1)


class TfidfTransformer:
    def __init__(self):
        self.idf_ = None

    def fit_transform(self, count_matrix):
        count_matrix = np.array(count_matrix, dtype=np.float64)

        tf = CountVectorizer.tf_transform(count_matrix)
        idf = CountVectorizer.idf_transform(count_matrix)

        self.idf_ = idf

        tfidf_matrix = np.round(tf * idf, 3)

        return tfidf_matrix


class TfidfVectorizer(CountVectorizer):
    def __init__(self):
        super().__init__()
        self.tfidf_transformer = TfidfTransformer()

    def fit_transform(self, corpus):
        count_matrix = super().fit_transform(corpus)

        tfidf_matrix = self.tfidf_transformer.fit_transform(count_matrix)

        return tfidf_matrix
