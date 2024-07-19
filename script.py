import re

URL_Regex = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"

def extract_urls(text):
    """Extracts URLs from the given text based on the regex pattern."""
    return set(re.findall(URL_Regex, text, re.IGNORECASE))

with open('README.md', 'r') as md_file:
    md_content = md_file.read()

with open('websites.txt', 'r') as websites_file:
    website_list = [line.strip() for line in websites_file]

md_urls = extract_urls(md_content)
website_urls = set(website_list)

common_urls = md_urls.intersection(website_urls)

filtered_md_lines = [
    line for line in md_content.splitlines()
    if not any(url in line for url in common_urls)
]

filtered_website_list = [
    url for url in website_list
    if url not in common_urls
]

with open('README.md', 'w') as md_file:
    md_file.write('\n'.join(filtered_md_lines) + '\n')

with open('websites.txt', 'w') as websites_file:
    websites_file.write('\n'.join(filtered_website_list) + '\n')
