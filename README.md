# BrainAIc
<p align="center">
    <img src="./images/logo.png" alt="BrainAIc" width="50%">

</p>
<p align="center">
    <small>Image generated with DALL-E.<br></small>
    <em>BrainAIc is an easy to use chatbot. In only a couple of lines of code, you can get answers based on your personal documents.</em>
</p>


You want to use OpenAi's pretrained models to query your files? Look no further.
BrainAIc is an easy to use chatbot. In only a couple of lines of code, you can get answers based on your personal documents.

### Models supported:
- `gpt-3.5-turbo`
- `llama2 7b chat`

## Set up for `gpt` model
- Save your OpenAI API Key locally:
#### write in your terminal:
```sh
export OPENAI_API_KEY="..."
```
#### or inside your python script:
```python
import os
os.environ["OPENAI_API_KEY"] = "..."
```

## Set up for `llama2` model
- Make sure you are following [this video](https://www.youtube.com/watch?v=TsVZJbnnaSs) from [Alex Ziskind](https://github.com/alexziskind1) to install all necessary model files.
- Or follow [this](https://medium.com/@auslei/llama-2-for-mac-m1-ed67bbd9a0c2) article.

*Remember to move the models under the `model` directory in this project, see the `config.py` file.*

## Set up environment
- Install dependencies inside your `virtual environment`:
```sh
pip install -r requirements.txt
CMAKE_ARGS="-DLLAMA_METAL=on" FORCE_CMAKE=1 pip install llama-cpp-python
```

Now you are ready to use the Bot.

Example:
```sh
python -m brainaic.app --data_path './data' --model_type 'llama' --prompt 'How old is Vasilis?'
```

## Run tests:
```sh
python -m pytest tests -W ignore::DeprecationWarning
```

## TODO:
- [ ] Add support for other models
    https://github.com/ChristopherKing42/llama/tree/patch-1 - LLAMA 7B ADDED
- [ ] Add more tasks. Right now only querying over files is supported. Chat-based funcionality using Llama will be added
- [ ] Llama model is very slow. Make it faster
- [x] Add memory - FIX
- [x] Add prompts - FIX


## Problems
- [ ] Llama model is useless when max_tokens are exceeded.
- [ ] Llama model produces nonsense and answers to questions I did not ask, maybe create an issue in langchain repo.


#### Usefull links
https://github.com/hwchase17/langchain/issues/2784
