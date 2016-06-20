import pyowm,sys,API

#Create API.py in same directory and add api_key = '_______' .  You must get your API key from openweathermap.org
#Need to have python 2.x installed locally on machine, also install pip, then sudo pip install pyowm
owm = pyowm.OWM(API.api_key)

try:
	if len(sys.argv) > 1:
        	# Get address from command line.
        	location = ' '.join(sys.argv[1:])
	else:
		location = "Houston,tx"
		print "Using Houston TX as an example"
		print "change location example: python weatherAPI.py Memphis,TN"
except:
	print "example Houston,tx ... Memphis,TN"

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
