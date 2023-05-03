import mysql.connector

"""Requête terminale

mysql -u root -p

CREATE DATABASE societe;
SHOW DATABASES;

USE societe

CREATE TABLE employes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nom VARCHAR(255),
  prenom VARCHAR(255),
  salaire DECIMAL(10,2),
  id_service INT
);

INSERT INTO employes (nom, prenom, salaire, id_service)
VALUES
  ('Dupont', 'Jean', 2000.50, 1),
  ('Martin', 'Sophie', 2500.75, 2),
  ('Duran', 'Pierre', 3200.50, 3),
  ('Lopez', 'Claire', 3100.50, 4);

SELECT * FROM employes WHERE salaire > 3000;

CREATE TABLE services (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nom VARCHAR(255)
);

SELECT employes.nom, employes.prenom, services.nom AS service_nom
FROM employes
JOIN services ON employes.id_service = services.id;

"""


class EmployeeDatabase:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost", user="root", password="Egypte3813", database="societe"
        )
        self.cursor = self.db.cursor()

    def create_employee(self, nom, prenom, salaire, id_service):
        query_check = "SELECT * FROM employes WHERE nom = %s AND prenom = %s"
        values_check = (nom, prenom)
        self.cursor.execute(query_check, values_check)
        existing_employee = self.cursor.fetchone()

        if not existing_employee:
            query = "INSERT INTO employes (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
            values = (nom, prenom, salaire, id_service)
            self.cursor.execute(query, values)
            self.db.commit()
            return self.cursor.lastrowid
        else:
            print("An employee with this name and surname already exists.")
            return None

    def read_employee(self, nom, prenom):
        query = "SELECT * FROM employes WHERE nom = %s AND prenom = %s"
        values = (nom, prenom)
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()
        if result:
            return {
                "id": result[0],
                "nom": result[1],
                "prenom": result[2],
                "salaire": result[3],
                "id_service": result[4],
            }
        else:
            return None

    def update_employee(
        self,
        nom,
        prenom,
        new_nom=None,
        new_prenom=None,
        new_salaire=None,
        new_id_service=None,
    ):
        employee = self.read_employee(nom, prenom)
        if employee:
            if new_nom:
                employee["nom"] = new_nom
            if new_prenom:
                employee["prenom"] = new_prenom
            if new_salaire:
                employee["salaire"] = new_salaire
            if new_id_service:
                employee["id_service"] = new_id_service
            query = "UPDATE employes SET nom = %s, prenom = %s, salaire = %s, id_service = %s WHERE id = %s"
            values = (
                employee["nom"],
                employee["prenom"],
                employee["salaire"],
                employee["id_service"],
                employee["id"],
            )
            self.cursor.execute(query, values)
            self.db.commit()
            return True
        else:
            return False

    def delete_employee(self, nom, prenom):
        query = "DELETE FROM employes WHERE nom = %s AND prenom = %s"
        values = (nom, prenom)
        self.cursor.execute(query, values)
        self.db.commit()
        return self.cursor.rowcount


### Requête exemples

db = EmployeeDatabase()

# Créer un nouvel employé
employee_id = db.create_employee("Doe", "John", 3500, 1)
print(f"Created employee with ID: {employee_id}")

# Lire les informations d'un employé
employee = db.read_employee("Doe", "John")
print(f"Read employee: {employee}")
# Mettre à jour les informations d'un employé
updated = db.update_employee(
    "Doe",
    "John",
    new_nom="Smith",
    new_prenom="Jane",
    new_salaire=4000,
    new_id_service=2,
)
if updated:
    print("Employee updated successfully.")
else:
    print("Employee update failed.")

# Lire à nouveau les informations de l'employé pour vérifier la mise à jour
employee = db.read_employee("Dupuis", "Clement")
print(f"Updated employee: {employee}")

# Supprimer un employé
deleted = db.delete_employee("Smith", "Jane")
if deleted > 0:
    print("Employee deleted successfully.")
else:
    print("Employee deletion failed.")
