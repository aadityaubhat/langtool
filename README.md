# 🛠️ LangTool

LangTool is a Python library designed to enable seamless interactions between Large Language Models (LLMs) and Python functions and classes. The primary objective of LangTool is to facilitate the creation of user-friendly LLM tools for Python functions and classes. To achieve this, LangTool introduces Toolify, a class that adds a semantic layer on top of functions or classes.

LangTool borrows the concept of a Tool from LangChain (https://github.com/hwchase17/langchain). One of the goals of this project is to complement LangChain by providing a high-level interface for users to create tools on the fly.

## 📝 Example Usage

``` python
from langtool import Openai, Toolify, Model

def get_headlines(topic, date, language='EN', n=100):
    """
    Function to fetch headlines based on a given topic, date, and language.
    
    Args:
    topic (str): The topic for which headlines should be fetched.
    date (str): The date (YYYY-MM-DD) on which the headlines were published.
    language (str, optional): The language in which the headlines should be returned. Defaults to 'EN' (English).
    n (int, optional): The number of headlines to fetch. Defaults to 100.

    Returns:
    list: A list of headlines (strings) based on the specified topic, date, and language.
    """
    return ['']

llm = Openai('<OpenAI_API_KEY>', Model.GPT_4)
headlines_tool = Toolify(get_headlines, llm)

print(headlines_tool.run('Get headlines about Twitter as of yesterday'))
# Output 
# get_headlines('Twitter', '2023-04-18') 
```

## 📦 Installation

```python
pip install langtool
```

## 📍 Roadmap

- [ ] Support creating LangChain tools
- [ ] Support Python modules as tools
- [ ] Support external APIs as tools
- [ ] Support Toolkits consisting of multiple tools
- [ ] Support other LLMs

## ✨ Contributing

Get started by checking out the Github issues and using LangTool to familiarize yourself with the project. LangTool is still actively under development, and any support is gladly welcomed.
Feel free to open an issue or reach out if you would like to contribute to the project!
