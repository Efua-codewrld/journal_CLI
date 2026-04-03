from datetime import datetime
#setting a standard variable to hold the entry as the file incase no file has been set
current_file = None
while True:
    choice = input("1. Add entry\n2. View entries\n3. change file\n4. Exit\nchoose: ")

    if choice == "1":
        if current_file is None:
            current_file = input("Enter filename: ").strip()
        
        now = datetime.now()
        Date = now.strftime("%d/%m/%Y, %H:%M:%S")

        journal_entry = input("log in today's journal entry: ")
        Mood=input("Okay baddie, what's the mood for today: ")
        print("Today's yap session be looking like: ",journal_entry)
        with open(current_file + ".txt","a") as f:
            f.write( f" {Date} | MOOD {Mood} | {journal_entry}\n")

    if choice == "2":
        filename = input("Enter file name to view: ")
        with open(filename + ".txt","r") as f:
            content = f.read()
            print(content)
    
    #giving the user an option to set a new file to hold entries
    elif choice == "3":
        current_file = input("Enter new filename: ").strip()
    
    if choice == "4":
        break

    

