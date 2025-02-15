import requests


API_KEY = "76Ago1vfJUmfxYMcdySfzQ22mUXi5Icz"


def get_data(object_iterate, key, raw=None):
    dates = []
    value_list = []
    i = 0
    if raw['code'] != '429001':
        for content_raw in object_iterate:
            no = f"{content_raw['time']}"
            date, raw_t = no.split('T')
            raw_t = raw_t.replace(':00Z', '')
            dates.append(f"{date}({raw_t})")
            if key in f"{content_raw['values']}":
                value = f"{content_raw['values'][key]}"
                value_list.append(value)
            else:
                if sum(value_list) != 0:
                    if len(value_list) != 0:
                        average_uv = sum(value_list) / len(value_list)
                        value_list.append(average_uv)
                    else:
                        average_uv = sum(value_list) / 1
                        value_list.append(average_uv)

                else:
                    value_list.append(0)
            i += 1
        return dates, value_list

    else:
        return ['Server error', 'Try after 1 hour.']


def api_day(location, frequency):
    location = location.replace(' ', '%20').lower()
    url = ("https://api.tomorrow.io/v4/weather/forecast?"
           f"location={location}&"
           f"timesteps=1{frequency}&"
           "values=metric&"
           f"apikey={API_KEY}")
    try:
        response = requests.get(url=url)
        content_raw = response.json()

        if frequency == 'd':
            content = content_raw['timelines']['daily']
            dates, temp = get_data(content, 'temperatureApparentAvg', content_raw)
            return dates, temp
        elif frequency == 'm':
            content = content_raw['timelines']['minutely']
            dates, temp = get_data(content, 'temperature', content_raw)
            return dates, temp
        elif frequency == 'h':
            content = content_raw['timelines']['hourly']
            dates, temp = get_data(content, 'temperature', content_raw)
            return dates, temp
    except KeyError:
        pass


def api_uv_index(location, frequency):
    location = location.replace(' ', '%20').lower()
    url = ("https://api.tomorrow.io/v4/weather/forecast?"
           f"location={location}&"
           f"timesteps=1{frequency}&"
           "values=metric&"
           f"apikey={API_KEY}")

    response = requests.get(url=url)

    content_raw = response.json()
    try:
        if frequency == 'd':
            content = content_raw['timelines']['daily']
            dates, uv_indexes = get_data(content, 'uvIndexMax', content_raw)
            return dates, uv_indexes
        elif frequency == 'm':
            content = content_raw['timelines']['minutely']
            dates, uv_indexes = get_data(content, 'uvIndexMax', content_raw)
            return dates, uv_indexes
        elif frequency == 'h':
            content = content_raw['timelines']['hourly']
            dates, uv_indexes = get_data(content, 'uvIndexMax', content_raw)
            return dates, uv_indexes

    except IndexError:
        pass


def api_humidity(location, frequency):
    location = location.replace(' ', '%20').lower()
    url = ("https://api.tomorrow.io/v4/weather/forecast?"
           f"location={location}&"
           f"timesteps=1{frequency}&"
           "values=metric&"
           f"apikey={API_KEY}")
    try:
        response = requests.get(url=url)
        content_raw = response.json()
        if frequency == 'd':
            content = content_raw['timelines']['daily']
            dates, humidity = get_data(content, 'humidityAvg', content_raw)
            return dates, humidity
        elif frequency == 'm':
            content = content_raw['timelines']['minutely']
            dates, humidity = get_data(content, 'humidity', content_raw)
            return dates, humidity
        elif frequency == 'h':
            content = content_raw['timelines']['hourly']
            dates, humidity = get_data(content, 'humidity', content_raw)
            return dates, humidity
    except KeyError:
        pass


def api_visibility(location, frequency):
    location = location.replace(' ', '%20').lower()
    url = ("https://api.tomorrow.io/v4/weather/forecast?"
           f"location={location}&"
           f"timesteps=1{frequency}&"
           "values=metric&"
           f"apikey={API_KEY}")
    try:
        response = requests.get(url=url)
        content_raw = response.json()
        if frequency == 'd':
            content = content_raw['timelines']['daily']
            dates, visibility = get_data(content, 'visibilityAvg', content_raw)
            return dates, visibility
        elif frequency == 'm':
            content = content_raw['timelines']['minutely']
            dates, visibility = get_data(content, 'visibility', content_raw)
            return dates, visibility
        elif frequency == 'h':
            content = content_raw['timelines']['hourly']
            dates, visibility = get_data(content, 'visibility', content_raw)
            return dates, visibility
    except KeyError:
        pass


def api_dew_point(location, frequency):
    location = location.replace(' ', '%20').lower()
    url = ("https://api.tomorrow.io/v4/weather/forecast?"
           f"location={location}&"
           f"timesteps=1{frequency}&"
           "values=metric&"
           f"apikey={API_KEY}")
    try:
        response = requests.get(url=url)
        content_raw = response.json()
        if frequency == 'd':
            content = content_raw['timelines']['daily']
            dates, dew_point = get_data(content, "dewPointAvg", content_raw)
            return dates, dew_point
        elif frequency == 'm':
            content = content_raw['timelines']['minutely']
            dates, dew_point = get_data(content, "dewPoint", content_raw)
            return dates, dew_point
        elif frequency == 'h':
            content = content_raw['timelines']['hourly']
            dates, dew_point = get_data(content, "dewPoint", content_raw)
            return dates, dew_point
    except KeyError:
        pass


def api_weather_code(location, frequency):
    location = location.replace(' ', '%20').lower()
    url = ("https://api.tomorrow.io/v4/weather/forecast?"
           f"location={location}&"
           f"timesteps=1{frequency}&"
           "values=metric&"
           f"apikey={API_KEY}")
    try:
        response = requests.get(url=url)
        content_raw = response.json()
        if frequency == 'd':
            content = content_raw['timelines']['daily']
            dates, weather_code = get_data(content, "weatherCodeMax", content_raw)
            return dates, weather_code
        elif frequency == 'm':
            content = content_raw['timelines']['minutely']
            dates, weather_code = get_data(content, "weatherCode", content_raw)
            return dates, weather_code
        elif frequency == 'h':
            content = content_raw['timelines']['hourly']
            dates, weather_code = get_data(content, "weatherCode", content_raw)
            return dates, weather_code
    except KeyError:
        pass


def api_surface_level(location, frequency):
    location = location.replace(' ', '%20').lower()
    url = ("https://api.tomorrow.io/v4/weather/forecast?"
           f"location={location}&"
           f"timesteps=1{frequency}&"
           f"apikey={API_KEY}")
    try:
        response = requests.get(url=url)
        content_raw = response.json()
        if frequency == 'd':
            content = content_raw['timelines']['daily']
            dates, weather_code = get_data(content, "pressureSurfaceLevelAvg", content_raw)
            return dates, weather_code
        elif frequency == 'm':
            content = content_raw['timelines']['minutely']
            dates, weather_code = get_data(content, "pressureSurfaceLevel", content_raw)
            return dates, weather_code
        elif frequency == 'h':
            content = content_raw['timelines']['hourly']
            dates, weather_code = get_data(content, "pressureSurfaceLevel", content_raw)
            return dates, weather_code
    except KeyError:
        pass


def api_wind_speed(location, frequency):
    location = location.replace(' ', '%20').lower()
    url = ("https://api.tomorrow.io/v4/weather/forecast?"
           f"location={location}&"
           f"timesteps=1{frequency}&"
           f"apikey={API_KEY}")
    try:
        response = requests.get(url=url)
        content_raw = response.json()
        if frequency == 'd':
            content = content_raw['timelines']['daily']
            dates, wind_speed = get_data(content, "windSpeedAvg", content_raw)
            return dates, wind_speed
        elif frequency == 'm':
            content = content_raw['timelines']['minutely']
            dates, wind_speed = get_data(content, "windSpeed", content_raw)
            return dates, wind_speed
        elif frequency == 'h':
            content = content_raw['timelines']['hourly']
            dates, wind_speed = get_data(content, "windSpeed", content_raw)
            return dates, wind_speed
    except KeyError:
        pass


def api_wind_gust(location, frequency):
    location = location.replace(' ', '%20').lower()
    url = ("https://api.tomorrow.io/v4/weather/forecast?"
           f"location={location}&"
           f"timesteps=1{frequency}&"
           f"apikey={API_KEY}")
    try:
        response = requests.get(url=url)
        content_raw = response.json()
        if frequency == 'd':
            content = content_raw['timelines']['daily']
            dates, wind_gust = get_data(content, "windGustAvg", content_raw)
            return dates, wind_gust
        elif frequency == 'm':
            content = content_raw['timelines']['minutely']
            dates, wind_gust = get_data(content, "windGust", content_raw)
            return dates, wind_gust
        elif frequency == 'h':
            content = content_raw['timelines']['hourly']
            dates, wind_gust = get_data(content, "windGust", content_raw)
            return dates, wind_gust
    except KeyError:
        pass

def api_wind_direction(location, frequency):
    location = location.replace(' ', '%20').lower()
    url = ("https://api.tomorrow.io/v4/weather/forecast?"
           f"location={location}&"
           f"timesteps=1{frequency}&"
           f"apikey={API_KEY}")
    try:
        response = requests.get(url=url)
        content_raw = response.json()
        if frequency == 'd':
            content = content_raw['timelines']['daily']
            dates, wind_direction = get_data(content, "windDirectionAvg", content_raw)
            wind_direction = [int(i) for i in wind_direction]
            return dates, wind_direction
        elif frequency == 'm':
            content = content_raw['timelines']['minutely']
            dates, wind_direction = get_data(content, "windDirection", content_raw)
            wind_direction = [int(i) for i in wind_direction]
            return dates, wind_direction
        elif frequency == 'h':
            content = content_raw['timelines']['hourly']
            dates, wind_direction = get_data(content, "windDirection", content_raw)
            wind_direction = [int(i) for i in wind_direction]
            return dates, wind_direction
    except KeyError:
        pass

if __name__ == "__main__":
    a, m = api_weather_code('new%20york', 'h')
    print(len(a))

