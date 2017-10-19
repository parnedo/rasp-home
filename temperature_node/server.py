#!/usr/bin/env python
import web
import config
from raspio import raspio

urls = (
    '/sensor/temperature', 'get_temperature',
)

app = web.application(urls, globals())
gpio = raspio(config.temperature)
class get_temperature:        
    def GET(self):
	output = {}
	import datetime,time
	output['timestamp'] =  datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
	output['degree'] = gpio.getPin('temperature')
        return str(output)

if __name__ == "__main__":
    app.run()

