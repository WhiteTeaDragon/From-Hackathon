#!/usr/bin/env python

import re
import yaml
import urllib
import urllib.parse
import urllib.request

class WikipediaError(Exception):
    pass

class Wikipedia:
    url_article = 'http://%s.wikipedia.org/w/index.php?action=raw&title=%s'
    url_image = 'http://%s.wikipedia.org/w/index.php?title=Special:FilePath&file=%s'
    url_search = 'http://%s.wikipedia.org/w/api.php?action=query&list=search&srsearch=%s&sroffset=%d&srlimit=%d&format=yaml'
    
    def __init__(self, lang):
        self.lang = lang
    
    def __fetch(self, url):
        #print("fetch")
        request = urllib.request.Request(url)
        #print(request)
        #request.add_header('User-Agent', 'Mozilla/5.0')
        
        try:
            #print("trying in fetch")
            result = urllib.request.urlopen(request)
            #print(result)
        except urllib.error.HTTPError as e:
            raise WikipediaError(e.code)
        except urllib.error.URLError as e:
            raise WikipediaError(e.reason)
        
        #print("returning fetch")
        return result
    
    def article(self, article):
        #print("article", self.url_article, self.lang)
        #print(urllib.parse.quote_plus(article))
        url = self.url_article % (self.lang, urllib.parse.quote_plus(article))
        #print(url)
        result = self.__fetch(url)
        content = result.read().decode(result.headers.get_content_charset())
        #print("before if")
        #print(content.upper().startswith('#REDIRECT'))
        #print(content.upper())

        if content.upper().startswith('#REDIRECT'):
            #print("in if")
            match = re.match('(?i)#REDIRECT \[\[([^\[\]]+)\]\]', content)
            
            if not match == None:
                return self.article(match.group(1))
            
            raise WikipediaError('Can\'t found redirect article.')
        
        #print("returning article")
        return content
    
    def image(self, image, thumb=None):
        url = self.url_image % (self.lang, image)
        result = self.__fetch(url)
        content = result.read()
        
        if thumb:
            url = result.geturl() + '/' + thumb + 'px-' + image
            url = url.replace('/commons/', '/commons/thumb/')
            url = url.replace('/' + self.lang + '/', '/' + self.lang + '/thumb/')
            
            return self.__fetch(url).read()
        
        return content
    
    def search(self, query, page=1, limit=10):
        offset = (page - 1) * limit
        url = self.url_search % (self.lang, urllib.quote_plus(query), offset, limit)
        content = self.__fetch(url).read()
        
        parsed = yaml.load(content)
        search = parsed['query']['search']
        
        results = []
        
        if search:
            for article in search:
                title = article['title'].strip()
                
                snippet = article['snippet']
                snippet = re.sub(r'(?m)<.*?>', '', snippet)
                snippet = re.sub(r'\s+', ' ', snippet)
                snippet = snippet.replace(' . ', '. ')
                snippet = snippet.replace(' , ', ', ')
                snippet = snippet.strip()
                
                wordcount = article['wordcount']
                
                results.append({
                    'title' : title,
                    'snippet' : snippet,
                    'wordcount' : wordcount
                })
        
        # yaml.dump(results, default_style='', default_flow_style=False,
        #     allow_unicode=True)
        return results

if __name__ == '__main__':
    wiki = Wikipedia('simple')
    wiki.article('Uruguay')
    wiki.image('Bono_at_the_2009_Tribeca_Film_Festival.jpg', '640')
    wiki.search('Wikipedia')
    
    print('OK')