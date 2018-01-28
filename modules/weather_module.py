from weather import Weather
import pycountry
import yweather

weather = Weather()
# Lookup via location name.
#country = pycountry.countries.get(name=location_name)

#allcountry = list(pycountry.countries)
#print(allcountry)
#location = weather.lookup_by_location(location_name)
#condition = location.units()
#condition['temperature'] = 'C'
#print(condition['temperature'])

def get_weather_at( location_input ):
	location = weather.lookup_by_location(location_input)
	condition = location.condition()
	print(location.atmosphere()['humidity'])
	print(location.atmosphere())
	print(location.wind())
	print(location.units())
	print(location.condition())
	text = condition.text()
	temp = condition.temp()
	result="weather is "+text+" and the temperature is around "+temp+"F"
	return result

	
