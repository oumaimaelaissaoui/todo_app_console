def add_task(tasks):
    """
    Ajoute une nouvelle tâche à la liste des tâches
    """
    title = input("Entrez le nom de la tâche : ")

    if title.strip() == "":
        print("❌ Le nom de la tâche ne peut pas être vide.")
        return

    task = {
        "title": title,
        "completed": False
    }

    tasks.append(task)
    print("✅ Tâche ajoutée avec succès !")

if __name__ == "__main__":
    tasks = []
    add_task(tasks)
    print(tasks)

