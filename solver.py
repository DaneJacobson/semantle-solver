import gensim.downloader
import gensim.models
import os
import re
    
STARTWORD = 'viscous'
if os.path.exists('word2vec.wordvectors'):
    word_vectors = gensim.models.KeyedVectors.load('word2vec.wordvectors')
else:
    word_vectors = gensim.downloader.load('word2vec-google-news-300')
    word_vectors.save('word2vec.wordvectors')


# Prepping dataset specifically for semantle.com filtering 
# (single word, alphanumeric, and with first character potentially capitalized)
candidate_words = []
for word in word_vectors.index_to_key:
    if re.search('^[A-Za-z]+$', word):
        if '_' not in word and not word[:1].isupper():
            candidate_words.append(word)

base_word = STARTWORD
while True:
    score_to_word = {}
    for search_word in candidate_words:
        similarity_score = round(float(word_vectors.similarity(base_word, search_word)), 4)
        if similarity_score in score_to_word:
            score_to_word[similarity_score].append(search_word)
        else:
            score_to_word[similarity_score] = [search_word]
    
    baseword_to_target_sim = round(float(input('What is the similarity score for: %s ' % (base_word))) / 100, 4)
    candidate_words = score_to_word[baseword_to_target_sim]
    if len(candidate_words) == 1:
        print('The answer is: %s' % candidate_words[0])
        break
    base_word = candidate_words[0]