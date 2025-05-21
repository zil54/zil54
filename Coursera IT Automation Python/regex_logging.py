import logging
import fileinput
import re

import logging

class RegexLogger:
    """Handles logging for regex operations."""

    def __init__(self, output_dir):
        self.output_dir = output_dir
        logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

    def log_successful_regex_implementation(self, regex_action, output, filename):
        """Logs successful regex operations."""
        self._log_to_file(filename, f"SUCCESS: {regex_action}\n{output}", logging.INFO)

    def log_warning_regex_implementation(self, regex_action, output, filename):
        """Logs warnings for operations that completed but didn't match criteria."""
        self._log_to_file(filename, f"WARNING: {regex_action}\n{output}", logging.WARNING)

    def log_error_regex_implementation(self, regex_action, output, filename):
        """Logs errors for incorrectly structured regex patterns."""
        self._log_to_file(filename, f"ERROR: {regex_action}\n{output}", logging.ERROR)

    def _log_to_file(self, filename, message, log_level):
        """Handles logging while ensuring file-level separation."""
        file_path = f"{self.output_dir}/{filename}"
        logger = logging.getLogger(file_path)
        handler = logging.FileHandler(file_path)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(log_level)

        logger.log(log_level, message)
        logger.removeHandler(handler)  # Prevent duplicate handlers



