# BrainAIc
<p align="center">
    <img src="./images/logo.png" alt="BrainAIc" width="70%">

</p>
<p align="center">
    <em>BrainAIc is an easy to use chatbot. In only a couple of lines of code, you can get answers based on your documents.
</em>
</p>


You want to use OpenAi's pretrained models to query your files? Look no further.
BrainAIc is an easy to use chatbot. In only a couple of lines of code, you can get answers based on your documents.


## Steps to use the bot
- Save your OpenAI API Key locally:
#### write in your terminal:
```sh
export OPENAI_API_KEY="..."
```
#### or inside your python script:
```sh
import os
os.environ["OPENAI_API_KEY"] = "..."
```
- Install dependencies inside your `virtual environment`:
```sh
pip install -r requirements.txt
```

Now you are ready to use the Bot.

Example:
```sh
from brainaic.bot import Bot

# set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "..."

data_path = "./data"
# create the bot
bot = Bot(data_path=data_path)

# get the response to your question
ans = bot.get_response("How old is Vasilis?")

print(ans)
# Vasilis is 25 years old.
```

## Run tests:
```sh
python -m pytest tests -W ignore::DeprecationWarning
```
