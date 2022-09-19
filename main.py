import os
import colorama as cr
import bs4
import io
import googlesearch
import openai
import requests
import sys
import traceback
import re

cr.init(autoreset=True)


def google_search(query: str, num_results: int = 10) -> list:
    return list(googlesearch.search(query, num_results))


def get_url_text(url: str) -> str:
    return requests.get(url).text


def read_webpage(url: str) -> str:
    """Returns all readable text present on the webpage at url."""
    page_text = requests.get(url).text
    soup = bs4.BeautifulSoup(page_text, "html.parser")
    text = soup.get_text()
    text = text[:(2500 * 4)]  # Limit text due to OpenAI limits
    return text


def get_all_classes(url):
    classes = []
    source = requests.get(url).text
    # return source
    soup = bs4.BeautifulSoup(source, 'lxml')
    for node in soup.findAll('div'):
        class_ = node.get('class', [])
        if class_:
            classes.extend(class_)
    return list(set(classes))


def ask_gpt3(prompt: str, stop: str = None, max_tokens: int = 256):
    """Returns GPT-3's response to the given prompt."""
    response = openai.Completion.create(model="text-davinci-002",
                                        prompt=prompt,
                                        temperature=0,
                                        max_tokens=max_tokens,
                                        stop=stop)
    print('tokens used: ' + str(response.usage.total_tokens))
  #   print("""
  # ask_gpt3:
  #   tokens used: """ + str(response.usage.total_tokens) + """
  #   response:
  # """ + str(response))

    return response.choices[0].text.strip()


def execute_code(code: str) -> str:
    sys_stdout = sys.stdout
    sys.stdout = output = io.StringIO()
    try:
        exec(code)
    except Exception as e:
        print("ERROR: Code failed to execute:")
        print(e)
        print(e.args)
        # traceback.print_tb(e.__traceback__)
        # print(traceback.format_exc())
        print(e.__traceback__.tb_frame.f_locals)
    sys.stdout = sys_stdout
    return output.getvalue()


def print_generated_code(code: str) -> None:
    indented_code = '\n'.join([f'\t{line}' for line in code.splitlines()])
    print(cr.Fore.YELLOW + f"\n[DEBUG] Generated Code:\n{indented_code}\n")


if __name__ == "__main__":
    openai.api_key = os.environ['OPENAI_API_KEY']
    with open('prompt.md') as f:
        PROMPT = f.read()
    while (task := input('QUESTION: ').strip()) != "":
        prompt = f'{PROMPT} {task}\n```python'
        code = ask_gpt3(prompt, stop='```', max_tokens=512)
        print_generated_code(code)
        result = execute_code(code)
        print(openai)
        print(cr.Fore.GREEN + f"\nANSWER: {result}")
