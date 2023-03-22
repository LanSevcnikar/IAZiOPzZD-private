# beatutiful soup program that parses the local html file
from bs4 import BeautifulSoup

html = ""

with open("VizHub - GBD Results.html") as fp:
    html = fp.read()

soup = BeautifulSoup(html, "html.parser")

# forward the print function into a file called output.txt
with open("output.txt", "w") as fp:

    # loop through all children of div with class "ant-select-tree-list-holder-inner"
    for child in soup.find("div", {"class": "ant-select-tree-list-holder-inner"}).children:
        # in the child, find span with class ant-select-tree-indent-unit and count the number of children
        if child.name is not None:
            indent_count = 0
            for indent in child.find_all("span", {"class": "ant-select-tree-indent-unit"}):
                indent_count += 1
            
            # find the child with text and print it
            for text in child.find_all("span", {"class": "ant-select-tree-title"}):
                texts = text.text.replace("\n", "").replace("\t", "")
                # from the text, remove any multiuple spaces and replace them with a singular one
                texts = " ".join(texts.split())
                print(" " * indent_count, indent_count, texts)

