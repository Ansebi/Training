import random
import json
import pandas as pd


MATERIALS_FOLDER = './materials'
THE_20K = list(open(f'{MATERIALS_FOLDER}/20k_words_dictionary'))

SYNONYMS_FILENAME = 'en_thesaurus.jsonl'
FREQUENCY_FILENAME = 'unigram_freq.csv'
SYNONYMS_MIN_WORD_LEN = 7
FREQUENCY_FLOOR = 5000



synonyms_path = f'{MATERIALS_FOLDER}/{SYNONYMS_FILENAME}'
frequency_path = f'{MATERIALS_FOLDER}/{FREQUENCY_FILENAME}'
synonyms_entry_list = [json.loads(entry) for entry in open(synonyms_path)]
df_frequency = pd.read_csv(frequency_path)
synonyms_dict = {}
for n, entry in enumerate(synonyms_entry_list):
    word = entry['word']
    pos = entry['pos']
    synonyms = entry['synonyms']
    if word in synonyms_dict:
        synonyms_dict[word]['synonyms'].extend(synonyms)
        synonyms_dict[word]['pos'].append(pos)
        synonyms_dict[word]['pos'] = list(set(synonyms_dict[word]['pos']))
    else:
        synonyms_dict[word] = {
            'pos': [pos],
            'synonyms': synonyms
        }

frequent_words = df_frequency[:FREQUENCY_FLOOR]['word'].astype(str)
frequent_words = [word for word in frequent_words if len(word) >= SYNONYMS_MIN_WORD_LEN]
frequent_synonyms = [word for word in frequent_words if word in synonyms_dict]


def get_random_word(limit, words=THE_20K):
    return random.choice(words[:limit])[:-1]


def augmenter(word):
    selector = random.randint(0, 11)
    endings = ['ing', "'s", "'ll", "ed", "'m", 'es']
    endings += ["'s", "'s", "'s"]

    if selector in range(0, 3):
        word += random.choice(endings)
    elif selector in range(4, 9):
        word = word.capitalize()
    elif selector == 9:
        word = word.capitalize()
        word += random.choice(endings)
    else:
        pass
    return word


def test(difficulty: int):
    input('Test')


def irregular_verbs(difficulty: int):
    right_answers, input_message, prompt = None, None, None
    irregular_verbs = []
    with open(f'{MATERIALS_FOLDER}/irregular_verbs.csv') as irregular_verbs_csv:
        for i in irregular_verbs_csv:
            i = i.split(';')
            i[2] = i[2][:-1]
            irregular_verbs.append(i)
        irregular_verbs_csv.close()
    the_item = random.choice(irregular_verbs)
    input_message = 'I ' + the_item[0] + '\n'
    input_message += 'Yesterday I '
    right_answer = the_item[1]
    right_answers = [right_answer]
    return right_answers, input_message, prompt


def missing_words(difficulty: int):
    right_answers, input_message, prompt = None, None, None
    alphabet = "abcdefghijklmnopqrstuvwxyz'ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sentences_list = []
    sentences = open(f'{MATERIALS_FOLDER}/sentences.csv')
    for i in sentences:
        if i != '\n':
            sentences_list.append(i[:-1])

    the_sentence = random.choice(sentences_list)
    the_sentence = the_sentence.split(' ')
    blank_n = random.randint(0, len(the_sentence) - 1)
    right_answer = the_sentence[blank_n]

    the_dots = '...'
    for i in right_answer:
        if i not in alphabet:
            the_dots += i

    right_answer_holder = ''
    for i in right_answer:
        if i in alphabet:
            right_answer_holder += i
    right_answer = right_answer_holder

    the_sentence[blank_n] = the_dots
    the_sentence = ' '.join(the_sentence)
    the_options = [right_answer]
    for i in range(5):
        limit = random.choice([2000, 10000])
        random_word = get_random_word(limit)
        augmented_word = augmenter(random_word)
        the_options.append(augmented_word)
    random.shuffle(the_options)
    input_message = the_sentence
    input_message += '\n' * 2
    for i in the_options:
        input_message += i + '\n'
    input_message += '\n'
    right_answers = [right_answer]
    return right_answers, input_message, prompt


def vocabulary(difficulty: int):
    right_answers, input_message, prompt = None, None, None
    vocabulary = []
    with open(f'{MATERIALS_FOLDER}/vocabulary.csv') as vocabulary_csv:
        for i in vocabulary_csv:
            i = i.split(';')
            i[1] = i[1][:-1]
            vocabulary.append(i)
        vocabulary_csv.close()
    the_item = random.choice(vocabulary)
    prompt = 'Translate to English:\n'
    input_message = the_item[1] + '\n'
    right_answer = the_item[0]
    right_answers = [right_answer]
    return right_answers, input_message, prompt


def synonyms(difficulty: int):
    right_answers, input_message, prompt = None, None, None  
    word = random.choice(frequent_synonyms)
    word_synonyms = synonyms_dict[word]['synonyms']
    prompt = 'Give a synonym for the following word:'
    right_answers = word_synonyms
    input_message = f'{word}: '
    return right_answers, input_message, prompt