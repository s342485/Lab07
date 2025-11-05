from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        self._musei = []

    #elenco di tutti i musei
    def get_all_musei(self) -> list[Museo] |None:
    #Funzione che legge tutti i musei nel database
        if len(self._musei) == 0:
            cnx = ConnessioneDB.get_connection()
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM museo") #prende tutti i musei
            result = cursor.fetchall() # prende tutte le righe

            for row in result:
                museo = Museo(
                    row["id"],
                    row["nome"],
                    row["tipologia"]
                )
                self._musei.append(museo)
            cursor.close()
            cnx.close()
            return self._musei
