import logging
import fileinput
import re

class APICallsLogger:

	def __init__(self, outputDir):
		self.outputDir = outputDir

	def log_success(self, api_command, status_code, output, filename):
		logging.basicConfig(filename=self.outputDir + filename, level=logging.DEBUG)
		if '200' in status_code:
			logging.info("Log output: " + api_command + "\n" + output)


