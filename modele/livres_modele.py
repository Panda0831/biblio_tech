from connexion_base import ConnexionBase

class LivresModel:
    @classmethod
    def ajouter_livre(cls, titre_livre, id_categorie=None):
        conn = ConnexionBase.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Livres (titre_livre, id_categorie) VALUES (?, ?)",
            (titre_livre, id_categorie)
        )
        conn.commit()
        conn.close()

    @classmethod
    def get_all_livres(cls):
        conn = ConnexionBase.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Livres")
        livres = cursor.fetchall()
        conn.close()
        return livres

    @classmethod
    def get_livre_by_id(cls, id_livre):
        conn = ConnexionBase.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Livres WHERE id_livre=?", (id_livre,))
        livre = cursor.fetchone()
        conn.close()
        return livre

    @classmethod
    def modifier_livre(cls, id_livre, titre_livre, id_categorie):
        conn = ConnexionBase.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Livres
            SET titre_livre=?, id_categorie=?
            WHERE id_livre=?
        """, (titre_livre, id_categorie, id_livre))
        conn.commit()
        conn.close()

    @classmethod
    def supprimer_livre(cls, id_livre):
        conn = ConnexionBase.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Livres WHERE id_livre=?", (id_livre,))
        conn.commit()
        conn.close()
