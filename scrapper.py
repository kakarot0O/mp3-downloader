import os
import requests
from bs4 import BeautifulSoup

def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def download_mp3(url, folder_path, song_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(folder_path, f"{song_name}.mp3"), "wb") as file:
            file.write(response.content)
        print(f"{song_name} downloaded successfully!")
    else:
        print("Sorry, song not found.")

def main():
    song_name = input("Enter the song name: ")
    folder_path = os.path.join(os.path.expanduser("~"), "Desktop", "mp3_downloader")
    create_folder(folder_path)

    base_url = "https://pagalworld.com.pe/find/"
    search_url = base_url + song_name.replace(" ", "+")

    response = requests.get(search_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        song_link = soup.select_one("song_selector")
        
        if song_link:
            song_url = song_link["href"]
            download_mp3(song_url, folder_path, song_name)
        else:
            print("Sorry, song not found.")

    else:
        print("Error connecting to the website.")

    choice = input("Do you want to continue? (yes/no): ")
    if choice.lower() == "yes":
        main()
    else:
        print("Exiting the program.")

if __name__ == "__main__":
    main()

