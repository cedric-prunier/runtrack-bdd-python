import mysql.connector


class ZooDatabase:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost", user="root", password="Egypte3813", database="zoo"
        )
        self.cursor = self.db.cursor()

    def get_animal(self, nom, race):
        query = "SELECT * FROM animaux WHERE nom = %s AND race = %s"
        values = (nom, race)
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()
        return result

    def add_animal(self, nom, race, id_cage, date_naissance, pays_origine):
        query = "INSERT INTO animaux (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
        values = (nom, race, id_cage, date_naissance, pays_origine)
        self.cursor.execute(query, values)
        self.db.commit()

    def update_animal(
        self,
        nom,
        race,
        new_nom=None,
        new_race=None,
        new_animal_id=None,
        new_id_cage=None,
        new_date_naissance=None,
        new_pays_origine=None,
    ):
        animal = self.list_animaux(nom, race)
        if animal:
            animal = list(animal)  # convert tuple to list to modify the animal
            if new_nom:
                animal[1] = new_nom
            if new_race:
                animal[2] = new_race
            if new_animal_id:
                animal[0] = new_animal_id
            if new_id_cage:
                animal[3] = new_id_cage
            if new_date_naissance:
                animal[4] = new_date_naissance
            if new_pays_origine:
                animal[5] = new_pays_origine
            animal = tuple(animal)  # convert list back to tuple to update the database
            query = "UPDATE animaux SET nom = %s, race = %s, animal_id = %s, id_cage = %s, date_naissance = %s, pays_origine = %s WHERE nom = %s"
            values = (
                animal[1],
                animal[2],
                animal[0],
                animal[3],
                animal[4],
                animal[5],
                nom,
            )
            self.cursor.execute(query, values)
            self.db.commit()
            return True
        else:
            return False

    def delete_animal(self, nom):
        query = "DELETE FROM animaux WHERE nom = %s"
        values = (nom,)
        self.cursor.execute(query, values)
        self.db.commit()

    def get_cage_by_id(self, cage_id):
        query = "SELECT * FROM cages WHERE id = %s"
        values = (cage_id,)
        self.cursor.execute(query, values)
        return self.cursor.fetchone()

    def add_cage(self, superficie, capacite_max):
        query = "INSERT INTO cages (superficie, capacite_max) VALUES (%s, %s)"
        values = (superficie, capacite_max)
        self.cursor.execute(query, values)
        self.db.commit()

    def update_cage(self, cage_id, new_superficie=None, new_capacite_max=None):
        cage = self.get_cage_by_id(cage_id)
        if cage:
            cage = list(cage)  # convert tuple to list to modify the cage
            if new_superficie:
                cage[1] = new_superficie
            if new_capacite_max:
                cage[2] = new_capacite_max
            cage = tuple(cage)  # convert list back to tuple to update the database
            query = "UPDATE cages SET superficie = %s, capacite_max = %s WHERE id = %s"
            values = (cage[1], cage[2], cage[0])
            self.cursor.execute(query, values)
            self.db.commit()
            return True
        else:
            return False

    def delete_cage(self, cage_id):
        query = "DELETE FROM cages WHERE id = %s"
        values = (cage_id,)
        self.cursor.execute(query, values)
        self.db.commit()

    def list_animaux(self):
        query = "SELECT * FROM animaux"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def list_animaux_par_cage(self):
        query = "SELECT animaux.nom, animaux.race, cages.id AS cage_id, cages.superficie, cages.capacite_max FROM animaux JOIN cages ON animaux.id_cage = cages.id;"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def superficie_totale_cages(self):
        query = "SELECT SUM(superficie) FROM cages"
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]


def show_menu():
    print("Menu:")
    print("1. Ajouter un animal")
    print("2. Supprimer un animal")
    print("3. Modifier un animal")
    print("4. Ajouter une cage")
    print("5. Supprimer une cage")
    print("6. Modifier une cage")
    print("7. Afficher les animaux")
    print("8. Afficher les animaux par cage")
    print("9. Calculer la superficie totale des cages")
    print("0. Quitter")


def modify_animal(zoo_db):
    nom = input("Saisir le nom de l'animal à modifier: ")
    race = input("Saisir la race de l'animal à modifier: ")

    new_nom = input("Saisir le nouveau nom (laisser vide pour ne pas changer): ")
    new_race = input("Saisir la nouvelle race (laisser vide pour ne pas changer): ")
    new_id_cage_str = input(
        "Saisir le nouvel ID de cage (laisser vide pour ne pas changer): "
    )
    new_date_naissance = input(
        "Saisir la nouvelle date de naissance (laisser vide pour ne pas changer): "
    )
    new_pays_origine = input(
        "Saisir le nouveau pays d'origine (laisser vide pour ne pas changer): "
    )

    new_id_cage = int(new_id_cage_str) if new_id_cage_str else None

    if new_nom or new_race or new_id_cage or new_date_naissance or new_pays_origine:
        updated = zoo_db.update_animal(
            nom,
            race,
            new_nom=new_nom,
            new_race=new_race,
            new_id_cage=new_id_cage,
            new_date_naissance=new_date_naissance,
            new_pays_origine=new_pays_origine,
        )
        if updated:
            print(f"L'animal '{nom}' de race '{race}' a été mis à jour.")
        else:
            print("Aucun animal trouvé avec le nom et la race spécifiés.")
    else:
        print("Aucune modification fournie.")


def delete_animal(zoo_db):
    nom = input("Saisir le nom de l'animal à supprimer: ")
    zoo_db.delete_animal(nom)
    print(f"L'animal avec le nom '{nom}' a été supprimé.")


def add_animal():
    nom = input("Entrez le nom de l'animal: ")
    race = input("Entrez la race de l'animal: ")
    id_cage = int(input("Entrez l'ID de la cage: "))
    date_naissance = input(
        "Entrez la date de naissance de l'animal (format YYYY-MM-DD): "
    )
    pays_origine = input("Entrez le pays d'origine de l'animal: ")

    zoo_db.add_animal(nom, race, id_cage, date_naissance, pays_origine)


def add_cage(zoo_db):
    superficie = float(input("Entrez la superficie de la cage en m²: "))
    capacite_max = int(input("Entrez la capacité maximale de la cage: "))

    zoo_db.add_cage(superficie, capacite_max)

    print("La cage a été ajoutée avec succès.")


def modify_cage(zoo_db):
    cage_id = int(input("Saisir l'ID de la cage à modifier: "))
    new_superficie_str = input(
        "Saisir la nouvelle superficie (laisser vide pour ne pas changer): "
    )
    new_capacite_max_str = input(
        "Saisir la nouvelle capacité maximale (laisser vide pour ne pas changer): "
    )

    new_superficie = float(new_superficie_str) if new_superficie_str else None
    new_capacite_max = int(new_capacite_max_str) if new_capacite_max_str else None

    if new_superficie or new_capacite_max:
        updated = zoo_db.update_cage(
            cage_id,
            new_superficie=new_superficie,
            new_capacite_max=new_capacite_max,
        )
        if updated:
            print(f"La cage avec l'ID '{cage_id}' a été mise à jour.")
        else:
            print(f"Aucune cage trouvée avec l'ID '{cage_id}'.")
    else:
        print("Aucune modification fournie.")


def delete_cage(zoo_db):
    cage_id = int(input("Entrez l'ID de la cage à supprimer: "))

    zoo_db.delete_cage(cage_id)

    print("La cage a été supprimée avec succès.")


def handle_menu_choice(zoo_db, choice):
    if choice == 1:
        add_animal()
    elif choice == 2:
        delete_animal(zoo_db)
    elif choice == 3:
        modify_animal(zoo_db)
    elif choice == 4:
        add_cage(zoo_db)
    elif choice == 5:
        delete_cage(zoo_db)
    elif choice == 6:
        modify_cage(zoo_db)
    elif choice == 7:
        animaux = zoo_db.list_animaux()
        for animal in animaux:
            print(animal)
    elif choice == 8:
        animaux_par_cage = zoo_db.list_animaux_par_cage()
        for animal_cage in animaux_par_cage:
            print(animal_cage)
    elif choice == 9:
        superficie_totale = zoo_db.superficie_totale_cages()
        print("Superficie totale des cages:", superficie_totale, "m2")
    elif choice == 0:
        return False
    else:
        print("Choix invalide.")
    return True


zoo_db = ZooDatabase()

while True:
    show_menu()
    choice = int(input("Veuillez choisir une option (0-9): "))
    should_continue = handle_menu_choice(zoo_db, choice)
    if not should_continue:
        break
