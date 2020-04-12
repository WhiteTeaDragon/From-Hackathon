from wikipedia import Wikipedia
from wiki2plain import Wiki2Plain
import urllib.parse


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


def delete_art_from_tit(tit, art):
    if tit[:len(art) + 3] == art:
        return tit[len(art) + 3:]
        

def change_for_comp(str):
    ans = ""
    for i in range(len(str)):
        if str[i].isalpha():
            ans += str[i].lower()
    return ans


def check_song(song_name, session, artist_name):
    search_results = pylast.TrackSearch(track_title=song_name, artist_name=artist_name, network=network)
    page = search_results.get_next_page()
    #print(song_name, len(search_results))
    Flag = True
    #print(search_results[0].title)
    if len(page) > 0:
        Flag = False
        res = page[0]
        art = res.artist
        #print(art, res.artists, res.title)
        tit = res.title
        #print("before if", art, tit, file=file_w)
        if abs(len(tit) - len(song_name)) < 5 and (change_for_comp(tit)).find(change_for_comp(song_name)) != -1:
            #print("before return", art, tit, file=file_w)
            #print(tit)
            #tit = delete_art_from_tit(tit, art)
            #if len(res.title, 
            return (True, art, tit)
        else:
            Flag = True;
    if Flag:
        search_results = pylast.TrackSearch(track_title=song_name, artist_name="", network=network)
        page = search_results.get_next_page()
        second_flag = True
        if len(page) > 0:
            second_flag = False
            res = page[0]
            art = res.artist
            tit = res.title
            #print("before if", art, tit, file=file_w)
            if abs(len(tit) - len(song_name)) < 5 and (change_for_comp(tit)).find(change_for_comp(song_name)) != -1:
                #print("before return", art, tit, file=file_w)
                #tit = delete_art_from_tit(tit, art)
                return (True, art, tit)
            else:
                second_flag = True
        if second_flag:
            return (False, None, song_name)


file_w = open("result.txt", 'w', encoding='utf8')

import pylast

# You have to have your own unique two values for API_KEY and API_SECRET
# Obtain yours from https://www.last.fm/api/account/create for Last.fm
API_KEY = "70d48262b0e787315b7cce695159b899"  # this is a sample key
API_SECRET = "5150bc25a89cc30e9f7454e12a3afbac"

# In order to perform a write operation you need to authenticate yourself
username = "AlexSend57"
password_hash = pylast.md5("0nly4YOU!")

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash, session_key=None)
dict_signs = {"en" : ('"', '"'), "ru" : ('«', '»')}
#session = discogs.authorise()
#For Wikipedia
#print("hello")
#link = "https://en.wikipedia.org/wiki/Ray_Charles"
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
#link = "https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%BF%D0%BF%D0%B0,_%D0%A4%D1%80%D1%8D%D0%BD%D0%BA"
link = "https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D1%8D%D0%BD,_%D0%9B%D0%B5%D0%BE%D0%BD%D0%B0%D1%80%D0%B4"
link = urllib.parse.unquote(link)
#print(link)
lang = find_lang(link)
#print(lang)
wiki = Wikipedia(lang)

try:
    #print("trying")
    name = find_name(link)
    #print(name)
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
    names_set = set()
    pairs_set = set()
    i = 0
    while i < len(content):
        if content[i] == dict_signs[lang][0]:
            print(len(names_set))
            j = i + 1
            while j < len(content) and content[j] != dict_signs[lang][1]:
                j += 1
            curr = content[i + 1:j]
            if curr not in names_set:
                #print(curr)
                flag, artist, song_name = check_song(curr, network, true_name)
                #print(flag, artist, song_name, file=file_w)
                names_set.add(song_name)
                if flag and (artist, song_name) not in pairs_set:
                    print(song_name, artist, file=file_w)
                    pairs_set.add((artist, song_name))
            i = j
        i += 1
file_w.close()