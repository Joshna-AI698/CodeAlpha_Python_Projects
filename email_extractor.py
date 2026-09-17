import re

input_file = "sample_text.txt"
output_file = "extracted_emails.txt"

with open(input_file, "r") as file:
    text = file.read()
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

emails = re.findall(email_pattern, text)

with open(output_file, "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Email addresses extracted successfully!")
print("Extracted emails are:")

for email in emails:
    print(email)
