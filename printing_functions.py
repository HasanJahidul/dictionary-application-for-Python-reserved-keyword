import sys
def main_menu():
    print("""********************************************************************
    \tPython Keyword Dictionary Application\n********************************************************************
	You can now perform the following operations on this Application\n
    1.Add a new keyword
    2.Update a keyword
    3.Delete a keyword
    4.Print all keywords
    5.Search for a keyword
    6.Export to a file
    8.Exit
    """)

def update_menu():
    print("""
    1.Update the name of a keyword
    2.Update the description of a keyword
    3.Update the sample code of a keyword
    4.Return to the main menu
    """)

def add_keyword_menu():
    print("""
    1.Add a new keyword
    2.Return to the main menu
    """)
def thanks():
    # A simple gesture of courtesy towards the user to enhance user experience
    print("********************************************************************")
    print("Thank you for using our Python Keyword Management Application.")
    print("Please visit again!")
    print("********************************************************************")
    sys.exit("Goodbye, have a nice day ahead!")