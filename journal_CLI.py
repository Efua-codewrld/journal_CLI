while True:
    choice = input("1. Add entry\n2. View entries\n3. Exit\nchoose: ")

    if choice == "1":
        journal_entry = input("log in today's journal entry: ")
        print("Today's yap session be looking like: ",journal_entry)
        filename = input("enter a filename that fits your journal vibe: ").strip()
        if len(filename) < 1:
            print("filename not entered")
        else:
            filename= filename +".txt"
            with open(filename,"a") as f:
                f.write(journal_entry + "\n")

    if choice == "2":
        filename = input("Enter file name to view: ")
        with open(filename + ".txt","r") as f:
            content = f.read()
            print(content)
    
    if choice == "3":
        break

    

