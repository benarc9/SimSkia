import glfw
from engine.lib.math import Vector


class Window:
    def __init__(self, size: Vector = Vector(800, 640)):
        if not glfw.init():
            raise RuntimeError('glfw.init() failed')
        glfw.window_hint(glfw.STENCIL_BITS, 8)
        self.size = size
        self.glfw_window = glfw.create_window(self.size.x, self.size.y, '', None, None)
        glfw.make_context_current(self.glfw_window)

    @property
    def size(self) -> Vector:
        return self._size

    @size.setter
    def size(self, value: Vector):
        self._size = value

    @property
    def glfw_window(self) -> glfw._GLFWwindow:
        return self._glfw_window

    @glfw_window.setter
    def glfw_window(self, value: glfw._GLFWwindow):
        self._glfw_window = value
