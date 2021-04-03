class KeyEvent:
	def __init__(self, key):
		self.key = key

	@property
	def key(self):
		return self._key

	@key.setter
	def key(self, value):
		self._key = value
