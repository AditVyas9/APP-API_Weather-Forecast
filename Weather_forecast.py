import streamlit as st
import plotly.express as px
import backend as bk
import pandas as pd

st.set_page_config(initial_sidebar_state="expanded")

st.header('Weather Forecast App')

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
	"1000": "Clear",
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
	   "East": 'images/east.png',
	   "North-west": 'images/northwest.png',
	   "North-east": 'images/northeast.png',
	   }

col1, nun, col2 = st.columns([1.5, 0.5, 1.5])
with col1:
	raw_place = st.text_input('Place:', help="Format-(City, State, Country) or (City, State) or (City, Country)",
							  placeholder="Enter place in format...(hover mouse over help icon)")
	option3 = st.selectbox("Format of Time:", (
	"Universal Time Co-ordinated or Greenwich Meridian Time", "Local Time"),
						   index=None,
						   placeholder="In which format time you want...")

with col2:
	option = st.selectbox("Select data to view", ("Temperature", "UV Index",
												  "Visibility", "Humidity",
												  "Sky Conditions",
												  "Wind Speed",
												  "Wind Gust",
												  "Wind Direction",
												  "AQI(PM₁₀, PM₂.₅)"),
						  index=None,
						  placeholder="Data you want to view...")



col1, col2 = st.columns(2)


if raw_place and option is not None and option3 is not None:
	place = bk.exact(raw_place)
	if option3 == "Local Time":
		if option == "AQI(PM₁₀, PM₂.₅)":
			st.subheader(f"{option} in {raw_place.title()}",
						 help="""You can scroll the graph.""")
			try:
				latitude, longitude = str(place).split(',')
				content = bk.aqi(float(latitude), float(longitude))
				dates = content[0]
				pm2_5= content[1]
				pm10 = content[2]
				dates = bk.local_time(latitude, longitude, dates)
				df = pd.DataFrame({
					'Dates': dates,
					'PM₂.₅': pm2_5,
					'PM₁₀': pm10
				})
				df_long = pd.melt(df, id_vars=['Dates'],
								  value_vars=['PM₂.₅', 'PM₁₀'],
								  var_name='Key', value_name='AQI(PM₁₀, PM₂.₅)')

				figure = px.line(df_long, x='Dates', y='AQI(PM₁₀, PM₂.₅)',
								 color='Key',
								 custom_data=['Key']
								 )
				figure.update_xaxes(tickmode="auto", nticks=12)
				figure.update_xaxes(ticksuffix="   ")
				figure.update_yaxes(ticksuffix="   ")
				figure.update_traces(hovertemplate="Time: %{x}<br> %{customdata[0]}: %{y}")
				st.plotly_chart(figure)
				

			except TypeError:
				st.header('Server error:'
						  'Please try after 1 hour!')
		else:
			option_2 = st.selectbox("Select frequency:",
									("Daily", "Hourly", "Minutely"),
									index=None,
									placeholder="Frequency you want...",
									)
			if option_2 is not None:
				st.subheader(f"{option} in {raw_place.title()}", help="""You can scroll the graph.""")
				match option:
					case "Temperature":
						match option_2:
							case "Daily":
								try:
									dates, temp = bk.api_day(place, 'd')
									latitude, longitude = place.split(',')
									dates = bk.local_time(latitude, longitude, dates)
									figure = px.line(x=dates, y=temp, labels={"x": "Time",
																			  "y": f"Temperature({u"\u00b0"}C)"})
									figure.update_xaxes(tickmode="auto", nticks=12)
									figure.update_xaxes(ticksuffix="   ")
									figure.update_yaxes(ticksuffix="   ")
									figure.update_traces(hovertemplate='Time: %{x}<br>Temperature: %{y}°C')
									st.plotly_chart(figure_or_data=figure)
									
								except TypeError:
									st.header('Server error:'
											  'Please try after 1 hour!')
							case "Hourly":
								try:
									dates, temp = bk.api_day(place, 'h')
									latitude, longitude = place.split(',')
									dates = bk.local_time(latitude, longitude,
														 dates)
									figure = px.line(x=dates, y=temp, labels={"x": "Time",
																			  "y": f"Temperature({u"\u00b0"}C)"})

									figure.update_xaxes(tickmode="auto", nticks=12)
									figure.update_xaxes(ticksuffix="   ")
									figure.update_yaxes(ticksuffix="   ")
									figure.update_traces(hovertemplate='Time: %{x}<br>Temperature: %{y}°C')
									st.plotly_chart(figure_or_data=figure)
									
								except TypeError:

									st.header('Server error:'
											  'Please try after 1 hour!')
							case "Minutely":
								try:
									dates, temp = bk.api_day(place, 'm')
									latitude, longitude = place.split(',')
									dates = bk.local_time(latitude, longitude,
														 dates)
									figure = px.line(x=dates, y=temp, labels={"x": "Time",
																			  "y": f"Temperature({u"\u00b0"}C)"})
									figure.update_xaxes(tickmode="auto", nticks=12)
									figure.update_xaxes(ticksuffix="   ")
									figure.update_traces(hovertemplate='Time: %{x}<br>Temperature: %{y}°C')

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
									latitude, longitude = place.split(',')
									dates = bk.local_time(latitude, longitude,
														 dates)
									figure = px.line(x=dates, y=temp, labels={"x": "Time",
																			  "y": f"UV Index(mW/m{'\u00b2'})"})
									figure.update_traces(hovertemplate='Time: %{x}<br>UV Index: %{y}mW/m²')
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
									latitude, longitude = place.split(',')
									dates = bk.local_time(latitude, longitude,
														 dates)
									figure = px.line(x=dates, y=temp, labels={"x": "Time",
																			  "y": f"UV Index(mW/m{'\u00b2'})"})
									figure.update_xaxes(tickmode="auto", nticks=12)
									figure.update_traces(hovertemplate='Time: %{x}<br>UV Index: %{y}mW/m²')

									figure.update_xaxes(ticksuffix="   ")
									figure.update_yaxes(ticksuffix="   ")
									st.plotly_chart(figure_or_data=figure)
								except TypeError:

									st.header('Server error:'
											  'Please try after 1 hour!')
							case "Minutely":
								try:
									dates, temp = bk.api_uv_index(place, 'm')
									latitude, longitude = place.split(',')
									dates = bk.local_time(latitude, longitude,
														 dates)
									figure = px.line(x=dates, y=temp, labels={"x": "Time",
																			  "y": f"UV Index(mW/m{'\u00b2'})"})
									figure.update_xaxes(tickmode="auto", nticks=12)
									figure.update_traces(hovertemplate='Time: %{x}<br>UV Index: %{y}mW/m²')

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
									latitude, longitude = place.split(',')
									dates = bk.local_time(latitude, longitude,
														 dates)
									figure = px.line(x=dates, y=temp, labels={"x": "Time",
																			  "y": f"Visibility(km)"})
									figure.update_xaxes(tickmode="auto", nticks=12)
									figure.update_traces(hovertemplate='Time: %{x}<br>Visibility: %{y}km')

									figure.update_xaxes(ticksuffix="   ")
									figure.update_yaxes(ticksuffix="   ")
									st.plotly_chart(figure_or_data=figure)
								except TypeError:

									st.header('Server error:'
											  'Please try after 1 hour!')
							case "Hourly":
								try:
									dates, temp = bk.api_visibility(place, 'h')
									latitude, longitude = place.split(',')
									dates = bk.local_time(latitude, longitude,
														 dates)
									figure = px.line(x=dates, y=temp, labels={"x": "Time",
																			  "y": f"Visibility(km)"})
									figure.update_xaxes(tickmode="auto", nticks=12)
									figure.update_traces(hovertemplate='Time: %{x}<br>Visibility: %{y}km')

									figure.update_xaxes(ticksuffix="   ")
									figure.update_yaxes(ticksuffix="   ")
									st.plotly_chart(figure_or_data=figure)
								except TypeError:

									st.header('Server error:'
											  'Please try after 1 hour!')
							case "Minutely":
								try:
									dates, temp = bk.api_visibility(place, 'm')
									latitude, longitude = place.split(',')
									dates = bk.local_time(latitude, longitude,
														 dates)
									figure = px.line(x=dates, y=temp, labels={"x": "Time",
																			  "y": f"Visibility(km)"})
									figure.update_xaxes(tickmode="auto", nticks=12)
									figure.update_traces(hovertemplate='Time: %{x}<br>Visibility: %{y}km')

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
									latitude, longitude = place.split(',')
									dates = bk.local_time(latitude, longitude,
														 dates)
									figure = px.line(x=dates, y=temp, labels={"x": "Time",
																			  "y": f"Humidity(%)"})
									figure.update_xaxes(tickmode="auto", nticks=12)
									figure.update_traces(hovertemplate='Time: %{x}<br>Humidity: %{y}%')

									figure.update_xaxes(ticksuffix="   ")
									figure.update_yaxes(ticksuffix="   ")
									st.plotly_chart(figure_or_data=figure)
								except TypeError:

									st.header('Server error:'
											  'Please try after 1 hour!')
							case "Hourly":
								try:
									dates, temp = bk.api_humidity(place, 'h')
									latitude, longitude = place.split(',')
									dates = bk.local_time(latitude, longitude,
														 dates)
									figure = px.line(x=dates, y=temp, labels={"x": "Time",
																			  "y": f"Humidity(%)"})
									figure.update_xaxes(tickmode="auto", nticks=12)
									figure.update_traces(hovertemplate='Time: %{x}<br>Humidity: %{y}%')

									figure.update_xaxes(ticksuffix="   ")
									figure.update_yaxes(ticksuffix="   ")
									st.plotly_chart(figure_or_data=figure)
								except TypeError:

									st.header('Server error:'
											  'Please try after 1 hour!')
							case "Minutely":
								try:
									dates, temp = bk.api_humidity(place, 'm')
									latitude, longitude = place.split(',')
									dates = bk.local_time(latitude, longitude,
														 dates)
									figure = px.line(x=dates, y=temp, labels={"x": "Time",
																			  "y": f"Humidity(%)"})
									figure.update_xaxes(tickmode="auto", nticks=12)
									figure.update_traces(hovertemplate='Time: %{x}<br>Humidity: %{y}%')

									figure.update_xaxes(ticksuffix="   ")
									figure.update_yaxes(ticksuffix="   ")
									st.plotly_chart(figure_or_data=figure)
								except TypeError:

									st.header('Server error:'
											  'Please try after 1 hour!')
					case "Sky Conditions":

						match option_2:
							case "Daily":
								try:
									dates, codes = bk.api_weather_code(place, 'd')
									latitude, longitude = place.split(',')
									dates = bk.local_time(latitude, longitude,
														 dates)
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
								value = st.slider('Data:', min_value=5, max_value=120, help="Number of data you want.")
								try:
									dates, codes = bk.api_weather_code(place, 'h')
									latitude, longitude = place.split(',')
									dates = bk.local_time(latitude, longitude,
														 dates)
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
								value = st.slider('Data you want:', min_value=5, max_value=120, help="Number of data you want.")
								try:
									dates, codes = bk.api_weather_code(place, 'm')
									latitude, longitude = place.split(',')
									dates = bk.local_time(latitude, longitude,
														 dates)
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
									latitude, longitude = place.split(',')
									dates = bk.local_time(latitude, longitude,
														 dates)
									figure = px.line(x=dates, y=temp, labels={
										"x": "Time",
										"y": f"Dew point({u"\u00b0"}C)"},hover_templates='Time: %{x}<br>Dew point: %{y}°C')
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
									latitude, longitude = place.split(',')
									dates = bk.local_time(latitude, longitude,
														 dates)
									figure = px.line(x=dates, y=temp, labels={
										"x": "Time",
										"y": f"Dew point({u"\u00b0"}C)"},hover_templates='Time: %{x}<br>Dew point: %{y}°C')
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
									latitude, longitude = place.split(',')
									dates = bk.local_time(latitude, longitude,
														 dates)
									figure = px.line(x=dates, y=temp, labels={
										"x": "Time",
										"y": f"Dew point({u"\u00b0"}C)"},hover_templates='Time: %{x}<br>Dew point: %{y}°C')
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
									latitude, longitude = place.split(',')
									dates = bk.local_time(latitude, longitude,
														 dates)
									figure = px.line(x=dates, y=temp, labels={
										"x": "Time",
										"y": f"Surface Pressure(hPa)"},hover_templates='Time: %{x}<br>Surface Pressure: %{y} hPa')
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
									latitude, longitude = place.split(',')
									dates = bk.local_time(latitude, longitude,
														 dates)
									figure = px.line(x=dates, y=temp, labels={
										"x": "Time",
										"y": f"Surface Pressure(hPa)"},hover_templates='Time: %{x}<br>Surface Pressure: %{y} hPa')
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
									latitude, longitude = place.split(',')
									dates = bk.local_time(latitude, longitude,
														 dates)
									figure = px.line(x=dates, y=temp, labels={
										"x": "Time",
										"y": f"Surface Pressure(hPa)"},hover_templates='Time: %{x}<br>Surface Pressure: %{y} hPa')
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
									latitude, longitude = place.split(',')
									dates = bk.local_time(latitude, longitude,
														 dates)
									figure = px.line(x=dates, y=temp, labels={
										"x": "Time",
										"y": f"Wind Speed(m/s)"})
									figure.update_xaxes(tickmode="auto", nticks=12)
									figure.update_traces(hovertemplate='Time: %{x}<br>Wind Speed: %{y}m/s')

									figure.update_xaxes(ticksuffix="   ")
									figure.update_yaxes(ticksuffix="   ")
									st.plotly_chart(figure_or_data=figure)
								except TypeError:

									st.header('Server error:'
											  'Please try after 1 hour!')
							case "Hourly":
								try:
									dates, temp = bk.api_wind_speed(place, 'h')
									latitude, longitude = place.split(',')
									dates = bk.local_time(latitude, longitude,
														 dates)
									figure = px.line(x=dates, y=temp, labels={
										"x": "Time",
										"y": f"Wind Speed(m/s)"})
									figure.update_xaxes(tickmode="auto", nticks=12)
									figure.update_traces(hovertemplate='Time: %{x}<br>Wind Speed: %{y}m/s')

									figure.update_xaxes(ticksuffix="   ")
									figure.update_yaxes(ticksuffix="   ")
									st.plotly_chart(figure_or_data=figure)
								except TypeError:

									st.header('Server error:'
											  'Please try after 1 hour!')
							case "Minutely":
								try:
									dates, temp = bk.api_wind_speed(place, 'm')
									latitude, longitude = place.split(',')
									dates = bk.local_time(latitude, longitude,
														 dates)
									figure = px.line(x=dates, y=temp, labels={
										"x": "Time",
										"y": f"Wind Speed(m/s)"})
									figure.update_traces(hovertemplate='Time: %{x}<br>Wind Speed: %{y}m/s')
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
									latitude, longitude = place.split(',')
									dates = bk.local_time(latitude, longitude,
														 dates)
									figure = px.line(x=dates, y=temp, labels={
										"x": "Time",
										"y": f"Wind Gust(m/s)"})
									figure.update_xaxes(tickmode="auto", nticks=12)
									figure.update_traces(hovertemplate='Time: %{x}<br>Wind Gust: %{y}m/s')

									figure.update_xaxes(ticksuffix="   ")
									figure.update_yaxes(ticksuffix="   ")
									st.plotly_chart(figure_or_data=figure)
								except TypeError:

									st.header('Server error:'
											  'Please try after 1 hour!')
							case "Hourly":
								try:
									dates, temp = bk.api_wind_gust(place, 'h')
									latitude, longitude = place.split(',')
									dates = bk.local_time(latitude, longitude,
														 dates)
									figure = px.line(x=dates, y=temp, labels={
										"x": "Time",
										"y": f"Wind Gust(m/s)"})
									figure.update_xaxes(tickmode="auto", nticks=12)
									figure.update_traces(hovertemplate='Time: %{x}<br>Wind Gust: %{y}m/s')

									figure.update_xaxes(ticksuffix="   ")
									figure.update_yaxes(ticksuffix="   ")
									st.plotly_chart(figure_or_data=figure)
								except TypeError:

									st.header('Server error:'
											  'Please try after 1 hour!')
							case "Minutely":
								try:
									dates, temp = bk.api_wind_gust(place, 'm')
									latitude, longitude = place.split(',')
									dates = bk.local_time(latitude, longitude,
														 dates)
									figure = px.line(x=dates, y=temp, labels={
										"x": "Time",
										"y": f"Wind Gust(m/s)"})
									figure.update_traces(hovertemplate='Time: %{x}<br>Wind Gust: %{y}m/s')
									figure.update_xaxes(tickmode="auto", nticks=12)
									figure.update_xaxes(ticksuffix="   ")
									figure.update_yaxes(ticksuffix="   ")
									st.plotly_chart(figure_or_data=figure)
								except TypeError:

									st.header('Server error:'
											  'Please try after 1 hour!')
					case "Wind Direction":

						match option_2:
							case "Daily":
								value_list = []
								try:
									dates, values = bk.api_wind_direction(place, 'd')
									latitude, longitude = place.split(',')
									dates = bk.local_time(latitude, longitude,
														 dates)
									ii = 0
									for value in values:
										if  0 == value or value == 360:
											value_list.append(f"{value}{u"\u00b0"}N")
										elif 1 <= value < 90:
											value_list.append(f"{value}{u"\u00b0"}NE")
										elif 90 == value:
											value_list.append(f"{value}{u"\u00b0"}E")
										elif 91 <= value < 180:
											value_list.append(f"{value}{u"\u00b0"}SE")
										elif value == 180:
											value_list.append(f"{value}{u"\u00b0"}S")
										elif 181 <= value < 270:
											value_list.append(f"{value}{u"\u00b0"}SW")
										elif value == 270:
											value_list.append(f"{value}{u"\u00b0"}W")
										elif 271 <= value < 360:
											value_list.append(f"{value}{u"\u00b0"}NW")
									num_cols = 5
									num_rows = (len(value_list) + num_cols - 1) // num_cols

									image_paths = []
									descriptions = []
									dates_to_display = []

									for i, date in zip(value_list, dates):
										if i.endswith('°N'):
											image_paths.append(img['North'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°NE'):
											image_paths.append(img['North-east'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°E'):
											image_paths.append(img['East'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°SE'):
											image_paths.append(img['South-east'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°S'):
											image_paths.append(img['South'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°SW'):
											image_paths.append(img['South-west'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°W'):
											image_paths.append(img['West'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°NW'):
											image_paths.append(img['North-west'])
											descriptions.append(i)
											dates_to_display.append(date)

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
								value_slider = st.slider('Data you want:', min_value=5, max_value=120, help="Number of data you want.")
								value_list = []

								try:
									dates, values = bk.api_wind_direction(place, 'h')
									latitude, longitude = place.split(',')
									dates = bk.local_time(latitude, longitude,
														 dates)
									dates = dates[:value_slider]
									values = values[:value_slider]
									ii = 0
									for value in values:
										if  0 == value or value == 360:
											value_list.append(f"{value}{u"\u00b0"}N")
										elif 1 <= value < 90:
											value_list.append(f"{value}{u"\u00b0"}NE")
										elif 90 == value:
											value_list.append(f"{value}{u"\u00b0"}E")
										elif 91 <= value < 180:
											value_list.append(f"{value}{u"\u00b0"}SE")
										elif value == 180:
											value_list.append(f"{value}{u"\u00b0"}S")
										elif 181 <= value < 270:
											value_list.append(f"{value}{u"\u00b0"}SW")
										elif value == 270:
											value_list.append(f"{value}{u"\u00b0"}W")
										elif 271 <= value < 360:
											value_list.append(f"{value}{u"\u00b0"}NW")
									num_cols = 5
									num_rows = (len(value_list) + num_cols - 1) // num_cols

									image_paths = []
									descriptions = []
									dates_to_display = []

									for i, date in zip(value_list, dates):
										if i.endswith('°N'):
											image_paths.append(img['North'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°NE'):
											image_paths.append(img['North-east'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°E'):
											image_paths.append(img['East'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°SE'):
											image_paths.append(img['South-east'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°S'):
											image_paths.append(img['South'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°SW'):
											image_paths.append(img['South-west'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°W'):
											image_paths.append(img['West'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°NW'):
											image_paths.append(img['North-west'])
											descriptions.append(i)
											dates_to_display.append(date)

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
								value_slider = st.slider('Data you want:', min_value=5, max_value=120, help="Number of data you want.")
								try:
									dates, values = bk.api_wind_direction(place, 'h')
									latitude, longitude = place.split(',')
									dates = bk.local_time(latitude, longitude,
														 dates)
									dates = dates[:value_slider]
									values = values[:value_slider]
									ii = 0
									for value in values:
										if  0 == value or value == 360:
											value_list.append(f"{value}{u"\u00b0"}N")
										elif 1 <= value < 90:
											value_list.append(f"{value}{u"\u00b0"}NE")
										elif 90 == value:
											value_list.append(f"{value}{u"\u00b0"}E")
										elif 91 <= value < 180:
											value_list.append(f"{value}{u"\u00b0"}SE")
										elif value == 180:
											value_list.append(f"{value}{u"\u00b0"}S")
										elif 181 <= value < 270:
											value_list.append(f"{value}{u"\u00b0"}SW")
										elif value == 270:
											value_list.append(f"{value}{u"\u00b0"}W")
										elif 271 <= value < 360:
											value_list.append(f"{value}{u"\u00b0"}NW")
									num_cols = 5
									num_rows = (len(value_list) + num_cols - 1) // num_cols

									image_paths = []
									descriptions = []
									dates_to_display = []

									for i, date in zip(value_list, dates):
										if i.endswith('°N'):
											image_paths.append(img['North'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°NE'):
											image_paths.append(img['North-east'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°E'):
											image_paths.append(img['East'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°SE'):
											image_paths.append(img['South-east'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°S'):
											image_paths.append(img['South'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°SW'):
											image_paths.append(img['South-west'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°W'):
											image_paths.append(img['West'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°NW'):
											image_paths.append(img['North-west'])
											descriptions.append(i)
											dates_to_display.append(date)

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
	else:
		if option == "AQI(PM₁₀, PM₂.₅)":
			st.subheader(f"{option} in {raw_place.title()}",
						 help="""You can scroll the graph.""")
			try:
				lat, lon = place.split(',')
				raw_d = bk.aqi(float(lat), float(lon))
				dates = raw_d[0]
				pm2_5 = raw_d[1]
				pm10 = raw_d[2]
				df = pd.DataFrame({
					'Dates': dates,
					'PM₂.₅': pm2_5,
					'PM₁₀': pm10
				})
				df_long = pd.melt(df, id_vars=['Dates'],
								  value_vars=['PM₂.₅', 'PM₁₀'],
								  var_name='Key',
								  value_name='AQI(PM₁₀, PM₂.₅)')

				figure = px.line(df_long, x='Dates', y='AQI(PM₁₀, PM₂.₅)',
								 color='Key',
								 custom_data=['Key']
								 )
				figure.update_xaxes(tickmode="auto", nticks=12)
				figure.update_xaxes(ticksuffix="   ")
				figure.update_yaxes(ticksuffix="   ")
				figure.update_traces(
					hovertemplate="Time: %{x}<br> %{customdata[0]}: %{y}")
				st.plotly_chart(figure)
			except TypeError:
				st.header('Server error:'
						  'Please try after 1 hour!')
		else:
			option_2 = st.selectbox("Select frequency:",
									("Daily", "Hourly", "Minutely"),
									index=None,
									placeholder="Frequency you want...",
									)
			if option_2 is not None:
				st.subheader(f"{option} in {raw_place.title()}", help="""You can scroll the graph.    
				All Dates and time are in Universal Time Coordinated-UTC""")
				match option:
					case "Temperature":
						match option_2:
							case "Daily":
								try:
									dates, temp = bk.api_day(place, 'd')
									figure = px.line(x=dates, y=temp,
													 labels={"x": "Time",
															 "y": f"Temperature({u"\u00b0"}C)"})
									figure.update_xaxes(tickmode="auto",
														nticks=12)
									figure.update_xaxes(ticksuffix="   ")
									figure.update_yaxes(ticksuffix="   ")
									figure.update_traces(
										hovertemplate='Time: %{x}<br>Temperature: %{y}°C')
									st.plotly_chart(figure_or_data=figure)
								except TypeError:
									st.header('Server error:'
											  'Please try after 1 hour!')
							case "Hourly":
								try:
									dates, temp = bk.api_day(place, 'h')
									figure = px.line(x=dates, y=temp,
													 labels={"x": "Time",
															 "y": f"Temperature({u"\u00b0"}C)"})

									figure.update_xaxes(tickmode="auto",
														nticks=12)
									figure.update_xaxes(ticksuffix="   ")
									figure.update_yaxes(ticksuffix="   ")
									figure.update_traces(
										hovertemplate='Time: %{x}<br>Temperature: %{y}°C')

									st.plotly_chart(figure_or_data=figure)
								except TypeError:

									st.header('Server error:'
											  'Please try after 1 hour!')
							case "Minutely":
								try:
									dates, temp = bk.api_day(place, 'm')
									figure = px.line(x=dates, y=temp,
													 labels={"x": "Time",
															 "y": f"Temperature({u"\u00b0"}C)"})
									figure.update_xaxes(tickmode="auto",
														nticks=12)
									figure.update_xaxes(ticksuffix="   ")
									figure.update_traces(
										hovertemplate='Time: %{x}<br>Temperature: %{y}°C')

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
									figure = px.line(x=dates, y=temp,
													 labels={"x": "Time",
															 "y": f"UV Index(mW/m{'\u00b2'})"})
									figure.update_traces(
										hovertemplate='Time: %{x}<br>UV Index: %{y}mW/m²')
									figure.update_xaxes(tickmode="auto",
														nticks=12)
									figure.update_xaxes(ticksuffix="   ")
									figure.update_yaxes(ticksuffix="   ")
									st.plotly_chart(figure_or_data=figure)
								except TypeError:

									st.header('Server error:'
											  'Please try after 1 hour!')
							case "Hourly":
								try:
									dates, temp = bk.api_uv_index(place, 'h')
									figure = px.line(x=dates, y=temp,
													 labels={"x": "Time",
															 "y": f"UV Index(mW/m{'\u00b2'})"})
									figure.update_xaxes(tickmode="auto",
														nticks=12)
									figure.update_traces(
										hovertemplate='Time: %{x}<br>UV Index: %{y}mW/m²')

									figure.update_xaxes(ticksuffix="   ")
									figure.update_yaxes(ticksuffix="   ")
									st.plotly_chart(figure_or_data=figure)
								except TypeError:

									st.header('Server error:'
											  'Please try after 1 hour!')
							case "Minutely":
								try:
									dates, temp = bk.api_uv_index(place, 'm')
									figure = px.line(x=dates, y=temp,
													 labels={"x": "Time",
															 "y": f"UV Index(mW/m{'\u00b2'})"})
									figure.update_xaxes(tickmode="auto",
														nticks=12)
									figure.update_traces(
										hovertemplate='Time: %{x}<br>UV Index: %{y}mW/m²')

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
									figure = px.line(x=dates, y=temp,
													 labels={"x": "Time",
															 "y": f"Visibility(km)"})
									figure.update_xaxes(tickmode="auto",
														nticks=12)
									figure.update_traces(
										hovertemplate='Time: %{x}<br>Visibility: %{y}km')

									figure.update_xaxes(ticksuffix="   ")
									figure.update_yaxes(ticksuffix="   ")
									st.plotly_chart(figure_or_data=figure)
								except TypeError:

									st.header('Server error:'
											  'Please try after 1 hour!')
							case "Hourly":
								try:
									dates, temp = bk.api_visibility(place, 'h')
									figure = px.line(x=dates, y=temp,
													 labels={"x": "Time",
															 "y": f"Visibility(km)"})
									figure.update_xaxes(tickmode="auto",
														nticks=12)
									figure.update_traces(
										hovertemplate='Time: %{x}<br>Visibility: %{y}km')

									figure.update_xaxes(ticksuffix="   ")
									figure.update_yaxes(ticksuffix="   ")
									st.plotly_chart(figure_or_data=figure)
								except TypeError:

									st.header('Server error:'
											  'Please try after 1 hour!')
							case "Minutely":
								try:
									dates, temp = bk.api_visibility(place, 'm')
									figure = px.line(x=dates, y=temp,
													 labels={"x": "Time",
															 "y": f"Visibility(km)"})
									figure.update_xaxes(tickmode="auto",
														nticks=12)
									figure.update_traces(
										hovertemplate='Time: %{x}<br>Visibility: %{y}km')

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
									figure = px.line(x=dates, y=temp,
													 labels={"x": "Time",
															 "y": f"Humidity(%)"})
									figure.update_xaxes(tickmode="auto",
														nticks=12)
									figure.update_traces(
										hovertemplate='Time: %{x}<br>Humidity: %{y}%')

									figure.update_xaxes(ticksuffix="   ")
									figure.update_yaxes(ticksuffix="   ")
									st.plotly_chart(figure_or_data=figure)
								except TypeError:

									st.header('Server error:'
											  'Please try after 1 hour!')
							case "Hourly":
								try:
									dates, temp = bk.api_humidity(place, 'h')
									figure = px.line(x=dates, y=temp,
													 labels={"x": "Time",
															 "y": f"Humidity(%)"})
									figure.update_xaxes(tickmode="auto",
														nticks=12)
									figure.update_traces(
										hovertemplate='Time: %{x}<br>Humidity: %{y}%')

									figure.update_xaxes(ticksuffix="   ")
									figure.update_yaxes(ticksuffix="   ")
									st.plotly_chart(figure_or_data=figure)
								except TypeError:
									st.header('Server error:'
											  'Please try after 1 hour!')
							case "Minutely":
								try:
									dates, temp = bk.api_humidity(place, 'm')

									figure = px.line(x=dates, y=temp,
													 labels={"x": "Time",
															 "y": f"Humidity(%)"})
									figure.update_xaxes(tickmode="auto",
														nticks=12)
									figure.update_traces(
										hovertemplate='Time: %{x}<br>Humidity: %{y}%')

									figure.update_xaxes(ticksuffix="   ")
									figure.update_yaxes(ticksuffix="   ")
									st.plotly_chart(figure_or_data=figure)
								except TypeError:

									st.header('Server error:'
											  'Please try after 1 hour!')
					case "Sky Conditions":
						match option_2:
							case "Daily":
								try:
									dates, codes = bk.api_weather_code(place,
																	   'd')
									image_paths = [images[condition] for
												   condition in codes]
									description = [weather_code[condition] for
												   condition in codes]
									num_cols = 5
									num_rows = (
														   len(image_paths) + num_cols - 1) // num_cols

									for i in range(num_rows):
										cols = st.columns(num_cols)
										for j in range(num_cols):
											index = i * num_cols + j
											if index < len(image_paths):
												cols[j].image(
													image_paths[index],
													width=50)
												cols[j].write(
													description[index])
												cols[j].write(dates[index])

								except TypeError:

									st.header('Server error:'
											  'Please try after 1 hour!')
							case "Hourly":
								value = st.slider('Data:', min_value=5,
												  max_value=120,
												  help="Number of data you want.")
								try:
									dates, codes = bk.api_weather_code(place,
																	   'h')
									dates = dates[:value]
									image_paths = [images[condition] for
												   condition in codes][:value]
									description = [weather_code[condition] for
												   condition in codes][:value]
									num_cols = 5
									num_rows = (
														   len(image_paths) + num_cols - 1) // num_cols

									for i in range(num_rows):
										cols = st.columns(num_cols)
										for j in range(num_cols):
											index = i * num_cols + j
											if index < len(image_paths):
												cols[j].image(
													image_paths[index],
													width=50)
												cols[j].write(
													description[index])
												cols[j].write(dates[index])

								except TypeError:

									st.header('Server error:'
											  'Please try after 1 hour!')
							case "Minutely":
								value = st.slider('Data you want:',
												  min_value=5, max_value=120,
												  help="Number of data you want.")
								try:
									dates, codes = bk.api_weather_code(place,
																	   'm')
									dates = dates[:value]
									image_paths = [images[condition] for
												   condition in codes][:value]
									description = [weather_code[condition] for
												   condition in codes][:value]
									num_cols = 5
									num_rows = (
														   len(image_paths) + num_cols - 1) // num_cols

									for i in range(num_rows):
										cols = st.columns(num_cols)
										for j in range(num_cols):
											index = i * num_cols + j
											if index < len(image_paths):
												cols[j].image(
													image_paths[index],
													width=50)
												cols[j].write(
													description[index])
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
										"x": "Time",
										"y": f"Dew point({u"\u00b0"}C)"},
													 hover_templates='Time: %{x}<br>Dew point: %{y}°C')
									figure.update_xaxes(tickmode="auto",
														nticks=12)
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
										"x": "Time",
										"y": f"Dew point({u"\u00b0"}C)"},
													 hover_templates='Time: %{x}<br>Dew point: %{y}°C')
									figure.update_xaxes(tickmode="auto",
														nticks=12)
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
										"x": "Time",
										"y": f"Dew point({u"\u00b0"}C)"},
													 hover_templates='Time: %{x}<br>Dew point: %{y}°C')
									figure.update_xaxes(tickmode="auto",
														nticks=12)
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
									dates, temp = bk.api_surface_level(place,
																	   'd')
									figure = px.line(x=dates, y=temp, labels={
										"x": "Time",
										"y": f"Surface Pressure(hPa)"},
													 hover_templates='Time: %{x}<br>Surface Pressure: %{y} hPa')
									figure.update_xaxes(tickmode="auto",
														nticks=12)
									figure.update_xaxes(ticksuffix="   ")
									figure.update_yaxes(ticksuffix="   ")
									st.plotly_chart(figure_or_data=figure)
								except TypeError:

									st.header('Server error:'
											  'Please try after 1 hour!')
							case "Hourly":
								try:
									dates, temp = bk.api_surface_level(place,
																	   'h')
									figure = px.line(x=dates, y=temp, labels={
										"x": "Time",
										"y": f"Surface Pressure(hPa)"},
													 hover_templates='Time: %{x}<br>Surface Pressure: %{y} hPa')
									figure.update_xaxes(tickmode="auto",
														nticks=12)
									figure.update_xaxes(ticksuffix="   ")
									figure.update_yaxes(ticksuffix="   ")
									st.plotly_chart(figure_or_data=figure)
								except TypeError:

									st.header('Server error:'
											  'Please try after 1 hour!')
							case "Minutely":
								try:
									dates, temp = bk.api_surface_level(place,
																	   'm')
									figure = px.line(x=dates, y=temp, labels={
										"x": "Time",
										"y": f"Surface Pressure(hPa)"},
													 hover_templates='Time: %{x}<br>Surface Pressure: %{y} hPa')
									figure.update_xaxes(tickmode="auto",
														nticks=12)
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
										"x": "Time",
										"y": f"Wind Speed(m/s)"})
									figure.update_xaxes(tickmode="auto",
														nticks=12)
									figure.update_traces(
										hovertemplate='Time: %{x}<br>Wind Speed: %{y}m/s')

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
										"x": "Time",
										"y": f"Wind Speed(m/s)"})
									figure.update_xaxes(tickmode="auto",
														nticks=12)
									figure.update_traces(
										hovertemplate='Time: %{x}<br>Wind Speed: %{y}m/s')

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
										"x": "Time",
										"y": f"Wind Speed(m/s)"})
									figure.update_traces(
										hovertemplate='Time: %{x}<br>Wind Speed: %{y}m/s')
									figure.update_xaxes(tickmode="auto",
														nticks=12)

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
										"x": "Time",
										"y": f"Wind Gust(m/s)"})
									figure.update_xaxes(tickmode="auto",
														nticks=12)
									figure.update_traces(
										hovertemplate='Time: %{x}<br>Wind Gust: %{y}m/s')

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
										"x": "Time",
										"y": f"Wind Gust(m/s)"})
									figure.update_xaxes(tickmode="auto",
														nticks=12)
									figure.update_traces(
										hovertemplate='Time: %{x}<br>Wind Gust: %{y}m/s')

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
										"x": "Time",
										"y": f"Wind Gust(m/s)"})
									figure.update_traces(
										hovertemplate='Time: %{x}<br>Wind Gust: %{y}m/s')
									figure.update_xaxes(tickmode="auto",
														nticks=12)
									figure.update_xaxes(ticksuffix="   ")
									figure.update_yaxes(ticksuffix="   ")
									st.plotly_chart(figure_or_data=figure)
								except TypeError:

									st.header('Server error:'
											  'Please try after 1 hour!')
					case "Wind Direction":
						match option_2:
							case "Daily":
								value_list = []
								try:
									dates, values = bk.api_wind_direction(
										place, 'd')
									ii = 0
									for value in values:
										if 0 == value or value == 360:
											value_list.append(
												f"{value}{u"\u00b0"}N")
										elif 1 <= value < 90:
											value_list.append(
												f"{value}{u"\u00b0"}NE")
										elif 90 == value:
											value_list.append(
												f"{value}{u"\u00b0"}E")
										elif 91 <= value < 180:
											value_list.append(
												f"{value}{u"\u00b0"}SE")
										elif value == 180:
											value_list.append(
												f"{value}{u"\u00b0"}S")
										elif 181 <= value < 270:
											value_list.append(
												f"{value}{u"\u00b0"}SW")
										elif value == 270:
											value_list.append(
												f"{value}{u"\u00b0"}W")
										elif 271 <= value < 360:
											value_list.append(
												f"{value}{u"\u00b0"}NW")
									num_cols = 5
									num_rows = (
														   len(value_list) + num_cols - 1) // num_cols

									image_paths = []
									descriptions = []
									dates_to_display = []

									for i, date in zip(value_list, dates):
										if i.endswith('°N'):
											image_paths.append(img['North'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°NE'):
											image_paths.append(
												img['North-east'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°E'):
											image_paths.append(img['East'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°SE'):
											image_paths.append(
												img['South-east'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°S'):
											image_paths.append(img['South'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°SW'):
											image_paths.append(
												img['South-west'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°W'):
											image_paths.append(img['West'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°NW'):
											image_paths.append(
												img['North-west'])
											descriptions.append(i)
											dates_to_display.append(date)

									for i in range(num_rows):
										cols = st.columns(num_cols)
										for j in range(num_cols):
											index = i * num_cols + j
											if index < len(image_paths):
												cols[j].image(
													image_paths[index],
													width=50)
												cols[j].write(
													descriptions[index])
												cols[j].write(
													dates_to_display[index])
								except TypeError:
									st.header('Server error:'
											  'Please try after 1 hour!')
							case "Hourly":
								value_slider = st.slider('Data you want:',
														 min_value=5,
														 max_value=120,
														 help="Number of data you want.")
								value_list = []

								try:
									dates, values = bk.api_wind_direction(
										place, 'h')
									dates = dates[:value_slider]
									values = values[:value_slider]
									ii = 0
									for value in values:
										if 0 == value or value == 360:
											value_list.append(
												f"{value}{u"\u00b0"}N")
										elif 1 <= value < 90:
											value_list.append(
												f"{value}{u"\u00b0"}NE")
										elif 90 == value:
											value_list.append(
												f"{value}{u"\u00b0"}E")
										elif 91 <= value < 180:
											value_list.append(
												f"{value}{u"\u00b0"}SE")
										elif value == 180:
											value_list.append(
												f"{value}{u"\u00b0"}S")
										elif 181 <= value < 270:
											value_list.append(
												f"{value}{u"\u00b0"}SW")
										elif value == 270:
											value_list.append(
												f"{value}{u"\u00b0"}W")
										elif 271 <= value < 360:
											value_list.append(
												f"{value}{u"\u00b0"}NW")
									num_cols = 5
									num_rows = (
														   len(value_list) + num_cols - 1) // num_cols

									image_paths = []
									descriptions = []
									dates_to_display = []

									for i, date in zip(value_list, dates):
										if i.endswith('°N'):
											image_paths.append(img['North'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°NE'):
											image_paths.append(
												img['North-east'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°E'):
											image_paths.append(img['East'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°SE'):
											image_paths.append(
												img['South-east'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°S'):
											image_paths.append(img['South'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°SW'):
											image_paths.append(
												img['South-west'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°W'):
											image_paths.append(img['West'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°NW'):
											image_paths.append(
												img['North-west'])
											descriptions.append(i)
											dates_to_display.append(date)

									for i in range(num_rows):
										cols = st.columns(num_cols)
										for j in range(num_cols):
											index = i * num_cols + j
											if index < len(image_paths):
												cols[j].image(
													image_paths[index],
													width=50)
												cols[j].write(
													descriptions[index])
												cols[j].write(
													dates_to_display[index])
								except TypeError:

									st.header('Server error:'
											  'Please try after 1 hour!')
							case "Minutely":
								value_list = []
								value_slider = st.slider('Data you want:',
														 min_value=5,
														 max_value=120,
														 help="Number of data you want.")
								try:
									dates, values = bk.api_wind_direction(
										place, 'h')
									dates = dates[:value_slider]
									values = values[:value_slider]
									ii = 0
									for value in values:
										if 0 == value or value == 360:
											value_list.append(
												f"{value}{u"\u00b0"}N")
										elif 1 <= value < 90:
											value_list.append(
												f"{value}{u"\u00b0"}NE")
										elif 90 == value:
											value_list.append(
												f"{value}{u"\u00b0"}E")
										elif 91 <= value < 180:
											value_list.append(
												f"{value}{u"\u00b0"}SE")
										elif value == 180:
											value_list.append(
												f"{value}{u"\u00b0"}S")
										elif 181 <= value < 270:
											value_list.append(
												f"{value}{u"\u00b0"}SW")
										elif value == 270:
											value_list.append(
												f"{value}{u"\u00b0"}W")
										elif 271 <= value < 360:
											value_list.append(
												f"{value}{u"\u00b0"}NW")
									num_cols = 5
									num_rows = (
														   len(value_list) + num_cols - 1) // num_cols

									image_paths = []
									descriptions = []
									dates_to_display = []

									for i, date in zip(value_list, dates):
										if i.endswith('°N'):
											image_paths.append(img['North'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°NE'):
											image_paths.append(
												img['North-east'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°E'):
											image_paths.append(img['East'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°SE'):
											image_paths.append(
												img['South-east'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°S'):
											image_paths.append(img['South'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°SW'):
											image_paths.append(
												img['South-west'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°W'):
											image_paths.append(img['West'])
											descriptions.append(i)
											dates_to_display.append(date)
										elif i.endswith('°NW'):
											image_paths.append(
												img['North-west'])
											descriptions.append(i)
											dates_to_display.append(date)

									for i in range(num_rows):
										cols = st.columns(num_cols)
										for j in range(num_cols):
											index = i * num_cols + j
											if index < len(image_paths):
												cols[j].image(
													image_paths[index],
													width=50)
												cols[j].write(
													descriptions[index])
												cols[j].write(
													dates_to_display[index])
								except TypeError:
									st.header('Server error:'
											  'Please try after 1 hour!')

