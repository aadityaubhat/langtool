from langtool.llms.base import LLM
from langtool import Toolify
from io import StringIO
import sys


class HeadlinesLLM(LLM):
    def __init__(self):
        pass

    def get_reply(self, message, **kwargs):
        return "get_headlines('Twitter', '2021-01-01', language='EN', n=100)"


def get_headlines(topic, date, language="EN", n=100):
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
    print(f"Top {n} headlines for {topic} on {date} in {language}")


def test_headlines_tool():
    headlines_tool = Toolify(get_headlines, HeadlinesLLM())

    result = StringIO()
    sys.stdout = result
    headlines_tool.run("Twitter", safe_mode=False)
    output = result.getvalue()

    assert output == "Top 100 headlines for Twitter on 2021-01-01 in EN\n"
