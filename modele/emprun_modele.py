from connexion_base import ConnexionBase



class EmpruntModele:
    @classmethod
    def enregistrer_emprunt(cls, id_livre, id_membre, date_emprunt, date_retour_prevu):
        conn = ConnexionBase.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Emprunts (id_livre, id_membre, date_emprunt, date_retour_prevu)
            VALUES (?, ?, ?, ?)
        """, (id_livre, id_membre, date_emprunt, date_retour_prevu))
        conn.commit()
        conn.close()

    @classmethod
    def retourner_livre(cls, id_emprunt, date_retour):
        conn = ConnexionBase.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Emprunts
            SET date_retour=?
            WHERE id_emprunt=?
        """, (date_retour, id_emprunt))
        conn.commit()
        conn.close()

    @classmethod
    def get_all_emprunts(cls):
        conn = ConnexionBase.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Emprunts")
        emprunts = cursor.fetchall()
        conn.close()
        return emprunts

    @classmethod
    def get_emprunt_by_id(cls, id_emprunt):
        conn = ConnexionBase.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Emprunts WHERE id_emprunt=?", (id_emprunt,))
        emprunt = cursor.fetchone()
        conn.close()
        return emprunt

    @classmethod
    def get_emprunts_by_membre(cls, id_membre):
        conn = ConnexionBase.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Emprunts WHERE id_membre=?", (id_membre,))
        emprunts = cursor.fetchall()
        conn.close()
        return emprunts
    @classmethod
    def get_emprunts_by_livre(cls, id_livre):
        conn = ConnexionBase.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Emprunts WHERE id_livre=?", (id_livre,))
        emprunts = cursor.fetchall()
        conn.close()
        return emprunts
    @classmethod
    def get_emprunts_en_cours(cls):
        conn = ConnexionBase.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Emprunts WHERE date_retour IS NULL")
        emprunts = cursor.fetchall()
        conn.close()
        return emprunts
    @classmethod
    def get_emprunts_terminees(cls):
        conn = ConnexionBase.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Emprunts WHERE date_retour IS NOT NULL")
        emprunts = cursor.fetchall()
        conn.close()
        return emprunts
    @classmethod
    def supprimer_emprunt(cls, id_emprunt):
        conn = ConnexionBase.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Emprunts WHERE id_emprunt=?", (id_emprunt,))
        conn.commit()
        conn.close()
    @classmethod
    def get_emprunts_en_cours_by_membre(cls, id_membre):
        conn = ConnexionBase.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Emprunts WHERE id_membre=? AND date_retour IS NULL", (id_membre,))
        emprunts = cursor.fetchall()
        conn.close()
        return emprunts
    @classmethod
    def get_emprunt_by_membre_livre(cls, id_membre, id_livre):
        conn = ConnexionBase.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM Emprunts
            WHERE id_membre=? AND id_livre=? AND date_retour IS NULL
        """, (id_membre, id_livre))
        emprunt = cursor.fetchone()
        conn.close()
        return emprunt

    @classmethod
    def modifier_emprunt(cls, id_emprunt, id_livre, id_membre, date_emprunt, date_retour_prevu):
        conn = ConnexionBase.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Emprunts
            SET id_livre=?, id_membre=?, date_emprunt=?, date_retour_prevu=?
            WHERE id_emprunt=?
        """, (id_livre, id_membre, date_emprunt, date_retour_prevu, id_emprunt))
        conn.commit()
        conn.close()