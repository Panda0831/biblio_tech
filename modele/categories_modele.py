from connexion_base import ConnexionBase

class CategoriesModel:
    @classmethod
    def ajouter_categorie(cls, titre_categorie):
        conn = ConnexionBase.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Categories (titre_categorie)
            VALUES (?)
        """, (titre_categorie,))
        conn.commit()
        conn.close()
    @classmethod
    def get_all_categories(cls):
        conn = ConnexionBase.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Categories")
        categories = cursor.fetchall()
        conn.close()
        return categories
    @classmethod
    def get_categorie_by_id(cls, id_categorie):
        conn = ConnexionBase.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Categories WHERE id_categorie=?", (id_categorie,))
        categorie = cursor.fetchone()
        conn.close()
        return categorie
    @classmethod
    def modifier_categorie(cls, id_categorie, titre_categorie):
        conn = ConnexionBase.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Categories
            SET titre_categorie=?
            WHERE id_categorie=?
        """, (titre_categorie, id_categorie))
        conn.commit()
        conn.close()
    @classmethod
    def supprimer_categorie(cls, id_categorie):
        conn = ConnexionBase.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Categories WHERE id_categorie=?", (id_categorie,))
        conn.commit()
        conn.close()
    