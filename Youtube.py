#Para instalar pytube:
#   py -m pip install pytube 
#   python -m pip install pytube 
from pytube import YouTube

link = input('Ingresa el URL: ')
yt = YouTube(link)
yt.streams.filter(res="720p").first().download()
print('descargado', link)