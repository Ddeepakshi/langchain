# LangChain Experiments

Hands-on LangChain experiments — chat models and chatbot prototypes for LLM-powered applications.

## Structure

```
1.llm-intraction/    # Chat model usage with LangChain
   chatmodel.py

2.chatbot/           # Conversational chatbot
   chatbot.py

requirements.txt
```

## Quickstart

```bash
git clone https://github.com/Ddeepakshi/langchain.git
cd langchain
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

Set the LLM provider key your script expects (e.g. `OPENAI_API_KEY`, `GROQ_API_KEY`) in your environment, then run:

```bash
python 1.llm-intraction/chatmodel.py
python 2.chatbot/chatbot.py
```

## What's Inside

- **`1.llm-intraction/chatmodel.py`** — minimal LangChain `ChatModel` invocation with a system prompt and user turn.
- **`2.chatbot/chatbot.py`** — conversational chatbot with message history.

## Tech

- **Python**
- **LangChain**
- **LLM provider SDK** (configurable)

## Author

Built by [Deepakshi Sharma](https://www.linkedin.com/in/deepakshi-sharma-865068270/).
