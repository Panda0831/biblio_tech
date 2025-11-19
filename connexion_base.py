import sqlite3

class ConnexionBase:
    @classmethod
    def get_connection(cls):
        """Retourne une connexion SQLite vers la base bibliotheque.db"""
        return sqlite3.connect("bibliotheque.db")

    @classmethod
    def initialisation_bd(cls):
        """Crée les tables si elles n'existent pas déjà"""
        conn = cls.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Categories (
            id_categorie INTEGER PRIMARY KEY AUTOINCREMENT,
            titre_categorie TEXT NOT NULL
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Livres (
            id_livre INTEGER PRIMARY KEY AUTOINCREMENT,
            titre_livre TEXT NOT NULL,
            id_categorie INTEGER,
            FOREIGN KEY (id_categorie) REFERENCES Categories(id_categorie)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Membres (
            id_membre INTEGER PRIMARY KEY AUTOINCREMENT,
            nom_membre TEXT NOT NULL,
            contact_membre TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Emprunts (
            id_emprunt INTEGER PRIMARY KEY AUTOINCREMENT,
            id_livre INTEGER NOT NULL,
            id_membre INTEGER NOT NULL,
            date_emprunt DATE,
            date_retour_prevu DATE,
            date_retour DATE,
            FOREIGN KEY (id_livre) REFERENCES Livres(id_livre),
            FOREIGN KEY (id_membre) REFERENCES Membres(id_membre)
        )
        """)

        conn.commit()
        conn.close()
        print(" BISOUS")
