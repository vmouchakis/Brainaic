from brainaic.bot import Bot


data_path = "./data"
model_name = "gpt"


def main():
    bot = Bot(data_path=data_path, model_name=model_name)
    user_input = input()
    while user_input != "quit":
        ans = bot.get_response(user_input)
        print(ans)
        user_input = input()


if __name__ == "__main__":
    main()
