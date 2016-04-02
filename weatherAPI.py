import pyowm,sys,API

owm = pyowm.OWM(API.api_key)

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

