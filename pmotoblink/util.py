#
# Common utils for the package.
#
import re

PARSER_NAME_VALUE = re.compile("(.*): (.*)")

DEVICE_GENERIC = 'generic'
DEVICE_MP853CONNECT = 'mp853connect'

class result_parser():
	""" Template result parsers that can be used by devices. """
	@staticmethod
	def name_value(input):
		match = PARSER_NAME_VALUE.findall(input).pop()

		return { match[0]: match[1] }

	@staticmethod
	def value_only(input):
		match = PARSER_NAME_VALUE.findall(input).pop()

		return match[1]

class cmds():
	TEMPERATURE = 'temperature'
	MINI_DEVICE_INFO = 'mini_device_info'