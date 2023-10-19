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
