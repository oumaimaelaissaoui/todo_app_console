import json
import os
def show_menu():
    print("\n===== TODO APP =====")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Marquer une tâche comme terminée")
    print("4. Supprimer une tâche")
    print("5. Quitter")

# main.py

tasks = []  # liste globale des tâches


def add_task():
    title = input("Entrez le nom de la tâche : ")
    task = {
        "title": title,
        "done": False
    }
    tasks.append(task)
    print("✅ Tâche ajoutée avec succès !")


def delete_task():
    if len(tasks) == 0:
        print("❌ Aucune tâche à supprimer.")
        return

    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task['title']}")

    try:
        index = int(input("Entrez le numéro de la tâche à supprimer : "))
        removed_task = tasks.pop(index - 1)
        print(f"🗑️ Tâche '{removed_task['title']}' supprimée.")
    except (ValueError, IndexError):
        print("❌ Numéro invalide.")


def show_tasks():
    if len(tasks) == 0:
        print("📭 Aucune tâche.")
    else:
        for i, task in enumerate(tasks):
            status = "✔️" if task["done"] else "❌"
            print(f"{i + 1}. {task['title']} [{status}]")


# Menu simple pour tester
while True:
    print("\n--- TODO APP ---")
    print("1. Ajouter une tâche")
    print("2. Supprimer une tâche")
    print("3. Afficher les tâches")
    print("4. Quitter")

    choice = input("Choisissez une option : ")

    if choice == "1":
        add_task()
    elif choice == "2":
        delete_task()
    elif choice == "3":
        show_tasks()
    elif choice == "4":
        print("👋 Au revoir")
        break
    else:
        print("❌ Choix invalide")

def main():
    while True:
        show_menu()
        choice = input("Choisissez une option : ")

        if choice == "1":
            print("Fonction add_task à implémenter")
        elif choice == "2":
            print("Fonction show_tasks à implémenter")
        elif choice == "3":
            print("Fonction complete_task à implémenter")
        elif choice == "4":
            print("Fonction delete_task à implémenter")
        elif choice == "5":
            print("Au revoir 👋")
            break
        else:
            print("Choix invalide ❌")




if __name__ == "__main__":
    main()

def show_tasks(tasks):
    if not tasks:
        print("Aucune tâche pour le moment.")
        return

    print("\n  Liste des tâches :")
    for index, task in enumerate(tasks, start=1):
        status = " Terminée" if task["done"] else " Non terminée"
        print(f"{index}. {task['title']} - {status}")

def complete_task(tasks):
    show_tasks(tasks)

    if not tasks:
        return

    try:
        task_number = int(input("\nEntrez le numéro de la tâche à terminer : "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["done"] = True
            print("🎉 Tâche marquée comme terminée !")
        else:
            print("⚠️ Numéro invalide.")
    except ValueError:
        print("⚠️ Veuillez entrer un nombre valide.")

