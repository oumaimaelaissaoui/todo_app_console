import json
import os
def show_menu():
    print("\n===== TODO APP =====")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Marquer une tâche comme terminée")
    print("4. Supprimer une tâche")
    print("5. Quitter")

def add_task(tasks):
    title = input("Enter task title: ")
    task = {
        "title": title,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")

def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return

    for i, task in enumerate(tasks):
        status = "✔" if task["completed"] else "✖"
        print(f"{i + 1}. {task['title']} [{status}]")

    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Task '{removed['title']}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def show_tasks(tasks):
    if not tasks:
        print("Aucune tâche pour le moment.")
        return

    print("\n  Liste des tâches :")
    for index, task in enumerate(tasks, start=1):
        status = " Terminée" if task["completed"] else " Non terminée"
        print(f"{index}. {task['title']} - {status}")

def complete_task(tasks):
    show_tasks(tasks)

    if not tasks:
        return

    try:
        task_number = int(input("\nEntrez le numéro de la tâche à terminer : "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print("🎉 Tâche marquée comme terminée !")
        else:
            print("⚠️ Numéro invalide.")
    except ValueError:
        print("⚠️ Veuillez entrer un nombre valide.")

def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choisissez une option : ")

        if choice == "1":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Au revoir 👋")
            break
        else:
            print("Choix invalide ❌")


if __name__ == "__main__":
    main()
