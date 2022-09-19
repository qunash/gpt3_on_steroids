Given a question, your task is to write a valid Python3 program that prints the correct answer.

There are two special Python functions you now have access to:
- `read_webpage(url: str) -> str`, which returns all readable text present on the webpage at url.
- `ask_gpt3(prompt: str) -> str`, which returns GPT-3's response to the given prompt.

Begin.

QUESTION: What is the least common denominator of 123 and 12345?
```python
from math import gcd
print(gcd(123, 12345))
```

QUESTION: What is the date today?
```python
import datetime
print(datetime.date.today())
```

QUESTION: How much does the house at 1300 N Genesee Ave, Los Angeles, CA 90046 cost?
```python
# First, let's search Google to find some informative urls
search_result_urls = list(googlesearch.search("1300 N Genesee Ave, Los Angeles, CA 90046"))

# Ask GPT-3 which url is best.
prompt = f"Which of the following urls would most likely contain the price of the house at 1300 N Genesee Ave, Los Angeles, CA 90046? Return exactly one url.\n\n{search_result_urls}"
url = ask_gpt3(prompt)

print('selected url: ' + url)

# Now read the page and ask GPT-3 the question.
parsed_text = read_webpage(get_url_text(url))
prompt = f"Read the following text parsed from url {url}, and then answer the question below as helpfully as you can.\n\n{parsed_text}\n\nQuestion: How much does the house at 1300 N Genesee Ave, Los Angeles, CA 90046 cost? If you are not certain, precede your answer with 'I'm not certain, but...' Include the url you consulted in your answer."
print(ask_gpt3(prompt))
```

QUESTION: