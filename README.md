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

*Created on Macbook M1 Pro*

### Models supported:
- `gpt-3.5-turbo`
- `llama2 7b`

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

*Here we are using the 7b model, but following the instructions above you can use any Llama model*
*Remember to move the models under the `models` directory in this project, see the `config.py` file.*

## Set up environment
- Install dependencies inside your `virtual environment`:
```sh
pip install -r requirements.txt
CMAKE_ARGS="-DLLAMA_METAL=on" FORCE_CMAKE=1 pip install llama-cpp-python
```

Now you are ready to use the Bot.

Example:
```sh
python -m brainaic.app --data_path './data/samples' --model_type 'llama' --prompt 'How old is Vasilis?'
```
Instead of `samples` you could choose your desired subfolder (each subfolder contains related data).


## Run the app as a web app:
```sh
python -m streamlit run brainaic/web_app.py
```


## Run tests:
```sh
python -m pytest tests -W ignore::DeprecationWarning
```

## TODO:
- [ ] Add support for other models
    https://github.com/ChristopherKing42/llama/tree/patch-1 - LLAMA 7B ADDED
- [ ] Add more tasks. Right now only querying over files is supported. Chat-based funcionality using Llama will be added
- [ ] Add memory
- [x] Llama model is very slow. Make it faster. - Fixed, can be better though.


## Problems
- [ ] **MAJOR PROBLEM: need to test it in more capable hardware**
- [ ] Make prompts better

#### Usefull links
https://github.com/hwchase17/langchain/issues/2784
