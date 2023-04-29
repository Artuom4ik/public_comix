import os
from random import randint

import requests
from dotenv import load_dotenv


def douwnload_img(img_url):
    response_img = requests.get(img_url)
    response_img.raise_for_status()
    with open("images/comic.png", "wb") as file:
        file.write(response_img.content)


def get_adress_photo(token, group_id):
    params = {
        "group_id": group_id,
        "access_token": token,
        "v": 5.131
    }
    url = "https://api.vk.com/method/photos.getWallUploadServer"
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()['response']['upload_url']


def upload_image(upload_url):
    with open("images/comic.png", "rb") as image:
        url = upload_url
        files = {
            "photo": image
        }
        response = requests.post(url, files=files)
        response.raise_for_status()
        save_server = response.json()
        return save_server["server"], save_server["photo"], save_server["hash"]


def save_photo_to_album(server, photo, photo_hash, group_id, token):
    url = "https://api.vk.com/method/photos.saveWallPhoto"
    params = {
        "access_token": token,
        "group_id": group_id,
        "photo": photo,
        "server": server,
        "hash": photo_hash,
        "v": 5.131
    }
    response = requests.post(url, params=params)
    response.raise_for_status()
    save_comic = response.json()["response"][0]
    return save_comic["id"], save_comic["owner_id"]


def get_comic(comic_number):
    number_comic = randint(1, comic_number)
    url = f"https://xkcd.com/{number_comic}/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["alt"], response.json()["img"]


def post_photo(token, owner_id, media_id, comment, group_id):
    url = "https://api.vk.com/method/wall.post"
    params = {
        "access_token": token,
        "owner_id": f"-{group_id}",
        "from_group": 1,
        "message": comment,
        "attachments": f"photo{owner_id}_{media_id}",
        "v": 5.131
    }
    response = requests.post(url, params=params)
    response.raise_for_status()
    return response.json()


def get_comic_number():
    url = "https://xkcd.com/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["num"]


if __name__ == "__main__":
    load_dotenv()
    token = os.environ["VK_TOKEN"]
    group_id = os.environ["VK_GROUP_ID"]
    comic_number = get_comic_number()
    comment, img_url = get_comic(comic_number)
    douwnload_img(img_url)
    upload_url = get_adress_photo(token, group_id)
    server, photo, photo_hash = upload_image(upload_url)
    media_id, owner_id = save_photo_to_album(
        server,
        photo,
        photo_hash,
        group_id,
        token
    )
    post_photo(token, owner_id, media_id, comment, group_id)
    if os.path.isfile("images/comic.png"):
        os.remove("images/comic.png")
