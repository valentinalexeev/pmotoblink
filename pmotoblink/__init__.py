import importlib
import logging
import requests
from pmotoblink.util import DEVICE_MP853CONNECT, cmds
from pmotoblink.device.generic import COMMANDS as GENERIC_COMMANDS


BASE_COMMAND_URL_FORMAT = "http://{}/?action=command&command={}"
BASE_COMMAND_VALUE_URL_FORMAT = BASE_COMMAND_URL_FORMAT + "&value={}"

class MotoBlinkRaw():
	def __init__(self, address):
		self._address = address

	def send_command(self, command, value = None):
		url = None
		if value:
			url = BASE_COMMAND_VALUE_URL_FORMAT.format(self._address, command, value)
		else:
			url = BASE_COMMAND_URL_FORMAT.format(self._address, command)
		logging.debug('Requesting URL {}'.format(url))
		response = requests.get(url)
		logging.debug('Response code = {} and text = {}'.format(response.status_code, response.text))
		if response.status_code == 200:
			return {'ok': True, 'text': response.text}
		else:
			return {'ok': False, 'text': response.status_code}


class MotoBlink():
	def __init__(self, address, device_type = DEVICE_MP853CONNECT):
		self._rawSender = MotoBlinkRaw(address)

		mod = importlib.import_module("pmotoblink.device." + device_type)
		self._specific = getattr(mod, "COMMANDS")

	def __send_command(self, command, result_parser, value = None):
		response = self._rawSender.send_command(command, value)

		if response['ok']:
			response_value = result_parser(response['text'])
			return response_value
		else:
			raise ValueError("Invalid response received {}".format(response.code))

	def __select_command(self, command):
		specific = self._specific[command]
		generic = GENERIC_COMMANDS[command]

		if specific and specific.get('is_supported', True):
			logging.debug("Using device-specific command for {}".format(command))
			return specific
		elif generic and generic.get('is_supported', True):
			logging.debug("Using generic command for {}".format(command))
			return generic
		else:
			raise ValueError("Unknown command '{}'".format(command))

	def __run_command(self, command, value = None):
		cmd = self.__select_command(command)

		return self.__send_command(cmd['cmd'], cmd['parser'], value)

	def get_temperature(self):
		return self.__run_command(cmds.TEMPERATURE)

	def get_mini_device_info(self):
		return self.__run_command(cmds.MINI_DEVICE_INFO)