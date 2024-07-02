import requests


def fox():
    url = 'https://randomfox.ca/floof'

    response = requests.get(url)
    # response.raise_for_status()

    json_response = response.json()
    image_url = json_response.get('image')

    return image_url


if __name__ == '__main__':
    print(fox())