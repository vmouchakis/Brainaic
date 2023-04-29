from brainaic.bot import Bot
from brainaic.utils import parse_args


def main():
    args = parse_args()

    bot = Bot(data_path=args.data_path, model_name=args.model_type)
    ans = bot.get_response(args.prompt)
    print(ans)
    print(bot.get_response("Name 3 fottball teams from the place Vasilis lives."))


if __name__ == "__main__":
    main()
