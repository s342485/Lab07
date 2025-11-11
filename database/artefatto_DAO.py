from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo
from model.artefattoDTO import Artefatto


class ArtefattoDAO:
    def __init__(self):
        pass
    def get_all_epoche(self):
        self._epoche = []
        cnx = ConnessioneDB.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = ("SELECT DISTINCT epoca FROM artefatto")
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            self._epoche.append(row["epoca"])

        cursor.close()
        cnx.close()
        return self._epoche

#rivedi
    def get_all_artefatti(self, museo: str | None = None, epoca: str | None = None) -> list[Artefatto]:
        self._artefatti = []

        cnx = ConnessioneDB.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """
            SELECT a.*
            FROM artefatto a, museo m
            WHERE a.id_museo = m.id AND m.nome  = COALESCE(%s, m.nome) AND a.epoca = COALESCE(%s, a.epoca)
        """
        #COALESCE- se il parametro non è null filtra per nome museo, altrimenti non applica filtro

        cursor.execute(query, (museo, epoca,))
        result = cursor.fetchall()

        for row in result:
            self._artefatti.append(
                Artefatto(
                    row["id"],  # id artefatto
                    row["nome"],  # nome artefatto (non il museo!)
                    row["tipologia"],
                    row["epoca"],
                    row["id_museo"]
                )
            )

        cursor.close()
        cnx.close()

        return self._artefatti

