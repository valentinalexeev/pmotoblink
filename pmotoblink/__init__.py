import requests

BASE_COMMAND_URL_FORMAT = "http://{}/?action=command&command={}"
BASE_COMMAND_VALUE_URL_FORMAT = BASE_COMMAND_URL_FORMAT + "&value={}"

class MotoBlink():
	def __init__(self, address):
		self._address = address

	def send_command(self, command, value = None):
		url = None
		if value:
			url = BASE_COMMAND_VALUE_URL_FORMAT.format(self._address, command, value)
		else:
			url = BASE_COMMAND_URL_FORMAT.format(self._address, command)
		return requests.get(url).text