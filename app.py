import requests

video_id = input("Video ID: ")
url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
response = requests.get(url)

if response.status_code == 200:
    with open("thumbnail.jpg", "wb") as file:
        file.write(response.content)
    print("Imagen descargada como thumbnail.jpg")
else:
    print("No se pudo descargar la imagen.")
