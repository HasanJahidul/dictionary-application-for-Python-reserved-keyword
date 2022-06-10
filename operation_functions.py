from dictionary import keywords
def search():
    input_keyword = input("Please enter the keyword: ")
    for key, value in keywords.items():
        if input_keyword.lower() == key.lower():
            print("Name:", value["name"])
            print("Description:", value["des"])
            print("Sample Code:", value["sc"])
            break
    else:
        print("Name not found")


def remove():
    input_keyword = input("Please enter the keyword: ")
    for key, value in keywords.items():
        if input_keyword.lower() == key.lower():
            del keywords[key]
            print("Keyword removed successfully")
            break
    else:
        print("Keyword not found")

def remove_all():
    keywords.clear()
    print("All keywords removed successfully")


def show_all():
    count=0
    for key, value in keywords.items():
        count+=1
        print("Keyword", count, ":", key)
        for key, value in value.items():
            print("Name:", value["name"])
            print("Description:", value["des"])
            print("Sample Code:", value["sc"])
            print("********************************************************************")
def export():
    with open("keywords.txt", "w") as f:
        count = 0
        for key, value in keywords.items():
            count += 1
            print(str(count)+".", file=f)
            for key, value in value.items():
                f.write(key + ": " + value + "\n")
                f.write("********************************************************************\n")




