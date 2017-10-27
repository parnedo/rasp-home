#!/usr/bin/env python
import web
import config
from raspio import raspio

urls = (
    '/relay/switch_on/(.*)', 'switchon',
    '/relay/switch_off/(.*)', 'switchoff',
)

app = web.application(urls, globals())
gpio = raspio(config.ac_relay)
class switchon:        
    def GET(self,item):
	output = {}
	import datetime,time
	output['timestamp'] =  datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
	output['status'] = gpio.setPin(item)
        return str(output)

class switchoff:        
    def GET(self,item):
	output = {}
	import datetime,time
	output['timestamp'] =  datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
	output['status'] = gpio.unsetPin(item)
        return str(output)

if __name__ == "__main__":
    app.run()

