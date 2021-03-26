import skia
from OpenGL import GL
from .window import Window


class SkiaSurface:
    def __init__(self, window: Window):
        self.window = window

        self.context = skia.GrDirectContext.MakeGL()

        self.render_target = skia.GrBackendRenderTarget(
            self.window.size.x, self.window.size.y,
            0, 0,
            skia.GrGLFramebufferInfo(0, GL.GL_RGBA8))

        self.surface = skia.Surface.MakeFromBackendRenderTarget(
            self.context, self.render_target, skia.kBottomLeft_GrSurfaceOrigin,
            skia.kRGBA_8888_ColorType, skia.ColorSpace.MakeSRGB())

        self.canvas = self.surface.getCanvas()

    def flush(self):
        self.surface.flushAndSubmit()

    @property
    def canvas(self) -> skia.Canvas:
        return self._canvas

    @canvas.setter
    def canvas(self, value: skia.Canvas):
        self._canvas = value

    @property
    def context(self) -> skia.GrDirectContext:
        return self._context

    @context.setter
    def context(self, value: skia.GrDirectContext):
        self._context = value

    @property
    def render_target(self) -> skia.GrBackendRenderTarget:
        return self._render_target

    @render_target.setter
    def render_target(self, value: skia.GrBackendRenderTarget):
        self._render_target = value

    @property
    def surface(self) -> skia.Surface:
        return self._surface

    @surface.setter
    def surface(self, value: skia.Surface):
        self._surface = value

    @property
    def window(self) -> Window:
        return self._window

    @window.setter
    def window(self, value: Window):
        self._window = value
