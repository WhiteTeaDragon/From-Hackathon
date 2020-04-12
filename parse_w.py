from wikipedia import Wikipedia
from wiki2plain import Wiki2Plain
import urllib.parse


strange_words = ["music award", "золотой граммофон", "дебют года", "Comedy Club"]


def find_name(link):
    i = len(link) - 1
    while i >= 0 and link[i] != '/':
        i -= 1
    return link[i + 1:]


def find_lang(link):
    ind = link.find(".wikipedia.org")
    #print(ind)
    j = ind
    while j >= 0 and link[j] != '/':
        j -= 1
    return link[j + 1:ind]


def change_name(name, lang):
    names = name.split('_')
    if lang == 'en':
        return ' '.join(names)
    elif lang == 'ru':
        for i in range(len(names)):
            if names[i][-1] == ',':
                names[i] = names[i][:-1]
        return ' '.join(names[:2])


def there_are_letters(str):
    for i in range(len(str)):
        if str[i].isalpha:
            #print(str[i], str[i].isalpha())
            return True


def without_strange_words(str, name):
    copy = str.lower()
    if copy.find(name.lower()) != -1:
        return False
    for i in range(len(strange_words)):
        if copy.find(strange_words[i].lower()) != -1:
            return False
    return True


dict_signs = {"en" : ('"', '"'), "ru" : ('«', '»')}
link = "https://en.wikipedia.org/wiki/Category:British_songwriters"
link = urllib.parse.unquote(link)
print(link)
lang = find_lang(link)
print(lang)
wiki = Wikipedia(lang)

try:
    print("trying")
    name = find_name(link)
    print(name)
    raw = wiki.article(name)
    #true_name = change_name(name, lang)
except:
    print("exception")
    raw = None

if raw:
    wiki2plain = Wiki2Plain(raw)
    content = wiki2plain.text
    #print(content)
    names = []
    i = 0
    #while i < len(content):
    #    if content[i] == dict_signs[lang][0] and i + 1 < len(content) and content[i + 1].isalpha():
    #        j = i + 1
    #        while j < len(content) and content[j] != dict_signs[lang][1]:
    #            j += 1
    #        curr = content[i + 1:j]
    #        if len(curr) < 50 and len(curr) > 1 and there_are_letters(curr) and curr[0].isalpha() and without_strange_words(curr, true_name) and curr[0].isupper():
    #            if curr[0] == "Г":
    #                print(curr, 
    #            names.append(curr)
    #        i = j
    #    i += 1
    #print("Artist:", true_name)
    #names = list(set(names))
    #for i in range(len(names)):
    #    print(names[i])
    result = open('result.txt','w', encoding='utf-8')
    print(content, file=result)
    result.close()