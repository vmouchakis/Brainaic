import unittest
import tempfile
import shutil
import os
from brainaic.bot import Bot
from brainaic.prompt import DEFAULT_PROMPT
import warnings
warnings.filterwarnings("default", category=DeprecationWarning)


class TestBotInit(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.sample_file_path = os.path.join(self.temp_dir, 'sample.txt')
        with open(self.sample_file_path, 'w') as f:
            f.write('This is a sample text file for testing.')

        self.bot = Bot(data_path=self.temp_dir,
                       model_name='phi3',
                       temperature=0.0,
                       persist_vectors=False,
                       verbose=False)

    def test_initialization(self):
        # Test initialization of Bot instance
        self.assertEqual(self.bot.model_name, 'phi3')
        self.assertIsNotNone(self.bot.llm)
        self.assertEqual(self.bot.prompt, DEFAULT_PROMPT)
        self.assertIsNotNone(self.bot.embeddings)
        self.assertIsNotNone(self.bot.vectorstore)
        self.assertIsNotNone(self.bot.chain)

    def tearDown(self):
        self.bot = None  # Clear the Bot instance to release resources
        shutil.rmtree(self.temp_dir)


if __name__ == "__main__":
    unittest.main()
