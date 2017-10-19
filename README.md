# rasp-home
domotic usage of the raspberry pi 3


cat /etc/wpa_supplicant/wpa_supplicant.conf 
country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
	ssid="ESSID"
	scan_ssid=1
	key_mgmt=WPA-PSK
	psk="PASSWORD"
}


sudo apt-get install virtualenv python-dev

virtualenv venv
source venv/bin/activate
pip install  -r requirements.txt 
