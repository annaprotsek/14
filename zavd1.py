import requests
import re

url = "https://www.gutenberg.org/ebooks/16.txt.utf-8"

response = requests.get(url)

if response.status_code == 200:
    raw_text = response.text

    cleaned_text = re.sub(r"\*\*\*.*?\*\*\*", "", raw_text, flags=re.DOTALL)
    cleaned_text = re.sub(r"\n\s*\n", "\n\n", cleaned_text.strip())  

    excerpt = cleaned_text[:1000]

    with open("text.txt", "w", encoding="utf-8") as file:
        file.write(excerpt)
    
    print("The first 1000 characters of the text have been successfully saved to 'text.txt'.")
else:
    print("Failed to retrieve the text. Please check the URL.")
