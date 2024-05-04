import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data_path",
                        required=True,
                        type=str,
                        help="data path")
    parser.add_argument("-m", "--model_type",
                        required=True,
                        type=str,
                        help="gpt/llama/llama2/llama2-chat")
    parser.add_argument("-p", "--prompt",
                        required=True,
                        type=str,
                        help="prompt")

    return parser.parse_args()
