from enum import Enum

import loguru


class LogLevel(Enum):
	INFO = 'INFO',
	DEBUG = 'DEBUG',
	WARNING = 'WARNING',
	ERROR = 'ERROR'


class Logger:

	def __init__(self, level: str):
		self.level = level
		self.logger: loguru.Logger = loguru.logger
		self.info = self.logger.info
		self.debug = self.logger.debug
		self.error = self.logger.error

	@property
	def log_level(self) -> LogLevel:
		return self._level

	@log_level.setter
	def log_level(self, value: LogLevel):
		self._level = value

	@property
	def logger(self) -> loguru.logger:
		return self._logger

	@logger.setter
	def logger(self, value: loguru.logger):
		self._logger = value
