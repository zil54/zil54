
'''
re.compile(pattern, flags=0): Compiles a regular expression pattern into a regex object.
re.search(pattern, string, flags=0): Searches for the first occurrence of the pattern in the given string.
re.match(pattern, string, flags=0): Checks if the pattern matches at the beginning of the string.
re.findall(pattern, string, flags=0): Returns all occurrences of the pattern in the string.
re.sub(pattern, replacement, string, count=0, flags=0): Replaces occurrences of the pattern with the specified replacement.
re.split(pattern, string, maxsplit=0, flags=0): Splits the string by occurrences of the pattern.
'''
# Example product number pattern: two letters followed by four digits
import re

class RegexDemo:
    def __init__(self, text):
        self.text = text

    def search_example(self, pattern):
        result = re.search(pattern, self.text)
        return result.group() if result else None

    def match_example(self, pattern):
        result = re.match(pattern, self.text)
        return result.group() if result else None

    def findall_example(self, pattern):
        return re.findall(pattern, self.text)

    def sub_example(self, pattern, replacement):
        return re.sub(pattern, replacement, self.text)

    def split_example(self, pattern):
        return re.split(pattern, self.text)

# Example usage:
sample_text = "Hello, world! This is a sample text for regex demo."
demo = RegexDemo(sample_text)

# Search for "world"
#raw string (no special characters)
print(demo.search_example(r"world"))

# Match "Hello"
print(demo.match_example(r"Hello"))

# Find all words
print(demo.findall_example(r"\w+"))

# Replace "sample" with "awesome"
print(demo.sub_example(r"sample", "awesome"))

# Split by spaces
print(demo.split_example(r"\s+"))


email_text = "Contact us at support@example.com or info@company.org"
email_demo = RegexDemo(email_text)
emails = email_demo.findall_example(r"\b[\w\.-]+@[\w\.-]+\.\w+\b")
print(emails)

date_text = "Meeting scheduled for 06/15/2024 and 12/31/2024"
date_demo = RegexDemo(date_text)
dates = date_demo.findall_example(r"\b\d{2}/\d{2}/\d{4}\b")
print(dates)

social_text = "Check out #Python and #MachineLearning on Twitter!"
social_demo = RegexDemo(social_text)
hashtags = social_demo.findall_example(r"#\w+")
print(hashtags)

phone_text = "Call us at 123-456-7890 or 987-654-3210"
phone_demo = RegexDemo(phone_text)
masked_numbers = phone_demo.sub_example(r"\d{3}-\d{3}-\d{4}", "[REDACTED]")
print(masked_numbers)

sentence = "Hello! How are you? I'm fine."
split_demo = RegexDemo(sentence)
result = split_demo.split_example(r"[.!?]+")
print(result)

phrase = "The great escape artist"
split_demo = RegexDemo(phrase)
result = split_demo.split_example(r"\b\w*[a]\w*\b")
filtered_result = [word for word in result if word.strip()]
print(filtered_result)




print ('--------------------------------------------------')













product_number_pattern = r'[A-Za-z]{2}\d{4}'

# Sample document text
document_text = "The product numbers are AB1234, XY5678, and ZZ9012."

# Find all matches in the document text
product_numbers = re.findall(product_number_pattern, document_text)

print(product_numbers)

def check_aei(text):
    result = re.search(r"a.e.i", text)
    return result != None

print(check_aei("academia")) # True
print(check_aei("aerial"))   # False
print(check_aei("paramedic")) # True

