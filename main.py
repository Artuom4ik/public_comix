import requests
from pprint import pprint


def douwnload_img(img_url):
    response_img = requests.get(img_url)
    response_img.raise_for_status()
    with open("images/comix.png", "wb") as file:
        file.write(response_img.content)


if __name__=="__main__":
    url = "https://xkcd.com/353/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    img_url = response.json()["img"]
    douwnload_img(img_url)


