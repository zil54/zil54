import logging
import fileinput
import re

class CommandLineLogger:

	def __init__(self, outputDir):
		self.outputDir = outputDir

	def log_success(self, command, output, filename):
		logging.basicConfig(filename=self.outputDir + filename, level=logging.DEBUG)
		logging.info("Log output: " + command + "\n" + output)

	def log_failure(self, command, output, filename):
		logging.basicConfig(filename=self.outputDir + filename)
		logging.error("Log output: " + command + "\n" + output)

	def log_warning(self, command, output, filename):
		logging.basicConfig(filename=self.outputDir + filename)
		logging.warning("Log output: " + command + "\n" + output)

	def log_analyze(self, filename, startAt, *success_keywords):
		elem_found = ""
		returnLineNo = 0
		returnStatus = 1
		for line in fileinput.input(self.outputDir + filename):
			if fileinput.lineno() > startAt:
				for elem_to_find in success_keywords:
					if re.search(elem_to_find, line.strip()):
						returnLineNo = fileinput.lineno()
						elem_found = elem_to_find
						returnStatus = 0
						fileinput.close()

						break;
					else:
						returnLineNo = fileinput.lineno()
		if elem_found == "":
			elem_found = "nothing found from the list of success keywords such as : " + str(success_keywords)

		return returnStatus, returnLineNo, elem_found

