from typing import Callable
from OpenGL import GL
from abc import ABC
from .window import Window
from .draw import SkiaSurface

import glfw, skia


class EngineInterface(ABC):
    def __init__(self):
        glfw.init()
        self.running = False

    def stop(self) -> None:
        pass

    def start(self) -> None:
        pass

    def update(self) -> bool:
        pass


class Engine(EngineInterface):
    def __init__(self):
        super(Engine, self).__init__()
        self.window = Window()
        self.surface = SkiaSurface(self.window)

    def start(self):
        self.running = True

    def update(self) -> bool:
        self.running = True
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        self.surface.flush()
        glfw.swap_buffers(self.window.window)
        glfw.poll_events()

        if glfw.get_key(self.window.window, glfw.KEY_ESCAPE):
            self.running = False
        elif glfw.window_should_close(self.window.window):
            self.running = False

        return self.running

    @property
    def window(self) -> Window:
        return self._window

    @window.setter
    def window(self, value: Window):
        self._window = value

    @property
    def surface(self) -> skia.Surface:
        return self._surface

    @surface.setter
    def surface(self, value: skia.Surface):
        self._surface = value


