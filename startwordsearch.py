import json
import gensim.downloader
import gensim.models
import re
import sys
import os

def wordsearch(startwords_dict: dict, starting_index: int):
    if os.path.exists('word2vec.wordvectors'):
        word_vectors = gensim.models.KeyedVectors.load('word2vec.wordvectors')
    else:
        word_vectors = gensim.downloader.load('word2vec-google-news-300')
        word_vectors.save('word2vec.wordvectors')

    candidate_words = []
    for word in word_vectors.index_to_key:
        if re.search('^[A-Za-z]+$', word):
            if '_' not in word and not word[:1].isupper():
                candidate_words.append(word)

    n = len(candidate_words)
    print(n)
    for index in range(starting_index, n):
        sample_word = candidate_words[index]
        print('Running distribution computations for %s, %f percent complete' % (
            sample_word, 
            (index / n * 100))
        )

        if sample_word not in startwords_dict:
            score_to_word = {}
            for search_word in candidate_words:
                similarity_score = round(float(word_vectors.similarity(sample_word, search_word)), 4)
                if similarity_score in score_to_word:
                    score_to_word[similarity_score].append(search_word)
                else:
                    score_to_word[similarity_score] = [search_word]

            variability_sum = 0.0
            size_list = [len(word_list) for _, word_list in score_to_word.items()]
            for i in range(len(size_list) - 1):
                for j in range(i + 1, len(size_list)):
                    variability_sum += (size_list[i] - size_list[j]) ** 2

            startwords_dict[sample_word] = variability_sum

            if index % 100 == 0:
                print('Saving words %d:%d to startwords.json' % (starting_index, index))
                print(index)
                with open('startwords.json', 'w') as f:
                    json.dump(startwords_dict, f)
            index += 1

if __name__ == "__main__":
    with open('startwords.json') as f:
        startwords_dict = json.load(f)
    wordsearch(startwords_dict=startwords_dict, starting_index=int(sys.argv[1]))