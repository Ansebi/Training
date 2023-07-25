import re
# the_20K_words = [i.split(';')[1] for i in open('./materials/russian_20K', 'r')]
the_20K_words = [i.replace('\n', '') for i in open('./materials/20k_words_dictionary', 'r')]

pattern = input('Pattern: ')
banned = input('Banned letters: ')
included = input('Must include: ')
for word in the_20K_words:
    if re.match(pattern, word):
        if len(word) == 5:
            banned_okay = True
            for i in banned:
                if i in word:
                    banned_okay = False
            included_okay = True
            for i in included:
                if i not in word:
                    included_okay = False
            okay = banned_okay and included_okay
            if okay:
                print(word)
input('Finished')                

