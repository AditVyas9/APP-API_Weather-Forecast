import requests
import streamlit as st
from datetime import datetime
import pytz
API_KEY = st.secrets['API_KEY']['API_KEY']
api_key = st.secrets['Geocode']['API_KEY']
API_real = st.secrets['timezonedb']['API_KEY']
def exact(raw_location):
    url = ("https://geocode.maps.co/search?"
           f"q={raw_location}&"
           f"api_key={api_key}")
    response = requests.get(url=url)
    content_raw = response.json()
    for o in content_raw:
        if o['type'] == "locality" or "administrative" or "county" or "city" or "town" or "village":
            lat = o['lat']
            lon = o['lon']
            final_location = f"{lat}, {lon}"
            return final_location

def get_data(object_iterate, key):
    dates = []
    value_list = []
    i = 0

    for content_raw in object_iterate:
        no = f"{content_raw['time']}"
        date, raw_t = no.split('T')
        raw_t = raw_t.replace(':00Z', '')
        dates.append(f"{date}({raw_t})")
        if key in f"{content_raw['values']}":
            value = f"{content_raw['values'][key]}"
            value_list.append(value)
        else:
            value_list = [int(ii) for ii in value_list]
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
            dates, temp = get_data(content, 'temperatureApparentAvg')
            return dates, temp
        elif frequency == 'm':
            content = content_raw['timelines']['minutely']
            dates, temp = get_data(content, 'temperature')
            return dates, temp
        elif frequency == 'h':
            content = content_raw['timelines']['hourly']
            dates, temp = get_data(content, 'temperature')
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
            dates, uv_indexes = get_data(content, 'uvIndexMax')
            return dates, uv_indexes
        elif frequency == 'm':
            content = content_raw['timelines']['minutely']
            dates, uv_indexes = get_data(content, 'uvIndexMax')
            return dates, uv_indexes
        elif frequency == 'h':
            content = content_raw['timelines']['hourly']
            dates, uv_indexes = get_data(content, 'uvIndexMax')
            return dates, uv_indexes

    except KeyError:
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
            dates, humidity = get_data(content, 'humidityAvg')
            return dates, humidity
        elif frequency == 'm':
            content = content_raw['timelines']['minutely']
            dates, humidity = get_data(content, 'humidity')
            return dates, humidity
        elif frequency == 'h':
            content = content_raw['timelines']['hourly']
            dates, humidity = get_data(content, 'humidity')
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
            dates, visibility = get_data(content, 'visibilityAvg')
            return dates, visibility
        elif frequency == 'm':
            content = content_raw['timelines']['minutely']
            dates, visibility = get_data(content, 'visibility')
            return dates, visibility
        elif frequency == 'h':
            content = content_raw['timelines']['hourly']
            dates, visibility = get_data(content, 'visibility')
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
            dates, dew_point = get_data(content, "dewPointAvg")
            return dates, dew_point
        elif frequency == 'm':
            content = content_raw['timelines']['minutely']
            dates, dew_point = get_data(content, "dewPoint")
            return dates, dew_point
        elif frequency == 'h':
            content = content_raw['timelines']['hourly']
            dates, dew_point = get_data(content, "dewPoint")
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
            dates, weather_code = get_data(content, "weatherCodeMax")
            return dates, weather_code
        elif frequency == 'm':
            content = content_raw['timelines']['minutely']
            dates, weather_code = get_data(content, "weatherCode")
            return dates, weather_code
        elif frequency == 'h':
            content = content_raw['timelines']['hourly']
            dates, weather_code = get_data(content, "weatherCode")
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
            dates, weather_code = get_data(content, "pressureSurfaceLevelAvg")
            return dates, weather_code
        elif frequency == 'm':
            content = content_raw['timelines']['minutely']
            dates, weather_code = get_data(content, "pressureSurfaceLevel")
            return dates, weather_code
        elif frequency == 'h':
            content = content_raw['timelines']['hourly']
            dates, weather_code = get_data(content, "pressureSurfaceLevel")
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
            dates, wind_speed = get_data(content, "windSpeedAvg")
            return dates, wind_speed
        elif frequency == 'm':
            content = content_raw['timelines']['minutely']
            dates, wind_speed = get_data(content, "windSpeed")
            return dates, wind_speed
        elif frequency == 'h':
            content = content_raw['timelines']['hourly']
            dates, wind_speed = get_data(content, "windSpeed")
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
            dates, wind_gust = get_data(content, "windGustAvg")
            return dates, wind_gust
        elif frequency == 'm':
            content = content_raw['timelines']['minutely']
            dates, wind_gust = get_data(content, "windGust")
            return dates, wind_gust
        elif frequency == 'h':
            content = content_raw['timelines']['hourly']
            dates, wind_gust = get_data(content, "windGust")
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
            dates, wind_direction = get_data(content, "windDirectionAvg")
            wind_direction = [int(i) for i in wind_direction]
            return dates, wind_direction
        elif frequency == 'm':
            content = content_raw['timelines']['minutely']
            dates, wind_direction = get_data(content, "windDirection")
            wind_direction = [int(i) for i in wind_direction]
            return dates, wind_direction
        elif frequency == 'h':
            content = content_raw['timelines']['hourly']
            dates, wind_direction = get_data(content, "windDirection")
            wind_direction = [int(i) for i in wind_direction]
            return dates, wind_direction
    except KeyError:
        pass


def aqi(lat, lon):
    url = ("https://air-quality-api.open-meteo.com/v1/air-quality?"
           f"latitude={lat}&longitude={lon}&hourly=pm10,pm2_5")
    response = requests.get(url)
    content_raw = response.json()
    try:
        dates = content_raw['hourly']['time']
        dates = [f"{i.replace('T', '(')})" for i in dates]
        pm_25 = content_raw['hourly']['pm2_5']
        pm10 = content_raw['hourly']['pm10']
        return dates, pm_25, pm10
    except KeyError:
        pass

def local_time(lat, lon, gmt_datetime):
    url = ("https://api.timezonedb.com/v2.1/get-time-zone?"
           f"key={API_real}&format=json&by=position&"
           f"lat={lat}&"
           f"lng={lon}")
    response = requests.get(url)
    response.encoding = 'utf-8'
    content_raw = response.json()
    tz = content_raw['zoneName']
    new_dates = []
    for date in gmt_datetime:
        gmt_datetime = datetime.strptime(date, "%Y-%m-%d(%H:%M)")
        gmt_timezone = pytz.timezone('GMT')
        gmt_datetime = gmt_timezone.localize(gmt_datetime)
        zone = pytz.timezone(tz)
        dt = gmt_datetime.astimezone(zone)
        datetime_str = dt.strftime("%Y-%m-%d(%H:%M)")
        new_dates.append(datetime_str)
    return new_dates


if __name__ == "__main__":
    exact('New Delhi, India')