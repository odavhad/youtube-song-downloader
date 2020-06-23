import os

def create_directory():
    try:
        os.mkdir('data')
    except:
        pass