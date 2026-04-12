"""
Module: Data Stream Control
Practical: 01 - I/O Stream Management
Objective: Demonstrate controlled data output and modular execution patterns.
"""

# We use type hinting (first: str) to ensure the code is "Self-Documenting."
# '-> None' explicitly tells other developers this function returns no value.
def format_academic_record(first: str, last: str, uid: str) -> None:
    """
    Formats and displays student metadata using controlled output streams.
    
    Technical Mechanism:
    - String Replication: Generates a dynamic border for the UI.
    - Argument Passing: Transfers local scope variables into the function.
    """
    
    # Using the replication operator (*) to create a consistent UI divider.
    # This is more memory-efficient than manually typing 30 '=' characters.
    header = "=" * 30

    # f-strings (formatted string literals) provide the fastest way to 
    # interpolate variables and escape characters like '\n' (new line).
    print(f"\n{header}\nINTERNAL DATA RECORD\n{header}")

    # The 'sep' argument is a powerful print() feature. 
    # Instead of concatenating with '+', Python handles the joining logic
    # internally, reducing the creation of temporary string objects.
    print(first, last, uid, sep=" | ")
    
    print(header)

# This conditional block ensures modularity.
# It prevents the script from executing automatically if it is imported 
# into a larger system (like an AI Security Scanner or a GUI).
if __name__ == "__main__":
    
    # Capturing standard input. By default, input() stores data as a string (UTF-8).
    f_name = input("Identify First Name: ")
    l_name = input("Identify Last Name: ")
    id_code = input("Identify Student ID: ")
    
    # Calling the function and passing arguments into the defined parameters.
    format_academic_record(f_name, l_name, id_code)
