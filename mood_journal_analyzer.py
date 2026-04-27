entry_file = input("Enter file name: ")
if len (entry_file) < 1:
    print("File name not entered")
else:
    filename = entry_file + ".txt"
    e_file = open(filename,"a")
    
    while True:
        journal_entry = input("Spill the teaaaa: ")

        if journal_entry.uppercase()=="QUIT":
            break
        with open(filename,"a") as e_file:
            e_file.write (journal_entry + "\n")
    print(f"All entries saved to {filename}.")
