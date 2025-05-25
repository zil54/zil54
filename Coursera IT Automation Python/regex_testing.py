

#regex101.com

"""Study guide: Advanced regular expressions
Advanced regular expressions—commonly referred to as advanced regexes—are used by developers to execute complicated pattern matching against strings.
In this reading, you will learn about some of the common examples of advanced regular expressions.

Alterations
An alteration matches any one of the alternatives separated by the pipe | symbol. Let’s look at an example:
r"location.*(London|Berlin|Madrid)"

This line of code will match the text string location is London, location is Berlin, or location is Madrid.
Matching only at the beginning or end

If you use the circumflex symbol (also known as a caret symbol) ^ as the first character of your regex,
it will match only if the pattern occurs at the start of the string.
Alternatively, if you use the dollar sign symbol $ at the end of a regex, it will match only if the pattern occurs at the end. Let’s look at an example:
r”^My name is (\w+)”

This line of code will match My name is Asha but not Hello. My name is Asha.
Character ranges

Character ranges can be used to match a single character against a set of possibilities.
Let’s look at a couple of examples:

r”[A-Z] This will match a single uppercase letter.
r”[0-9$-,.] This will match any of the digits zero through nine, or the dollar sign, hyphen, comma, or period.

The two examples above are often combined with the repetition qualifiers.
Let’s look at one more example:

r”([0-9]{3}-[0-9]{3}-[0-9]{4})”

This line of code will match a U.S. phone number such as 888-123-7612.
Backreferences

A backreference is used when using re.sub() to substitute the value of a capture group into the output. Let’s look at an example:
re.sub(r”([A-Z])\.\s+(\w+)”, r”Ms. \2”, “A. Weber and B. Bellmas have joined the team.”)
This line of code will produce Ms. Weber and Ms. Bellmas have joined the team.

Lookahead
A lookahead matches a pattern only if it’s followed by another pattern. Let’s look at an example:
If the regex was r”(Test\d)-(?=Passed)” and the string was “Test1-Passed, Test2-Passed, Test3-Failed, Test4-Passed, Test5-Failed” the output would be:
Test1, Test2, Test4

Key takeaways

The types of advanced regular expressions explained in this reading are just some of the more commonly used ones by developers.
They are beneficial in pattern matching, text manipulation, and data validation. For more information, check out the following link:"""




import os
import re
from regex_logging import RegexLogger
from abc import ABC, abstractmethod

class RegexOperations(ABC):
    """Abstract base class for regex operations."""
    def __init__(self, text_list, logger):
        if not isinstance(text_list, list):
            raise ValueError("text_list must be a list of strings")
        self.text_list = text_list
        self.logger = logger

    @abstractmethod
    def extract_groups(self, pattern, index=None):
        pass



    def print_result(self, operation_name, pattern, results, index=None):
        """Console output method—keeps logging separate."""

        target = (
            f"on items {index.start + 1} to {index.stop}"
            if isinstance(index, slice) else f"on item {index + 1}"
            if isinstance(index, int) else "on all items"
        )

        print(f"{operation_name} using pattern '{pattern}' {target}:")

        if isinstance(results, list):
            for idx, result in enumerate(results, start=1):
                print(f"- Text {idx}: {result or 'No match found'}")
        else:
            print(f"- {results or 'No match found'}")


    def log_result(self, operation_name, pattern, results):
        log_msg = f"{operation_name} using pattern '{pattern}' with results: {results}"

        if results is None:  # Invalid regex
            self.logger.log_error_regex_implementation(operation_name, f"Failed execution: {log_msg}", "regex_error.log")
        elif any(results):  # Successful match
            self.logger.log_successful_regex_implementation(operation_name, log_msg, "regex_success.log")
        else:  # No match found
            self.logger.log_warning_regex_implementation(operation_name, log_msg, "regex_warning.log")


class RegexDemo(RegexOperations):
    """Concrete implementation of RegexOperations."""


    def validate_pattern(self, pattern):
            """Checks if the regex pattern is valid."""
            try:
                re.compile(pattern)
                return True
            except re.error:
                self.logger.log_error_regex_implementation("Validate Pattern", f"Invalid regex pattern: {pattern}",
                                                           "regex_error.log")
                return False
    def get_target_texts(self, index):
        """Helper method to retrieve target texts based on index type."""
        if isinstance(index, slice):
            return self.text_list[index.start:index.stop]  # Extract proper subset
        elif isinstance(index, int):
            return [self.text_list[index]] if 0 <= index < len(self.text_list) else []
        return self.text_list  # Full list if index is None

    def search_example(self, pattern, index=None):
        texts = self.get_target_texts(index)
        results = [re.search(pattern, text).group() if re.search(pattern, text) else None for text in texts]
        self.print_result("Search", pattern, results, index)
        return results

    def match_example(self, pattern, index=None):
        texts = self.get_target_texts(index)
        results = [re.match(pattern, text).group() if re.match(pattern, text) else None for text in texts]
        self.print_result("Match", pattern, results, index)
        return results

    def findall_example(self, pattern, index=None):
        texts = self.get_target_texts(index)
        results = [re.findall(pattern, text) for text in texts]
        self.print_result("Find All", pattern, results, index)
        return results

#regex
    def sub_example(self, pattern, replacement, index=None):
        texts = self.get_target_texts(index)
        results = [re.sub(pattern, replacement, text) for text in texts]
        self.print_result("Substitution", pattern, results, index)
        return results

#strings - (not re module related)
    def replace_example(self, pattern, replacement, index=None):
        texts = self.get_target_texts(index)
        results = [re.replace(pattern, replacement, text) for text in texts]
        self.print_result("Substitution", pattern, results, index)
        return results

    def split_example(self, pattern, index=None):
        texts = self.get_target_texts(index)
        results = [re.split(pattern, text) for text in texts]
        self.print_result("Split", pattern, results, index)
        return results

    def extract_groups(self, pattern, index=None):
        """Extracts regex groups from matches in a specific or all text items."""
        texts = self.get_target_texts(index)
        results = []

        for text in texts:
            match = re.search(pattern, text)
            results.append(match.groups() if match else None)

        self.print_result("Extract Groups", pattern, results, index)
        return results


# Example usage
texts = [
    "Hello, world! This is a sample text for regex demo.",
    "Python Programming!",
    "banana",
    "pineapple",
    "Animal Kingdom",
    "A is for apple",
    "google.com",
    "uncomment"]

texts2 = [
    "Order ID: 54321, Date: 2025-05-19",
    "User ID: ABC123, Status: Active",
    "Invoice No: 987654, Due: 2025-06-01"
]
logger = RegexLogger(os.getcwd())
demo2 = RegexDemo(texts2, logger)




# Extract User ID using regex groups from second item
demo2.extract_groups(r"User ID: (\w+), Status: (\w+)", index=1)
# Extract Order ID and Date using regex groups
demo2.extract_groups(r"Order ID: (\d+), Date: (\d{4}-\d{2}-\d{2})")



demo = RegexDemo(texts, logger)


demo.search_example(r"world",0)
demo.search_example(r"[.,:;!?]",1)

#Wild character search --> Python Programming!
demo.search_example(r"Py.*",1)
#Wild character search --> Python (no spaces)
demo.search_example(r"Py[a-z]*n",1)


#The repeating_letter_a function checks if the text passed includes the letter "a" (lowercase or uppercase) at least twice.
#For example, repeating_letter_a("banana") is True, while repeating_letter_a("pineapple") is False.
demo.search_example(r"[aA].*[aA]",slice(2, len(texts)))
#escape charaters --> .com
demo.search_example(r"\.com",slice(6, len(texts)))
#no escape characters --> Uncom
demo.search_example(r".com",slice(6, len(texts)))
demo.search_example(r"[a-zA-Z]{6}")



demo.findall_example(r"[.,:;!?]",0)
demo.findall_example(r"\w+")
demo.match_example(r"Hello")
demo.sub_example(r"sample", "awesome")
demo.split_example(r"\s+")







def check_zip_code(text):
    pattern = r"\s+\d{5}(-\d{4})?\b"  # Requires at least one space before the ZIP code
    return bool(re.search(pattern, text))

# Test cases
print(check_zip_code(" ZIP code is 90210."))  # True (space before ZIP)
print(check_zip_code("Send it to  12345-6789."))  # True (multiple spaces before ZIP)
print(check_zip_code("Invalid:12345"))  # False (no space before ZIP)
print(check_zip_code("Wrong format: 123456"))  # False (too many digits)
print(check_zip_code("ZIP+4 error: 12345-678"))  # False (ZIP+4 must have exactly 4 digits after '-')
print(check_zip_code("Not a ZIP: ABCDE"))  # False (not numeric)


def extract_secure_domain(url):
    pattern = r"https://www\.([a-zA-Z0-9-]+)\.(com|co)"
    match = re.search(pattern, url)
    return match.group(1) if match else None

# Test cases
urls = [
    "https://www.example.com",
    "http://www.test.com",
    "https://www.my-site.co",
    "http://www.another.co",
    "https://www.secure123.com",
    "http://www.unsecure-site.co"
]

for url in urls:
    result = extract_secure_domain(url)
    print(f"URL: {url} → Extracted: {result}")



def parse_city_state(text):
    """Extracts the state from a city-state field where they are separated by a comma or period."""
    pattern = r"[\w\s]+[,.]\s*([A-Z]{2})$"  # Captures the state (assumed to be a two-letter code)
    match = re.search(pattern, text)
    return match.group(1) if match else None

# Test cases
data = [
    "San Francisco, CA",
    "New York. NY",
    "Los Angeles, CA",
    "Austin. TX",
    "Chicago, IL",
    "Miami. FL",
    "Seattle, WA",
    "Denver. CO"
]

for entry in data:
    state = parse_city_state(entry)
    print(f"Input: {entry} → State: {state}")




    def parse_city_state(text):
        """Extracts the state from a city-state field, supporting abbreviations and full names."""
        pattern = r"[\w\s]+[,.]\s*([A-Z]{2}|(?:[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*))$"
        matches = re.findall(pattern, text)
        return matches[0] if matches else None  # Returns only the state


    # Test cases
    data = [
        "Hamilton, MN",
        "Albuquerque, New Mexico",
        "Portland, Oregon",
        "Chicago, IL",
        "Austin. Texas",
        "New York. NY",
        "Los Angeles, CA",
        "Denver. Colorado"
    ]

    for entry in data:
        state = parse_city_state(entry)
        print(f"Input: {entry} → State: {state}")

    import re


    def show_time_of_pid(line):
        """Extracts date, time, and process ID from syslog entries."""
        pattern = r"^([A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}).*\[(\d+)\]"
        match = re.search(pattern, line)

        return f"{match.group(1)} pid:{match.group(2)}" if match else None


    # Test cases
    logs = [
        "Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)",
        "Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)",
        "Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing",
        "Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)"
    ]

    for log in logs:
        print(show_time_of_pid(log))

