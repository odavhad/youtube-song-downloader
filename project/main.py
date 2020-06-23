from webscraper import Link
from downloader import Download
from data_dir import create_directory

def main():
    create_directory()

    songName = input("Enter the song name: ")
    link = Link(songName)
    details = link.song_list()
    
    download = Download(details[0], details[1])

main()