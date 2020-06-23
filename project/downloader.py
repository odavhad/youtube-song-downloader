import pafy

class Download():
    def __init__(self, fileName, url):
        self.fileName = fileName
        self.url = url

        try:
            self.getAudio()
        except:
            print ("Unable to download")

    def getAudio(self):
        self.audio = pafy.new(self.url).getbestaudio()
        self.audio.download(quiet=False, filepath="data/{0}.{1}".format(self.fileName, self.audio.extension))
        print ("Downloaded Successfully.")