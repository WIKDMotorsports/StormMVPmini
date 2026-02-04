from bs4 import BeautifulSoup

with open('K9.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

specs_grid = soup.find(class_='specs-grid')
details = specs_grid.find_all('details')

# Check first item
first_detail = details[0]
summary_text = first_detail.find('summary').text.strip()

print(f"First detail summary: '{summary_text}'")
print(f"First detail has 'open' attribute: {first_detail.has_attr('open')}")

# Check if "Operational Leadership" exists anywhere
op_leadership = soup.find(string="Operational Leadership")
print(f"'Operational Leadership' found: {op_leadership is not None}")

if summary_text == "Detection Configurations" and first_detail.has_attr('open') and op_leadership is None:
    print("VERIFICATION PASSED")
else:
    print("VERIFICATION FAILED")
