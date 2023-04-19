from bs4 import BeautifulSoup

# Replace "example.html" with the path to your HTML file
with open("./chems.html") as file:
    soup = BeautifulSoup(file, "html.parser")

# Find the first <select> element
select_elem = soup.select_one("select")

# Extract the text from the child elements of the <select> element
text = ""
for child in select_elem.children:
    if child.name:
        text += child.text.strip() + ";" + child['value'].strip() + "\n"

# Save the text to a file with the same name as the HTML file but with a .txt extension
filename = "chems.txt"
with open(filename, "w") as file:
    file.write(text)

print(f"Text saved to {filename}")
