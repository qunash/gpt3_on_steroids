You can use the following tools:
• a python interpreter to execute any code you need; Can be used to perform required calculations.
• `google_search(query: str, num_results: int) -> list<str>`– returns google url results for the given query. Default num_results = 10, adjust as you see fit, but don't go beyond 10.
• `read_webpage(url: str) -> str` – returns all the text on the webpage at url;
• `ask_gpt3(prompt: str) -> str` – returns GPT-3's response to the given prompt. Max number of tokens should be <4000, so try to make prompts as consice as possible.

Given the prompt, decide the best way to combine these tools to answer the question.
You can make as many google searches as you need.
For factual data like laws, dates, current events, current date, sizes etc. always consult google search (e.g. "the height of pyramid of Giza", "earth equatorial length" etc.).

QUESTION: Is today hotter in Paris than a year ago?

What steps do we need to take to answer this question?
Let's think step by step:

1. Find out the temperature in Paris today.
2. Find out the date a year ago.
3. Find out the temperature in Paris a year ago.
4. Compare the two temperatures.

Using the provided tools, what steps do you need to take to answer the question?

```python
# 1. Find out the temperature in Paris today.
# Factual data, use google search.
url = google_search("temperature in Paris today", 1)[0]
print('url: ' + url)
# get page content
page_text = read_webpage(url)
# construct a prompt for GPT-3 with the page content to get the temperature in python float format
prompt = f"{page_text}\n\nTemperature in Paris today in python float format (e.g. 7.3):"
# get temperature from GPT-3
temp_today = ask_gpt3(prompt)
temp_today = float(re.sub(r'[^\d.]', '', temp_today))
print(f"Temperature in Paris today: {temp_today}")

# 2. Find out the date a year ago. Factual data, use python.
import datetime
today = datetime.date.today()
year_ago = today - datetime.timedelta(days=365)

# 3. Find out the temperature in Paris a year ago.
# Factual data, use google search.
url = google_search(f"temperature in Paris on {year_ago}", 1)[0]
print('url: ' + url)
# get page content
page_text = read_webpage(url)
# construct a prompt for GPT-3 with the page content to get the temperature in python float format
prompt = f"{page_text}\n\nTemperature in Paris on {year_ago} in python float format (e.g. 5.0):"
# get temperature from GPT-3
temp_year_ago = ask_gpt3(prompt)
temp_year_ago = float(re.sub(r'[^\d.]', '', temp_year_ago))
print(f"Temperature in Paris on {year_ago}: {temp_year_ago}")

# 4. Compare the two temperatures.
# Use python to compare the two temperatures.
if float(temp_today) > float(temp_year_ago):
    print("Today is hotter than a year ago.")
elif temp_today < temp_year_ago:
    print("Today is cooler than a year ago.")
else:
    print("Today is the same temperature as a year ago.")
```

QUESTION: Where were the last olympic games held?

What steps do we need to take to answer this question?
Let's think step by step:

1. Find out the location of the last olympic games.

Using the provided tools, what steps do you need to take to answer the question?

```python
# 1. Find out the location of the last olympic games.
# Factual data, use google search.
url = google_search("location of the last olympic games", 1)[0]
print('url: ' + url)
# get page content
page_text = read_webpage(url)
# construct a prompt for GPT-3 with the page content to get the location
prompt = f"{page_text}\n\nWhere were the last olympic games held? If you're not sure, or there's no answer to the question, say so."
# get the answer from GPT-3
answer = ask_gpt3(prompt)
print(answer)
```

QUESTION: What's the square root of pi?
What steps do we need to take to answer this question?
Let's think step by step:

1.  Find out the square root of pi.

Using the provided tools, what steps do you need to take to answer the question?

```python
1. Find out the square root of pi.
# Factual data, use pythons interpreter.
import math
print(math.sqrt(math.pi))
```

QUESTION: