from loguru import logger

from tests.SimGame import SimGame

@logger.catch
def main():
    game = SimGame()
    game.run()

if __name__ == "__main__":
    main()
