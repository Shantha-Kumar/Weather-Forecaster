import requests

API_key = "49171809102a50ed2a60bb0a3b6ee988"


def get_data(place, days=None, option=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response = requests.get(url)
    content = response.json()

    return content


if __name__ == "__main__":
    print(get_data('Tokyo'))
