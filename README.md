# PythonPrograms

This repository contains various experiments and sample programs.

## Browser Game

A simple Snake game is included under `HTML/snake`. Open `index.html` in a web browser to play.

## DeepSeek Terminal Chat

`deepseek_terminal.py` provides a small terminal chat client for the free
[DeepSeek LLM](https://huggingface.co/deepseek-ai/deepseek-llm-7b-instruct)
hosted on Hugging Face. To use it you need a Hugging Face API token stored in
the environment variable `HUGGINGFACE_TOKEN`.

Install the required dependency and run:

```bash
pip install requests
python deepseek_terminal.py
```

Enter your prompts in the terminal and type `exit` to quit.
