from bs4 import BeautifulSoup
import csv
import re

# Read HTML from a file
with open("resorts.html", "r", encoding="utf-8") as f:
    html = f.read()

# Parse HTML
soup = BeautifulSoup(html, "html.parser")

# Extract options (skip the first one "Choose Your Resort")
options = soup.find_all("option")[1:]

# Prepare CSV data
rows = []
for opt in options:
    full_text = opt["value"].strip()
    
    # Extract resort name and price using regex
    match = re.match(r"^(.*?)-\s*\$(\d+)$", full_text)
    if match:
        resort_name = match.group(1).strip()
        price = match.group(2).strip()
        rows.append([full_text, resort_name, price])

# Write to CSV
with open("resorts.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Resort Name with Price", "Resort Name", "Price"])
    writer.writerows(rows)

print("CSV file created: resorts.csv")