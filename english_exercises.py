import random

the_20k = open('./materials/20k_words_dictionary', 'r')


def g():
    pass


g.the_20k_list = list(the_20k)


def get_random_word(limit):
    dictionary = g.the_20k_list[:limit]
    random_word = random.choice(dictionary)[:-1]
    return random_word


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
    with open('./materials/irregular_verbs.csv', 'r') as irregular_verbs_csv:
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
    sentences = open('./materials/sentences.csv', 'r')
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
    with open('./materials/vocabulary.csv', 'r') as vocabulary_csv:
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
