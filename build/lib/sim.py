from engine import game, ecs, engine
import sys
from loguru import logger
import argparse

parser = argparse.ArgumentParser()
parser.parse_args()


class TestComponent(ecs.Component):
    def __init__(self):
        super(TestComponent, self).__init__()


class TestEntity(ecs.Entity):
    def __init__(self):
        super(TestEntity, self).__init__([TestComponent])


class TestSystem(ecs.System):
    def __init__(self):
        super(TestSystem, self).__init__([TestComponent])


class InitialScene(ecs.Scene):
    def __init__(self):
        super(InitialScene, self).__init__([TestSystem], [TestEntity])


class SimGame(game.Game):
    def __init__(self):
        self.engine = engine.Engine()
        self.ecs = ecs.ECS([InitialScene], True)
        super(SimGame, self).__init__(self.engine, self.ecs)


@logger.catch
def main():
    print("Argument Count: {}".format(len(sys.argv)))
    logger.opt(record=True).add(sink="out.log")
    logger.info("Starting game...")
    game = SimGame()
    game.start()
    game.run()


if __name__ == "__main__":
    main()
