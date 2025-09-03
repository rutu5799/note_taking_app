FILE_NAME="myNotes.txt"

def show_menu():
    print("\n---------Note Taking Menu--------")
    print("1.Add a note")
    print("2.view all note")
    print("3.Delete all notes")
    print("4.Exit")

def add_note():
    note=input("Enter your note:")
    with open(FILE_NAME,"a") as file:
        file.write(note + "\n")
    print("note added sucessfully")

def view_notes():
    try:
        with open(FILE_NAME,"r") as file:
            content=file.read()
            if content:
                print("\n-----your note----")
                print(content)
            else:
                 print("no notes found.")
    except FileNotFoundError:
            print("No notes found.")

def delete_notes():
    confirm=input("Are you sure you want to delete all notes?(yes/n):")
    if confirm.lower()=="yes":
        with open(FILE_NAME,"w") as file:
            pass
        print("All notes have been deleted")
    else:
        print("Deletion cancelled")

while True:
    show_menu()
    choice=input("Enter your choice(1-4):")

    if choice=="1":
        add_note()
    elif choice=="2":
        view_notes()
    elif choice=="3":
        delete_notes()
    elif choice=="4":
        print("Existing not taking app.Goodbye!")
        break
    else:
        print("Invalid choice.please enter a number between 1 to 4")
