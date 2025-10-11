# Python program demonstrating different string functions
def string_functions_demo():
    text = "  hello, welcome to the world of Python programming!  "
    print("Original text:", repr(text))
    # Remove leading and trailing spaces
    stripped_text = text.strip()
    print("After strip():", repr(stripped_text))
    # Convert to uppercase
    upper_text = stripped_text.upper()
    print("After upper():", upper_text)
    # Convert to lowercase
    lower_text = stripped_text.lower()
    print("After lower():", lower_text)
    # Convert to title case
    title_text = stripped_text.title()
    print("After title():", title_text)
    # Replace word
    replaced_text = stripped_text.replace("Python", "Java")
    print("After replace():", replaced_text)
    # Find position of a substring
    pos = stripped_text.find("welcome")
    print("Position of 'welcome':", pos)
    # Split into list
    words_list = stripped_text.split()
    print("After split():", words_list)
    # Join list back into string with '-'
    joined_text = '-'.join(words_list)
    print("After join():", joined_text)
    # Check if text starts with 'hello'
    starts = stripped_text.startswith("hello")
    print("Starts with 'hello':", starts)
    # Check if text ends with 'programming!'
    ends = stripped_text.endswith("programming!")
    print("Ends with 'programming!':", ends)
    # Count occurrences of a character
    count_o = stripped_text.count('o')
    print("Number of 'o':", count_o)
    # Capitalize first letter
    capitalized_text = stripped_text.capitalize()
    print("After capitalize():", capitalized_text)
# Run the demo
string_functions_demo()
