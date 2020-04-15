import requests
from bs4 import BeautifulSoup
import urllib.parse


strange_words = ["music award", "золотой граммофон", "дебют года", "Comedy Club"]


def get_text(url):
    rs = requests.get(url)
    root = BeautifulSoup(rs.content, 'html.parser')
    #print(root.a)
    #print(root.b)
    #print(root.i)
    #print(root)
    article = root.select_one('article')
    #print(article)

    return article.text


def there_are_letters(str):
    for i in range(len(str)):
        if str[i].isalpha():
            #print(str[i], str[i].isalpha())
            return True


def get_name(str, arr):
    str_copy = ""
    for i in range(len(str)):
        if str[i] != '*':
            str_copy += str[i].lower()
    i = 0
    curr = 0
    while i < len(arr):
        bef = curr
        curr = str_copy.find(arr[i], curr)
        #print(arr[i], bef, curr, str[:100])
        if curr == -1 or (bef != 0 and (abs(bef - curr) == 0 or abs(bef - curr) > 1)):
            break
        curr += len(arr[i])
        i += 1
    ans = ' ' .join(arr[:i])
    #print(len(ans))
    if len(ans) > 0:
        return ans
    else:
        i = 0
        while i + 1 < len(str) and str[i].islower() and str[i + 1].isupper():
            i += 1
        return str[:i + 1]


def find_name(link):
    curr = link.split('/')
    i = len(curr) - 1
    while len(curr[i]) == 0:
        i -= 1
    return curr[i]


def without_strange_words(str, name):
    copy = str.lower()
    if copy.find(name.lower()) != -1:
        return False
    for i in range(len(strange_words)):
        if copy.find(strange_words[i].lower()) != -1:
            return False
    return True


def change_for_comp(str):
    ans = ""
    for i in range(len(str)):
        if str[i].isalpha():
            ans += str[i].lower()
    return ans


def check_song(song_name, session):
    search_results = pylast.TrackSearch(track_title=song_name, artist_name="", network=network)
    page = search_results.get_next_page()
    MAX = min(3, len(page))
    for i in range(MAX):
        second_flag = True
        if len(page) > i:
            second_flag = False
            res = page[i]
            art = res.artist
            tit = res.title
           # print(art)
            #print("before if", art, tit, file=file_w)
            if abs(len(tit) - len(song_name)) < 5 and (change_for_comp(tit)).find(change_for_comp(song_name)) != -1:
                #print("before return", art, tit, file=file_w)
                #tit = delete_art_from_tit(tit, art)
                return (True, art, tit)
    return (False, None, song_name)


file_w = open("result.txt", 'w', encoding='utf8')

import pylast

# You have to have your own unique two values for API_KEY and API_SECRET
# Obtain yours from https://www.last.fm/api/account/create for Last.fm
API_KEY = "my api key"  # this is a sample key
API_SECRET = "my secret key"

# In order to perform a write operation you need to authenticate yourself
username = "my username"
password_hash = pylast.md5("my password")

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash, session_key=None)

vars = [('"', '"'), ('«', '»'), ('“', '”')]
#url = 'https://pitchfork.com/reviews/albums/nils-frahm-all-melody/'
#url = "https://pitchfork.com/reviews/albums/nils-frahm-all-encores/"
#url = "https://pitchfork.com/reviews/albums/jonathan-fireeater-tremble-under-boom-lights/"
#url = "https://pitchfork.com/reviews/tracks/lil-tjay-lil-baby-decline/"
#url = "https://pitchfork.com/reviews/albums/nils-frahm-all-melody/"
#url = "https://pitchfork.com/reviews/albums/floating-points-crush/"
#url = "https://pitchfork.com/reviews/albums/jimmy-eat-world-surviving/"
#url = "https://pitchfork.com/news/bad-bunny-joins-natanael-cano-on-new-soy-el-diablo-remix-listen/"
#url = "https://pitchfork.com/news/kanye-wests-new-album-jesus-is-king-is-here-listen/"
#url = "https://pitchfork.com/reviews/albums/relaxer-coconut-grove/"
#url = "https://pitchfork.com/news/watch-billie-eilish-perform-bad-guy-and-i-love-you-on-snl/"
#url = "https://en.wikipedia.org/wiki/Yuri_Shatunov"
#url = "https://www.kinopoisk.ru/media/article/3401758/"
#url = "https://muzobzor.ru/news/tantcy-minus-vystupiat-v-klube-volta"
url = "https://muzobzor.ru/news/obiavleny-nominanty-na-premiiu-gremmi-2017"
url = urllib.parse.unquote(url)
content = get_text(url)
names = []
names_set = set()
pairs_set = set()
i = 0
while i < len(content):
    flag = True
    #if content[i] == vars[2][0]:
    #    print(i, content[i - 30:i + 30])
    #print(i)
    for jj in range(len(vars)):
        if not flag:
            break
        #if i == 3523:
        #    print(i, content[i], vars[jj][0])
        if content[i] == vars[jj][0]:
            #print(i)
            flag = False
            #print(len(names_set))
            j = i + 1
            while j < len(content) and content[j] != vars[jj][1]:
                j += 1
            curr = content[i + 1:j]
            if curr not in names_set:
               # print(curr)
                flag, artist, song_name = check_song(curr, network)
               # print(flag, artist, song_name)
                names_set.add(song_name)
                if flag and (artist, song_name) not in pairs_set:
                    print(song_name, artist, file=file_w)
                    pairs_set.add((artist, song_name))
            i = j
    i += 1
file_w.close()
#print(content)
