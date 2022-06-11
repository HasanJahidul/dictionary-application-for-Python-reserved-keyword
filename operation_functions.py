from dictionary import keywords
from printing_functions import main_menu, thanks


def add_keyword():
    print("Wanna go back? Press 'b'")
    input_keyword = input("Please enter the keyword: ")
    
    while input_keyword.lower() != "b":
        for key, value in keywords.items():
            if input_keyword.lower() == key.lower():
                print("Keyword already exists")
                break
        else:
            input_description = input("Please enter the description: ")
            input_sample_code = input("Please enter the sample code: ")
            keywords[input_keyword] = {
                "name": input_keyword,
                "des": input_description,
                "sc": input_sample_code
            }
            print("Keyword added successfully")
            break
        break
    else:
        main_menu()
        user_input()





def search():
    print("Wanna go back? Press 'b'")
    input_keyword = input("Please enter the keyword: ")
    while input_keyword.lower() != "b":
        for key, value in keywords.items():
            if input_keyword.lower() == key.lower():
                print("Name:", value["name"])
                print("Description:", value["des"])
                print("Sample Code:", value["sc"])
                break
        else:
            print("Name not found")
        break
    else:
        main_menu()
        user_input()


def remove():
    print("Wanna go back? Press 'b'")
    input_keyword = input("Please enter the keyword: ")
    while input_keyword.lower() != "b":
        for key, value in keywords.items():
            if input_keyword.lower() == key.lower():
                del keywords[key]
                print("Keyword removed successfully")
                break
        else:
            print("Keyword not found")
        break
    else:
        main_menu()
        user_input()


def remove_all():
    keywords.clear()
    print("All keywords removed successfully")


def show_all():
    count = 0
    for key, value in keywords.items():
        count += 1
        print("Keyword", count, ":", key)
        for key, value in value.items():
            print(key+": ", value)
        print("********************************************************************")
    print("********************************************************************")
    main_menu()
    user_input()


def export():
    with open("keywords.txt", "w") as f:
        count = 0
        for key, value in keywords.items():
            count += 1
            print(str(count)+".", file=f)
            for key, value in value.items():
                f.write(key + ": " + value + "\n")
            f.write(
                "********************************************************************\n")
    print("File exported")
    main_menu()
    user_input()


def user_input():
    menu = input("Please enter your choice: ")
    while menu != "8":
        if menu == "1":
            add_keyword()
        elif menu == "2":
            # update_menu()
            print("Update a keyword")
        elif menu == "3":
            remove()
        elif menu == "4":
            show_all()
        elif menu == "5":
            search()
        elif menu == "6":
            export()
        elif menu == "7":
            remove_all()
        else:
            print("Invalid choice")
    thanks()
