from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

class Link:
    def __init__(self, songName):
        self.filename = songName.title()
        self.url = "https://www.youtube.com/results?search_query={}".format(songName.rstrip().replace(' ', '+'))
        self.soup = BS(urlopen(self.url).read(), 'html.parser')
        self.tags = self.soup('a')
        self.links = list()

        count = 0
        for tag in self.tags:
            link = tag.get('href', None)
            if link[0: 7] == "/watch?" and count < 6:
                self.links.append("https://www.youtube.com" + link)
                count += 1
        
        self.data = self._filter()
        
    def _filter(self):
        length = len(self.links)

        tempArray = list()
        for i in range(0, length, 2):
            tempArray.append(self.links[i])

        self.links = tempArray
        del tempArray
        
        return self.links

    def song_list(self):
        return (self.filename, self.data[0])