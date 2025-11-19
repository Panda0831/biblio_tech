from connexion_base import ConnexionBase
class MembreModele:
    @classmethod
    def ajouter_membre(cls, nom_membre, contact_membre):
        conn = ConnexionBase.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Membres (nom_membre, contact_membre)
            VALUES (?, ?)
        """, (nom_membre, contact_membre))
        conn.commit()
        conn.close()

    @classmethod
    def get_all_membre(cls):
        conn = ConnexionBase.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Membres")
        membres = cursor.fetchall()
        conn.close()
        return membres
    @classmethod
    def get_membre_by_id(cls, id_membre):
        conn = ConnexionBase.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Membres WHERE id_membre=?", (id_membre,))
        membre = cursor.fetchone()
        conn.close()
        return membre
    @classmethod
    def modifier_membre(cls, id_membre, nom_membre, contact_membre):
        conn = ConnexionBase.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Membres
            SET nom_membre=?, contact_membre=?
            WHERE id_membre=?
        """, (nom_membre, contact_membre, id_membre))
        conn.commit()
        conn.close()
    @classmethod
    def supprimer_membre(cls, id_membre):
        conn = ConnexionBase.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Membres WHERE id_membre=?", (id_membre,))
        conn.commit()
        conn.close()
    @classmethod
    def get_membre_by_nom(cls, nom_membre):
        conn = ConnexionBase.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Membres WHERE nom_membre=?", (nom_membre,))
        membre = cursor.fetchone()
        conn.close()
        return membre
    @classmethod
    def get_membre_by_emprunts(cls, id_membre):
        conn = ConnexionBase.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT m.id_membre, m.nom_membre, m.contact_membre,
                e.id_emprunt, e.date_emprunt, e.date_retour_prevu, e.date_retour,
                l.id_livre, l.titre_livre
            FROM Membres m
            LEFT JOIN Emprunts e ON m.id_membre = e.id_membre
            LEFT JOIN Livres l ON e.id_livre = l.id_livre
            WHERE m.id_membre = ?
        """, (id_membre,))
        
        result = cursor.fetchall()
        conn.close()
        return result
