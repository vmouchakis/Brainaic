# BrainAIc
<p align="center">
    <img src="./images/logo.png" alt="BrainAIc" width="50%">

</p>
<p align="center">
    <small>Image generated with DALL-E.<br></small>
    <em>BrainAIc is an easy to use bot. In only a couple of lines of code, you can get answers based on your personal documents.</em>
</p>


If you're looking to use Ollama's pretrained models to query your files, you're in luck.
BrainAIc is a straightforward tool. With just a few lines of code, you can retrieve answers based on your personal documents.
*Created on Macbook M1 Pro*

## Set up Ollama

### Install Ollama
Follow [these instructions](https://ollama.com/download/)

### Download Ollama models
```sh
ollama pull llama2:7b
```

### Serve ollama
```sh
ollama serve
```

## Set up environment
- Install dependencies inside your `virtual environment`:
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Now you are ready to use the Bot.

Make sure Ollama is running.

Example:
```sh
python -m brainaic.app --data_path './data' --model_type 'phi3' --prompt 'How old is Vasilis?'
```
Instead of `samples` you could choose your desired subfolder (each subfolder contains related data).


## Run the app as a web app:
```sh
python -m streamlit run brainaic/web_app.py
```

## Run tests:
```sh
python -m pytest tests
```
