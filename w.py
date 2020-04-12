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
#For Wikipedia
#print("hello")
link = "https://en.wikipedia.org/wiki/Ray_Charles"
#link = "https://en.wikipedia.org/wiki/Yuri_Shatunov"
#link = "https://en.wikipedia.org/wiki/Nat_King_Cole"
#link = "https://en.wikipedia.org/wiki/Illinois_Jacquet"
#link = "https://en.wikipedia.org/wiki/Arthur_Alexander"
#link = "https://en.wikipedia.org/wiki/Jimmie_Allen"
#link = "https://en.wikipedia.org/wiki/DeFord_Bailey"
#link = "https://en.wikipedia.org/wiki/Cuje_Bertram"
#link = "https://en.wikipedia.org/wiki/Clarence_%22Gatemouth%22_Brown"
#link = "https://ru.wikipedia.org/wiki/%D0%A0%D1%8D%D0%B9_%D0%A7%D0%B0%D1%80%D0%BB%D1%8C%D0%B7"
#link = "https://ru.wikipedia.org/wiki/%D0%A8%D0%B0%D1%82%D1%83%D0%BD%D0%BE%D0%B2,_%D0%AE%D1%80%D0%B8%D0%B9_%D0%92%D0%B0%D1%81%D0%B8%D0%BB%D1%8C%D0%B5%D0%B2%D0%B8%D1%87"
#link = "https://ru.wikipedia.org/wiki/%D0%90%D0%B1%D0%B4%D1%8E%D1%88%D0%B5%D0%B2,_%D0%9D%D0%B8%D1%8F%D0%B7_%D0%9C%D0%B0%D0%BD%D1%81%D1%83%D1%80%D0%BE%D0%B2%D0%B8%D1%87"
#link = "https://ru.wikipedia.org/wiki/%D0%90%D0%BD%D0%B0%D1%81%D1%82%D0%B0%D1%81%D0%B8%D1%8F_(%D0%BF%D0%B5%D0%B2%D0%B8%D1%86%D0%B0)"
#link = "https://ru.wikipedia.org/wiki/%D0%94%D0%B5%D1%86%D0%BB"
#link = "https://ru.wikipedia.org/wiki/%D0%92%D1%8B%D1%81%D0%BE%D1%86%D0%BA%D0%B8%D0%B9,_%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80_%D0%A1%D0%B5%D0%BC%D1%91%D0%BD%D0%BE%D0%B2%D0%B8%D1%87"
link = urllib.parse.unquote(link)
print(link)
lang = find_lang(link)
print(lang)
wiki = Wikipedia(lang)

try:
    #print("trying")
    name = find_name(link)
    print(name)
    raw = wiki.article(name)
    true_name = change_name(name, lang)
except:
    #print("exception")
    raw = None

if raw:
    wiki2plain = Wiki2Plain(raw)
    content = wiki2plain.text
    #print(content)
    names = []
    i = 0
    while i < len(content):
        if content[i] == dict_signs[lang][0] and i + 1 < len(content) and content[i + 1].isalpha():
            j = i + 1
            while j < len(content) and content[j] != dict_signs[lang][1]:
                j += 1
            curr = content[i + 1:j]
            if len(curr) < 50 and len(curr) > 1 and there_are_letters(curr) and curr[0].isalpha() and without_strange_words(curr, true_name) and curr[0].isupper():
                if curr[0] == "Г":
                    print(curr, content[i - 50:i + 50])
                names.append(curr)
            i = j
        i += 1
    print("Artist:", true_name)
    names = list(set(names))
    for i in range(len(names)):
        print(names[i])
    result = open('result.txt','w', encoding='utf-8')
    print(content, file=result)
    result.close()