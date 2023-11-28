import requests

# Use Your Own API KEy
API_key = " "


def get_data(place, days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response = requests.get(url)
    content = response.json()
    filtered_data = content['list']
    nrvalues = 8 * days
    filtered_data = filtered_data[:nrvalues]
    return filtered_data


if __name__ == "__main__":
    print(get_data('Tokyo', 2, "Sky"))
