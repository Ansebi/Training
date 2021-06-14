import random
the_20K_words = [i.split(';')[1] for i in open('./materials/russian_20K', 'r')]


def test():
    global x, right_answers, input_message    
    right_answer="test"
    right_answers=[right_answer]
    input_message="test: "
    x=input(input_message)

def adjective_endings():
    global x, right_answers, input_message, prompt
    
    nouns_genders_list=[]
    with open('./materials/russian_nouns.csv','r') as nouns_merged:
        for i in nouns_merged:
            nouns_genders_list.append(i)
    noun_w_gender=random.choice(nouns_genders_list)
    noun_w_gender=noun_w_gender.split(';')
    the_noun=noun_w_gender[0]
    the_gender=noun_w_gender[2]

    adjectives_list=[]
    with open('./materials/russian_adjectives.txt','r') as adjectives:
        for i in adjectives:
            adjectives_list.append(i)
    the_adjective=random.choice(adjectives_list)

    m_ending=the_adjective[-3:-1]
    f_ending='ая'
    n_ending='ое'
    p_ending='ые'
    
    if m_ending=='ий':
        if the_adjective[-4] in ['ж','ч']:
            f_ending='ья'
        else:
            if the_adjective[-4] not in ['к','г']:
                f_ending='яя'
                
    if m_ending=='ий':
        if the_adjective[-4] in ['ж','ч']:
            n_ending='ье'
        else:
            if the_adjective[-4]!='к':
                n_ending='ее'

    
    if the_adjective[-4] in ['ж','ч']:
        if m_ending=='ий':
            p_ending='ьи'
        p_ending='ие'
    else:
        if m_ending=='ий':
            p_ending='ие'

    if the_adjective[-4] in ['х','г']:
        p_ending='ие'
    
    test_mode='OFF'
    if test_mode=='ON':
        try:
            print(m_ending)
            print(f_ending)
            print(n_ending)
            print(p_ending)
            print('*'+the_adjective[-4]+'*')
        except:
            print('ERROR n2')
    
    if 'm' in the_gender:
        ending=m_ending
    elif 'f' in the_gender:
        ending=f_ending
    elif 'n' in the_gender:
        ending=n_ending
    elif 'p' in the_gender:
        ending=p_ending
    else:
        print(the_noun)
        print(the_gender)
        input('ERROR')
        
    
    input_message= the_noun+', '+the_adjective+'\n'
    right_answer=the_adjective[:-3]+ending+' '+the_noun
    right_answers=[right_answer]
    x=input(input_message)
    

def picture_vocabulary_250():
    global x, right_answers, input_message, prompt
    words=[]
    with open('./materials/250 words.csv','r') as words_csv:
        for i in words_csv:
            words.append(i)
            
    words=words[100:140]#limiter
    
    the_item=random.choice(words)
    the_item=the_item.split(';')
    eng_word=the_item[0]
    rus_word=the_item[1][:-1]
    input_message= eng_word+'\n'
    right_answer=rus_word
    right_answers=[right_answer]
    x=input(input_message)


def n_nn():
    global x, right_answers, input_message, prompt
    n_nn=open('./materials/n_nn.txt','r')
    n_nn_list=[]
    for i in n_nn:
        n_nn_list.append(i)
    a_word=random.choice(n_nn_list)    
    
    masked_word=a_word.replace('нн','...')
    masked_word=masked_word.replace('н','...')

    input_message=masked_word
    
    a_word=a_word.replace('\n','')

    right_answer=a_word
    right_answers=[right_answer]

    
    
def difficult_words():
    global right_answers, input_message, prompt
    difficult_words = []
    difficult_words_csv = open('./materials/difficult_words.csv','r')
    for i in difficult_words_csv:
        i=i.split(';')
        #i[1]=i[1][:-1]
        difficult_words.append(i)
    the_item=random.choice(difficult_words)
    #prompt='Translate to English:\n'
    input_message=the_item[1]+'\n'
    right_answer=the_item[0]
    right_answers=[right_answer]

def shuffle_letters():
    global right_answers, input_message, prompt
    okay = False
    while not okay:
        word = random.choice(the_20K_words)
        word_shuffled = list(word)
        random.shuffle(word_shuffled)
        word_shuffled = ''.join(word_shuffled)
        if word_shuffled != word:
            okay = True
    prompt='Буквы перемешали. Какое слово загадано?\n'
    input_message = word_shuffled + '\n'
    right_answer = word
    right_answers = [right_answer]


 
     

    

#lists***lists***lists***lists***lists***lists***lists***lists***
exercises_list=[
    "Test",
    #"Adjective endings",
    #"Picture Vocabulary 250"
    'Н и НН' ,
    'Мои сложные слова',
    'Перестановка букв (UNDER CONSTRUCTION)'
    ]

exercises_dictionary={
    "Test" : test,
    #"Adjective endings" : adjective_endings,
    #"Picture Vocabulary 250" : picture_vocabulary_250
    'Н и НН' : n_nn,
    'Мои сложные слова' : difficult_words,
    'Перестановка букв (UNDER CONSTRUCTION)' : shuffle_letters
    }
    
