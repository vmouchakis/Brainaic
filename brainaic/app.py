from brainaic.bot import Bot


def main():
    data_path = "./data"
    bot = Bot(data_path=data_path)
    ans = bot.get_response("How old is Vasilis?")
    print(ans)


if __name__ == "__main__":
    main()
