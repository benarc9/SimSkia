from engine.ecs.component import Component
from engine.ecs.events.button_event import ButtonEvent
from engine.ecs.events.key_event import KeyEvent
from engine.input.control_layout import ControlLayout

from pyeventbus3.pyeventbus3 import subscribe, PyBus

from loguru import logger

log = logger.info


class InputController(Component):
	def __init__(self):
		super(InputController, self).__init__()
		self.control_layout = None
		PyBus.Instance().register(self, self.__class__.__name__)

	@subscribe(onEvent=KeyEvent)
	def on_key_event(self, event: KeyEvent):
		if self.control_layout.is_mapped(event.key):
			PyBus.Instance().post(ButtonEvent(self.__class__.__name__, self.control_layout.button_map[event.key], event.action))

	@property
	def control_layout(self) -> ControlLayout:
		return self._control_layout

	@control_layout.setter
	def control_layout(self, value: ControlLayout):
		self._control_layout = value
