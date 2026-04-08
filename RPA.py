Entries = list()
def get_non_empty_input(prompt):
    while True:
        value=input(prompt)
        if len(value.strip())== 0:
            print("This field cannot be empty.")
        else:
            return value

while True:
    print("Log in your details of your current read")
    title=get_non_empty_input("Enter the title of your book: ")
    author=get_non_empty_input("Enter name of the author: ")
    genre=get_non_empty_input("Enter book genre: ")
    pages=int(get_non_empty_input("Enter number of pages: "))
    start=get_non_empty_input("Enter date for starting book: ")
    end=get_non_empty_input("Enter date for ending book: ")

    Entry=dict()
    #fixing my inputted values into the dictionary called Entry
    Entry['Title']=title
    Entry['Author']=author
    Entry['Genre']=genre
    Entry['Pages']=pages
    Entry['Start']=start
    Entry['End']=end
    
    #appending the dictionary into the list
    Entries.append(Entry)
    print("Book detail overview: ",Entry)
    
    choice=input("Add another book? (yes/no): ")
    if choice.lower()=="no":
        break
print("you've read:",len(Entries),"book(s) in total")

pages = list()
for item in Entries:
    Page=item["Pages"]
    pages.append(Page)
print("In total you've read:",sum(pages),"pages")