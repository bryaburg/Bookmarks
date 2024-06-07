import re
# This checks the websites.txt and compares to my README.md file if there is matching websites and if so removes them from the list

URL_Regex = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"

with open('README.md', 'r') as md_file:
    md_content = md_file.read()

with open('websites.txt', 'r') as websites_file:
    website_list = [line.strip() for line in websites_file]

filtered_website_list = [url for url in website_list if not re.search(url, md_content, re.IGNORECASE)]

with open('websites.txt', 'w') as websites_file:
    for url in filtered_website_list:
        websites_file.write(url + '\n')
