import unittest
from brainaic.bot import Bot
import warnings
warnings.filterwarnings("default", category=DeprecationWarning)


class TestBotInit(unittest.TestCase):
    def test_bot_init(self):
        bot = Bot("./data")
        self.assertIsNotNone(bot.model.model_name)
        self.assertIsNotNone(bot.loader.load())


if __name__ == "__main__":
    unittest.main()