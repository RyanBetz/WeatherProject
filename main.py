#read files
humidity = pd.read_csv('humidity.csv')
temperature = pd.read_csv('temperature.csv')
pressure = pd.read_csv('pressure.csv')
weather_description = pd.read_csv('weather_description.csv')
wind_direction = pd.read_csv('wind_direction.csv')
wind_speed = pd.read_csv('wind_speed.csv')
#print the first 5 rows of the data
humidity.head()
temperature.head()
pressure.head()
weather_description.head()
wind_direction.head()
wind_speed.head()
#merge the data
weather = pd.merge(humidity, temperature, on='datetime')
weather = pd.merge(weather, pressure, on='datetime')
weather = pd.merge(weather, weather_description, on='datetime')
weather = pd.merge(weather, wind_direction, on='datetime')
weather = pd.merge(weather, wind_speed, on='datetime')


weather = pd.merge(weather, weather_description, on='datetime', suffixes= ('', '_weather_desc'))
weather = pd.merge(weather, wind_direction, on='datetime', suffixes=('', '_wind_direction'))
weather = pd.merge(weather, wind_speed, on='datetime', suffixes=('', '_wind_speed'))
weather = pd.merge(weather, pressure, on='datetime', suffixes=('', '_pressure'))