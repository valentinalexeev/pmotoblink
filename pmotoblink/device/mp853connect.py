from pmotoblink.util import cmds, result_parser

COMMANDS = {
	cmds.TEMPERATURE: {'cmd': 'value_temperature', 'parser': result_parser.value_only}
}