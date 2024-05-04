import unittest
from brainaic.llm import Llm


class TestLlm(unittest.TestCase):
    def test_llm(self):
        llm = Llm('phi3')
        response = llm.generate("Hello.")
        self.assertIsNotNone(response)


if __name__ == '__main__':
    unittest.main()
