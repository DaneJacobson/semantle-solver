import gensim.downloader
import gensim.models
import os
import random
import re
import sys

if os.path.exists('word2vec.wordvectors'):
    word_vectors = gensim.models.KeyedVectors.load('word2vec.wordvectors')
else:
    word_vectors = gensim.downloader.load('word2vec-google-news-300')
    word_vectors.save('word2vec.wordvectors')

manual_input = sys.argv[1]
if manual_input == 'manual':
    legit_target = False
    while not legit_target:
        target_word = input('What is the target word for this round? ')
        if target_word not in word_vectors.index_to_key:
            print('Not a word in the dataset, try again.')
        else:
            legit_target = True
elif manual_input == 'automatic':
    while True:
        target_word = random.sample(word_vectors.index_to_key, 1)[0]
        if re.search('^[\w\s]+$', target_word):
            if '_' not in target_word and not target_word[:1].isupper():
                print('The target word is %s' % target_word)
                break

user_guesses = []
while True:
    user_guess = input('What is your next guess? ')
    user_guesses.append(user_guess)
    if user_guess == target_word:
        print('You found the answer!')
        print('Guesses: ' + str(user_guesses))
        print('Game over')
        break
    sim_userword_targetword = word_vectors.similarity(user_guess, target_word)
    print('Distance from your guess to the target word: %f' % (100 * round(sim_userword_targetword, 4)))

# print(user_guesses)