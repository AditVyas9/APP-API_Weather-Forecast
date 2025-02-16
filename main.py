import streamlit as st
import plotly.express as px
import backend as bk

st.header('Weather Forecast App for the Next Days')
place = st.text_input('Place:')
images = {
                '1000': 'images/1000.png',
                '1100': 'images/1100.png',
                '1101': 'images/1101.png',
                '1102': 'images/1102.png',
                '1001': 'images/1001.png',
                '2100': 'images/2100.png',
                '2000': 'images/2000.png',
                '4000': 'images/4000.png',
                '4200': 'images/4200.png',
                '4001': 'images/4001.png',
                '4201': 'images/4201.png',
                '5000': 'images/5000.png',
                '5001': 'images/5001.png',
                '5100': 'images/5100.png',
                '5101': 'images/5101.png',
                '6000': 'images/6000.png',
                '6001': 'images/6001.png',
                '6200': 'images/6200.png',
                '6201': 'images/6201.png',
                '7000': 'images/7000.png',
                '7101': 'images/7101.png',
                '7102': 'images/7102.png',
                '8000': 'images/8000.png'
            }
weather_code ={
      "0": "Unknown",
      "1000": "Clear, Sunny",
      "1100": "Mostly Clear",
      "1101": "Partly Cloudy",
      "1102": "Mostly Cloudy",
      "1001": "Cloudy",
      "2000": "Fog",
      "2100": "Light Fog",
      "4000": "Drizzle",
      "4001": "Rain",
      "4200": "Light Rain",
      "4201": "Heavy Rain",
      "5000": "Snow",
      "5001": "Flurries",
      "5100": "Light Snow",
      "5101": "Heavy Snow",
      "6000": "Freezing Drizzle",
      "6001": "Freezing Rain",
      "6200": "Light Freezing Rain",
      "6201": "Heavy Freezing Rain",
      "7000": "Ice Pellets",
      "7101": "Heavy Ice Pellets",
      "7102": "Light Ice Pellets",
      "8000": "Thunderstorm"
    }
img = {"North": 'images/North.png',
       "South": 'images/South.png',
       "South-east": 'images/southeast.png',
       "South-west": 'images/southwest.png',
       "West": 'images/west.png',
       "East": 'images/east.png.png',
       "North-west": 'images/northwest.png',
       "North-east": 'images/northeast.png',
       }

option = st.selectbox("Select data to view", ("Temperature", "UV Index", "Visibility", "Humidity", "Dew point","Sky Conditions", "Surface Pressure", "Wind Speed", "Wind Gust", "Wind Direction"))
option_2 = st.selectbox("Select frequency:",("Daily", "Hourly", "Minutely"))


if place:

    st.subheader(f"{option} in {place}")
    match option:
        case "Temperature":
            match option_2:
                case "Daily":
                    try:
                        dates, temp = bk.api_day(place, 'd')
                        figure = px.line(x=dates, y=temp, labels={"x": "Dates(in Universal Time Coordinated-UTC)",
                                                                 "y": f"Temperature({u"\u00b0"}C)"})
                        figure.update_xaxes(tickmode="auto", nticks=12)
                        figure.update_xaxes(ticksuffix="   ")
                        figure.update_yaxes(ticksuffix="   ")
                        st.plotly_chart(figure_or_data=figure)
                    except TypeError:
                        st.header('Server error:'
                                  'Please try after 1 hour!')
                case "Hourly":
                    try:
                        dates, temp = bk.api_day(place, 'h')
                        figure = px.line(x=dates, y=temp, labels={"x": "Dates(in Universal Time Coordinated-UTC)",
                                                                  "y": f"Temperature({u"\u00b0"}C)"})
                        figure.update_xaxes(tickmode="auto", nticks=12)
                        figure.update_xaxes(ticksuffix="   ")
                        figure.update_yaxes(ticksuffix="   ")

                        st.plotly_chart(figure_or_data=figure)
                    except TypeError:
                        
                        st.header('Server error:'
                                  'Please try after 1 hour!')
                case "Minutely":
                    try:
                        dates, temp = bk.api_day(place, 'm')
                        figure = px.line(x=dates, y=temp, labels={"x": "Dates(in Universal Time Coordinated-UTC)",
                                                                  "y": f"Temperature({u"\u00b0"}C)"})
                        figure.update_xaxes(tickmode="auto", nticks=12)
                        figure.update_xaxes(ticksuffix="   ")
                        figure.update_yaxes(ticksuffix="   ")
                        st.plotly_chart(figure_or_data=figure)
                    except TypeError:
                        
                        st.header('Server error:'
                                  'Please try after 1 hour!')
        case "UV Index":
            match option_2:
                case "Daily":
                    try:
                        dates, temp = bk.api_uv_index(place, 'd')
                        figure = px.line(x=dates, y=temp, labels={"x": "Dates(in Universal Time Coordinated-UTC)",
                                                                  "y": f"UV Index(mW/m{'\u00b2'})"})
                        figure.update_xaxes(tickmode="auto", nticks=12)
                        figure.update_xaxes(ticksuffix="   ")
                        figure.update_yaxes(ticksuffix="   ")
                        st.plotly_chart(figure_or_data=figure)
                    except TypeError:
                        
                        st.header('Server error:'
                                  'Please try after 1 hour!')
                case "Hourly":
                    try:
                        dates, temp = bk.api_uv_index(place, 'h')
                        figure = px.line(x=dates, y=temp, labels={"x": "Dates(in Universal Time Coordinated-UTC)",
                                                                  "y": f"UV Index(mW/m{'\u00b2'})"})
                        figure.update_xaxes(tickmode="auto", nticks=12)
                        figure.update_xaxes(ticksuffix="   ")
                        figure.update_yaxes(ticksuffix="   ")
                        st.plotly_chart(figure_or_data=figure)
                    except TypeError:
                        
                        st.header('Server error:'
                                  'Please try after 1 hour!')
                case "Minutely":
                    try:
                        dates, temp = bk.api_uv_index(place, 'm')
                        figure = px.line(x=dates, y=temp, labels={"x": "Dates(in Universal Time Coordinated-UTC)",
                                                                  "y": f"UV Index(mW/m{'\u00b2'})"})
                        figure.update_xaxes(tickmode="auto", nticks=12)
                        figure.update_xaxes(ticksuffix="   ")
                        figure.update_yaxes(ticksuffix="   ")
                        st.plotly_chart(figure_or_data=figure)
                    except TypeError:
                        
                        st.header('Server error:'
                                  'Please try after 1 hour!')
        case "Visibility":
            match option_2:
                case "Daily":
                    try:
                        dates, temp = bk.api_visibility(place, 'd')
                        figure = px.line(x=dates, y=temp, labels={"x": "Dates(in Universal Time Coordinated-UTC)",
                                                                  "y": f"Visibility(km)"})
                        figure.update_xaxes(tickmode="auto", nticks=12)
                        figure.update_xaxes(ticksuffix="   ")
                        figure.update_yaxes(ticksuffix="   ")
                        st.plotly_chart(figure_or_data=figure)
                    except TypeError:
                        
                        st.header('Server error:'
                                  'Please try after 1 hour!')
                case "Hourly":
                    try:
                        dates, temp = bk.api_visibility(place, 'h')
                        figure = px.line(x=dates, y=temp, labels={"x": "Dates(in Universal Time Coordinated-UTC)",
                                                                  "y": f"Visibility(km)"})
                        figure.update_xaxes(tickmode="auto", nticks=12)
                        figure.update_xaxes(ticksuffix="   ")
                        figure.update_yaxes(ticksuffix="   ")
                        st.plotly_chart(figure_or_data=figure)
                    except TypeError:
                        
                        st.header('Server error:'
                                  'Please try after 1 hour!')
                case "Minutely":
                    try:
                        dates, temp = bk.api_visibility(place, 'm')
                        figure = px.line(x=dates, y=temp, labels={"x": "Dates(in Universal Time Coordinated-UTC)",
                                                                  "y": f"Visibility(km)"})
                        figure.update_xaxes(tickmode="auto", nticks=12)
                        figure.update_xaxes(ticksuffix="   ")
                        figure.update_yaxes(ticksuffix="   ")
                        st.plotly_chart(figure_or_data=figure)
                    except TypeError:
                        
                        st.header('Server error:'
                                  'Please try after 1 hour!')
        case "Humidity":
            match option_2:
                case "Daily":
                    try:
                        dates, temp = bk.api_humidity(place, 'd')
                        figure = px.line(x=dates, y=temp, labels={"x": "Dates(in Universal Time Coordinated-UTC)",
                                                                  "y": f"Humidity(%)"})
                        figure.update_xaxes(tickmode="auto", nticks=12)
                        figure.update_xaxes(ticksuffix="   ")
                        figure.update_yaxes(ticksuffix="   ")
                        st.plotly_chart(figure_or_data=figure)
                    except TypeError:
                        
                        st.header('Server error:'
                                  'Please try after 1 hour!')
                case "Hourly":
                    try:
                        dates, temp = bk.api_humidity(place, 'h')
                        figure = px.line(x=dates, y=temp, labels={"x": "Dates(in Universal Time Coordinated-UTC)",
                                                                  "y": f"Humidity(%)"})
                        figure.update_xaxes(tickmode="auto", nticks=12)
                        figure.update_xaxes(ticksuffix="   ")
                        figure.update_yaxes(ticksuffix="   ")
                        st.plotly_chart(figure_or_data=figure)
                    except TypeError:
                        
                        st.header('Server error:'
                                  'Please try after 1 hour!')
                case "Minutely":
                    try:
                        dates, temp = bk.api_humidity(place, 'm')
                        figure = px.line(x=dates, y=temp, labels={"x": "Dates(in Universal Time Coordinated-UTC)",
                                                                  "y": f"Humidity(%)"})
                        figure.update_xaxes(tickmode="auto", nticks=12)
                        figure.update_xaxes(ticksuffix="   ")
                        figure.update_yaxes(ticksuffix="   ")
                        st.plotly_chart(figure_or_data=figure)
                    except TypeError:
                        
                        st.header('Server error:'
                                  'Please try after 1 hour!')
        case "Sky Conditions":
            st.write('All Dates are in Universal Time Coordinated(UTC)')
            match option_2:
                case "Daily":
                    try:
                        dates, codes = bk.api_weather_code(place, 'd')
                        image_paths = [images[condition] for condition in codes]
                        description = [weather_code[condition] for condition in codes]
                        num_cols = 5
                        num_rows = (len(image_paths) + num_cols - 1) // num_cols

                        for i in range(num_rows):
                            cols = st.columns(num_cols)
                            for j in range(num_cols):
                                index = i * num_cols + j
                                if index < len(image_paths):
                                    cols[j].image(image_paths[index], width=50)
                                    cols[j].write(description[index])
                                    cols[j].write(dates[index])

                    except TypeError:
                        
                        st.header('Server error:'
                                  'Please try after 1 hour!')
                case "Hourly":
                    value = st.slider('Data you want:', min_value=5, max_value=120)
                    try:
                        dates, codes = bk.api_weather_code(place, 'h')
                        dates = dates[:value]
                        image_paths = [images[condition] for condition in codes][:value]
                        description = [weather_code[condition] for condition in codes][:value]
                        num_cols = 5
                        num_rows = (len(image_paths) + num_cols - 1) // num_cols

                        for i in range(num_rows):
                            cols = st.columns(num_cols)
                            for j in range(num_cols):
                                index = i * num_cols + j
                                if index < len(image_paths):
                                    cols[j].image(image_paths[index], width=50)
                                    cols[j].write(description[index])
                                    cols[j].write(dates[index])

                    except TypeError:
                        
                        st.header('Server error:'
                                  'Please try after 1 hour!')
                case "Minutely":
                    value = st.slider('Data you want:', min_value=5, max_value=120)
                    try:
                        dates, codes = bk.api_weather_code(place, 'm')
                        dates = dates[:value]
                        image_paths = [images[condition] for condition in codes][:value]
                        description = [weather_code[condition] for condition in codes][:value]
                        num_cols = 5
                        num_rows = (len(image_paths) + num_cols - 1) // num_cols

                        for i in range(num_rows):
                            cols = st.columns(num_cols)
                            for j in range(num_cols):
                                index = i * num_cols + j
                                if index < len(image_paths):
                                    cols[j].image(image_paths[index], width=50)
                                    cols[j].write(description[index])
                                    cols[j].write(dates[index])
                    except TypeError:
                        st.header('Server error:'
                                  'Please try after 1 hour!')
        case "Dew point":
            match option_2:
                case "Daily":
                    try:
                        dates, temp = bk.api_dew_point(place, 'd')
                        figure = px.line(x=dates, y=temp, labels={
                            "x": "Dates(in Universal Time Coordinated-UTC)",
                            "y": f"Dew point({u"\u00b0"}C)"})
                        figure.update_xaxes(tickmode="auto", nticks=12)
                        figure.update_xaxes(ticksuffix="   ")
                        figure.update_yaxes(ticksuffix="   ")
                        st.plotly_chart(figure_or_data=figure)
                    except TypeError:

                        st.header('Server error:'
                                  'Please try after 1 hour!')
                case "Hourly":
                    try:
                        dates, temp = bk.api_dew_point(place, 'h')
                        figure = px.line(x=dates, y=temp, labels={
                            "x": "Dates(in Universal Time Coordinated-UTC)",
                            "y": f"Dew point({u"\u00b0"}C)"})
                        figure.update_xaxes(tickmode="auto", nticks=12)
                        figure.update_xaxes(ticksuffix="   ")
                        figure.update_yaxes(ticksuffix="   ")
                        st.plotly_chart(figure_or_data=figure)

                    except TypeError:

                        st.header('Server error:'
                                  'Please try after 1 hour!')
                case "Minutely":
                    try:
                        dates, temp = bk.api_dew_point(place, 'm')
                        figure = px.line(x=dates, y=temp, labels={
                            "x": "Dates(in Universal Time Coordinated-UTC)",
                            "y": f"Dew point({u"\u00b0"}C)"})
                        figure.update_xaxes(tickmode="auto", nticks=12)
                        figure.update_xaxes(ticksuffix="   ")
                        figure.update_yaxes(ticksuffix="   ")
                        st.plotly_chart(figure_or_data=figure)
                    except TypeError:
                        st.header('Server error:'
                                  'Please try after 1 hour!')
        case "Surface Pressure":
            match option_2:
                case "Daily":
                    try:
                        dates, temp = bk.api_surface_level(place, 'd')
                        figure = px.line(x=dates, y=temp, labels={
                            "x": "Dates(in Universal Time Coordinated-UTC)",
                            "y": f"Surface Pressure(hPa)"})
                        figure.update_xaxes(tickmode="auto", nticks=12)
                        figure.update_xaxes(ticksuffix="   ")
                        figure.update_yaxes(ticksuffix="   ")
                        st.plotly_chart(figure_or_data=figure)
                    except TypeError:

                        st.header('Server error:'
                                  'Please try after 1 hour!')
                case "Hourly":
                    try:
                        dates, temp = bk.api_surface_level(place, 'h')
                        figure = px.line(x=dates, y=temp, labels={
                            "x": "Dates(in Universal Time Coordinated-UTC)",
                            "y": f"Surface Pressure(hPa)"})
                        figure.update_xaxes(tickmode="auto", nticks=12)
                        figure.update_xaxes(ticksuffix="   ")
                        figure.update_yaxes(ticksuffix="   ")
                        st.plotly_chart(figure_or_data=figure)
                    except TypeError:

                        st.header('Server error:'
                                  'Please try after 1 hour!')
                case "Minutely":
                    try:
                        dates, temp = bk.api_surface_level(place, 'm')
                        figure = px.line(x=dates, y=temp, labels={
                            "x": "Dates(in Universal Time Coordinated-UTC)",
                            "y": f"Surface Pressure(hPa)"})
                        figure.update_xaxes(tickmode="auto", nticks=12)
                        figure.update_xaxes(ticksuffix="   ")
                        figure.update_yaxes(ticksuffix="   ")
                        st.plotly_chart(figure_or_data=figure)
                    except TypeError:

                        st.header('Server error:'
                                  'Please try after 1 hour!')
        case "Wind Speed":
            match option_2:
                case "Daily":
                    try:
                        dates, temp = bk.api_wind_speed(place, 'd')
                        figure = px.line(x=dates, y=temp, labels={
                            "x": "Dates(in Universal Time Coordinated-UTC)",
                            "y": f"Wind Speed(m/s)"})
                        figure.update_xaxes(tickmode="auto", nticks=12)
                        figure.update_xaxes(ticksuffix="   ")
                        figure.update_yaxes(ticksuffix="   ")
                        st.plotly_chart(figure_or_data=figure)
                    except TypeError:

                        st.header('Server error:'
                                  'Please try after 1 hour!')
                case "Hourly":
                    try:
                        dates, temp = bk.api_wind_speed(place, 'h')
                        figure = px.line(x=dates, y=temp, labels={
                            "x": "Dates(in Universal Time Coordinated-UTC)",
                            "y": f"Wind Speed(m/s)"})
                        figure.update_xaxes(tickmode="auto", nticks=12)
                        figure.update_xaxes(ticksuffix="   ")
                        figure.update_yaxes(ticksuffix="   ")
                        st.plotly_chart(figure_or_data=figure)
                    except TypeError:

                        st.header('Server error:'
                                  'Please try after 1 hour!')
                case "Minutely":
                    try:
                        dates, temp = bk.api_wind_speed(place, 'm')
                        figure = px.line(x=dates, y=temp, labels={
                            "x": "Dates(in Universal Time Coordinated-UTC)",
                            "y": f"Wind Speed(m/s)"})
                        figure.update_xaxes(tickmode="auto", nticks=12)
                        figure.update_xaxes(ticksuffix="   ")
                        figure.update_yaxes(ticksuffix="   ")
                        st.plotly_chart(figure_or_data=figure)
                    except TypeError:

                        st.header('Server error:'
                                  'Please try after 1 hour!')
        case "Wind Gust":
            match option_2:
                case "Daily":
                    try:
                        dates, temp = bk.api_wind_gust(place, 'd')
                        figure = px.line(x=dates, y=temp, labels={
                            "x": "Dates(in Universal Time Coordinated-UTC)",
                            "y": f"Wind Gust(m/s)"})
                        figure.update_xaxes(tickmode="auto", nticks=12)
                        figure.update_xaxes(ticksuffix="   ")
                        figure.update_yaxes(ticksuffix="   ")
                        st.plotly_chart(figure_or_data=figure)
                    except TypeError:

                        st.header('Server error:'
                                  'Please try after 1 hour!')
                case "Hourly":
                    try:
                        dates, temp = bk.api_wind_gust(place, 'h')
                        figure = px.line(x=dates, y=temp, labels={
                            "x": "Dates(in Universal Time Coordinated-UTC)",
                            "y": f"Wind Gust(m/s)"})
                        figure.update_xaxes(tickmode="auto", nticks=12)
                        figure.update_xaxes(ticksuffix="   ")
                        figure.update_yaxes(ticksuffix="   ")
                        st.plotly_chart(figure_or_data=figure)
                    except TypeError:

                        st.header('Server error:'
                                  'Please try after 1 hour!')
                case "Minutely":
                    try:
                        dates, temp = bk.api_wind_gust(place, 'm')
                        figure = px.line(x=dates, y=temp, labels={
                            "x": "Dates(in Universal Time Coordinated-UTC)",
                            "y": f"Wind Gust(m/s)"})
                        figure.update_xaxes(tickmode="auto", nticks=12)
                        figure.update_xaxes(ticksuffix="   ")
                        figure.update_yaxes(ticksuffix="   ")
                        st.plotly_chart(figure_or_data=figure)
                    except TypeError:

                        st.header('Server error:'
                                  'Please try after 1 hour!')
        case "Wind Direction":
            st.write('All Dates are in Universal Time Coordinated(UTC)')
            match option_2:
                case "Daily":
                    value_list = []
                    try:
                        dates, values = bk.api_wind_direction(place, 'h')
                        ii = 0
                        for value in values:
                            if  0 >= value < 45:
                                value_list.append(f"{value}{u"\u00b0"}N")
                            elif 45 <= value < 90:
                                value_list.append(f"{value}{u"\u00b0"}NE")
                            elif 90 <= value < 135:
                                value_list.append(f"{value}{u"\u00b0"}E")
                            elif 135 <= value < 180:
                                value_list.append(f"{value}{u"\u00b0"}SE")
                            elif 180 <= value < 225:
                                value_list.append(f"{value}{u"\u00b0"}S")
                            elif 225 <= value < 270:
                                value_list.append(f"{value}{u"\u00b0"}SW")
                            elif 270 <= value < 310:
                                value_list.append(f"{value}{u"\u00b0"}W")
                            elif 310 <= value < 360:
                                value_list.append(f"{value}{u"\u00b0"}NW")
                        print(value_list)
                        num_cols = 5  # You can adjust this to have more or fewer columns
                        num_rows = (len(value_list) + num_cols - 1) // num_cols  # Calculate the number of rows

                        image_paths = []  # List to store image paths
                        descriptions = []  # List to store descriptions
                        dates_to_display = []  # List to store dates

                        for i, date in zip(value_list, dates):
                            if i.endswith('°N'):
                                image_paths.append(img['North'])
                                descriptions.append(i)
                                dates_to_display.append(
                                    date)  # added date to the list
                            elif i.endswith('°NE'):
                                image_paths.append(img['North-east'])
                                descriptions.append(i)
                                dates_to_display.append(
                                    date)  # added date to the list
                            elif i.endswith('°E'):
                                image_paths.append(img['East'])
                                descriptions.append(i)
                                dates_to_display.append(
                                    date)  # added date to the list
                            elif i.endswith('°SE'):
                                image_paths.append(img['South-east'])
                                descriptions.append(i)
                                dates_to_display.append(
                                    date)  # added date to the list
                            elif i.endswith('°S'):
                                image_paths.append(img['South'])
                                descriptions.append(i)
                                dates_to_display.append(
                                    date)  # added date to the list
                            elif i.endswith('°SW'):
                                image_paths.append(img['South-west'])
                                descriptions.append(i)
                                dates_to_display.append(
                                    date)  # added date to the list
                            elif i.endswith('°W'):
                                image_paths.append(img['West'])
                                descriptions.append(i)
                                dates_to_display.append(
                                    date)  # added date to the list
                            elif i.endswith('°NW'):
                                image_paths.append(img['North-west'])
                                descriptions.append(i)
                                dates_to_display.append(
                                    date)  # added date to the list

                        for i in range(num_rows):
                            cols = st.columns(num_cols)
                            for j in range(num_cols):
                                index = i * num_cols + j
                                if index < len(image_paths):
                                    cols[j].image(image_paths[index], width=50)
                                    cols[j].write(descriptions[index])
                                    cols[j].write(dates_to_display[index])
                    except TypeError:
                        st.header('Server error:'
                                  'Please try after 1 hour!')
                case "Hourly":
                    value_slider = st.slider('Data you want:', min_value=5,
                                      max_value=120)
                    value_list = []

                    try:
                        dates, values = bk.api_wind_direction(place, 'h')
                        dates = dates[:value_slider]
                        values = values[:value_slider]
                        ii = 0
                        for value in values:
                            if  0 >= value < 45:
                                value_list.append(f"{value}{u"\u00b0"}N")
                            elif 45 <= value < 90:
                                value_list.append(f"{value}{u"\u00b0"}NE")
                            elif 90 <= value < 135:
                                value_list.append(f"{value}{u"\u00b0"}E")
                            elif 135 <= value < 180:
                                value_list.append(f"{value}{u"\u00b0"}SE")
                            elif 180 <= value < 225:
                                value_list.append(f"{value}{u"\u00b0"}S")
                            elif 225 <= value < 270:
                                value_list.append(f"{value}{u"\u00b0"}SW")
                            elif 270 <= value < 310:
                                value_list.append(f"{value}{u"\u00b0"}W")
                            elif 310 <= value < 360:
                                value_list.append(f"{value}{u"\u00b0"}NW")
                        print(value_list)
                        num_cols = 5  # You can adjust this to have more or fewer columns
                        num_rows = (len(value_list) + num_cols - 1) // num_cols  # Calculate the number of rows

                        image_paths = []  # List to store image paths
                        descriptions = []  # List to store descriptions
                        dates_to_display = []  # List to store dates

                        for i, date in zip(value_list, dates):
                            if i.endswith('°N'):
                                image_paths.append(img['North'])
                                descriptions.append(i)
                                dates_to_display.append(
                                    date)  # added date to the list
                            elif i.endswith('°NE'):
                                image_paths.append(img['North-east'])
                                descriptions.append(i)
                                dates_to_display.append(
                                    date)  # added date to the list
                            elif i.endswith('°E'):
                                image_paths.append(img['East'])
                                descriptions.append(i)
                                dates_to_display.append(
                                    date)  # added date to the list
                            elif i.endswith('°SE'):
                                image_paths.append(img['South-east'])
                                descriptions.append(i)
                                dates_to_display.append(
                                    date)  # added date to the list
                            elif i.endswith('°S'):
                                image_paths.append(img['South'])
                                descriptions.append(i)
                                dates_to_display.append(
                                    date)  # added date to the list
                            elif i.endswith('°SW'):
                                image_paths.append(img['South-west'])
                                descriptions.append(i)
                                dates_to_display.append(
                                    date)  # added date to the list
                            elif i.endswith('°W'):
                                image_paths.append(img['West'])
                                descriptions.append(i)
                                dates_to_display.append(
                                    date)  # added date to the list
                            elif i.endswith('°NW'):
                                image_paths.append(img['North-west'])
                                descriptions.append(i)
                                dates_to_display.append(
                                    date)  # added date to the list

                        for i in range(num_rows):
                            cols = st.columns(num_cols)
                            for j in range(num_cols):
                                index = i * num_cols + j
                                if index < len(image_paths):
                                    cols[j].image(image_paths[index], width=50)
                                    cols[j].write(descriptions[index])
                                    cols[j].write(dates_to_display[index])
                    except TypeError:

                        st.header('Server error:'
                                  'Please try after 1 hour!')
                case "Minutely":
                    value_list = []
                    value_slider = st.slider('Data you want:', min_value=5,
                                      max_value=120)
                    try:
                        dates, values = bk.api_wind_direction(place, 'h')
                        dates = dates[:value_slider]
                        values = values[:value_slider]
                        ii = 0
                        for value in values:
                            if  0 >= value < 45:
                                value_list.append(f"{value}{u"\u00b0"}N")
                            elif 45 <= value < 90:
                                value_list.append(f"{value}{u"\u00b0"}NE")
                            elif 90 <= value < 135:
                                value_list.append(f"{value}{u"\u00b0"}E")
                            elif 135 <= value < 180:
                                value_list.append(f"{value}{u"\u00b0"}SE")
                            elif 180 <= value < 225:
                                value_list.append(f"{value}{u"\u00b0"}S")
                            elif 225 <= value < 270:
                                value_list.append(f"{value}{u"\u00b0"}SW")
                            elif 270 <= value < 310:
                                value_list.append(f"{value}{u"\u00b0"}W")
                            elif 310 <= value < 360:
                                value_list.append(f"{value}{u"\u00b0"}NW")
                        print(value_list)
                        num_cols = 5  # You can adjust this to have more or fewer columns
                        num_rows = (len(value_list) + num_cols - 1) // num_cols  # Calculate the number of rows

                        image_paths = []  # List to store image paths
                        descriptions = []  # List to store descriptions
                        dates_to_display = []  # List to store dates

                        for i, date in zip(value_list, dates):
                            if i.endswith('°N'):
                                image_paths.append(img['North'])
                                descriptions.append(i)
                                dates_to_display.append(
                                    date)  # added date to the list
                            elif i.endswith('°NE'):
                                image_paths.append(img['North-east'])
                                descriptions.append(i)
                                dates_to_display.append(
                                    date)  # added date to the list
                            elif i.endswith('°E'):
                                image_paths.append(img['East'])
                                descriptions.append(i)
                                dates_to_display.append(
                                    date)  # added date to the list
                            elif i.endswith('°SE'):
                                image_paths.append(img['South-east'])
                                descriptions.append(i)
                                dates_to_display.append(
                                    date)  # added date to the list
                            elif i.endswith('°S'):
                                image_paths.append(img['South'])
                                descriptions.append(i)
                                dates_to_display.append(
                                    date)  # added date to the list
                            elif i.endswith('°SW'):
                                image_paths.append(img['South-west'])
                                descriptions.append(i)
                                dates_to_display.append(
                                    date)  # added date to the list
                            elif i.endswith('°W'):
                                image_paths.append(img['West'])
                                descriptions.append(i)
                                dates_to_display.append(
                                    date)  # added date to the list
                            elif i.endswith('°NW'):
                                image_paths.append(img['North-west'])
                                descriptions.append(i)
                                dates_to_display.append(
                                    date)  # added date to the list

                        for i in range(num_rows):
                            cols = st.columns(num_cols)
                            for j in range(num_cols):
                                index = i * num_cols + j
                                if index < len(image_paths):
                                    cols[j].image(image_paths[index], width=50)
                                    cols[j].write(descriptions[index])
                                    cols[j].write(dates_to_display[index])
                    except TypeError:
                        st.header('Server error:'
                                  'Please try after 1 hour!')
