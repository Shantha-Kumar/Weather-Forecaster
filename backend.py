import requests

API_key = "49171809102a50ed2a60bb0a3b6ee988"


def get_data(place, days, option):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response = requests.get(url)
    content = response.json()
    filtered_data = content['list']
    nrvalues = 8*days
    filtered_data = filtered_data[:nrvalues]
    print(filtered_data)
    if option == "Temperature":
        filtered_data = [dict['main']['temp'] for dict in filtered_data]
    if option == "Sky":
        filtered_data = [dict['weather'][0]['main'] for dict in filtered_data]

    return filtered_data


if __name__ == "__main__":
    print(get_data('Tokyo',2,"Temperature"))
