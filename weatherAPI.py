import pyowm,sys

owm = pyowm.OWM('82d9778432f8232da399da4b4f4c817d')

if len(sys.argv) > 1:
        # Get address from command line.
        location = ' '.join(sys.argv[1:])
else:
	location = "Houston,tx"

forecast = owm.daily_forecast(location)
tomorrow = pyowm.timeutils.tomorrow()
forecast.will_be_sunny_at(tomorrow)

observation = owm.weather_at_place(location)
w = observation.get_weather()
#print(w)
print '\n'
print 'Location: ', location
print 'wind speed: ' , w.get_wind()['speed']
print 'wind degree: ', w.get_wind()['deg']
#print 'temp: ' , w.get_temperature('fahrenheit')
print 'current temp: ' , w.get_temperature('fahrenheit')['temp'] , ' F'
print '\t' ,'high: ',w.get_temperature('fahrenheit')['temp_max'] , '   low: ', w.get_temperature('fahrenheit')['temp_min']
print '\n'

