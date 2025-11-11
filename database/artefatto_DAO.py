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
    def get_all_artefatti(self, museo: int | None = None, epoca: str | None = None) -> list[Artefatto]:
        self._artefatti = []
        cnx = ConnessioneDB.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """
        SELECT *
        FROM artefatto a
        JOIN museo m ON a.id_museo = m.id
        WHERE 1 = 1
        """

        params = []

        if epoca:
            query += " AND a.epoca = %s"
            params.append(epoca)

        if museo:
            query += " AND m.nome = %s"
            params.append(museo)

        print("DAO DEBUG → QUERY:", query)
        print("DAO DEBUG → PARAMS:", params)

        cursor.execute(query, params)
        result = cursor.fetchall()

        print("DAO DEBUG → ROWS:", result)

        for row in result:
            print(" → ARTEFATTO:", row)
            self._artefatti.append(
                Artefatto(
                    row["id"],
                    row["nome"],
                    row["tipologia"],
                    row["epoca"],
                    row["id_museo"]
                )
            )

        cursor.close()
        cnx.close()

        return self._artefatti
