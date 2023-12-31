from pytube import YouTube
from moviepy.editor import *
import os

def download_youtube_video(url, output_path):
    try:
        # Baixar o vídeo do YouTube
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        video.download(output_path=output_path, filename='temp_video.mp4')

        # Converter o vídeo para MP3
        video_path = f"{output_path}/temp_video.mp4"
        audio_path = f"{output_path}/{yt.title}.mp3"  # Salvar com o título do vídeo
        video_clip = AudioFileClip(video_path)
        video_clip.write_audiofile(audio_path)

        # Excluir o vídeo baixado
        os.remove(video_path)

        print(f"Download e conversão concluídos. Arquivo MP3 salvo em: {audio_path}")
    except Exception as e:
        print(f"Ocorreu um erro ao processar a URL '{url}': {str(e)}")

def download_videos_from_list(file_path, output_directory):
    try:
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        
        with open(file_path, 'r') as file:
            urls = file.readlines()
            for url in urls:
                url = url.strip()  # Remover espaços em branco, nova linha, etc.
                download_youtube_video(url, output_directory + '/baixadas')
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo '{file_path}': {str(e)}")

# Nome do arquivo de texto com a lista de URLs dos vídeos
file_with_urls = "lista_de_videos.txt"

# Diretório de saída para salvar os arquivos MP3
output_directory = "."  # Substitua pelo seu diretório principal

download_videos_from_list(file_with_urls, output_directory)
