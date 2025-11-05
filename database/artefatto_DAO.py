from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo
from model.artefattoDTO import Artefatto


class ArtefattoDAO:
    def __init__(self):
        pass

#rivedi
    def get_all_artefatti(self, museo: Museo | None = None, epoca: str | None = None) -> list[Artefatto]:
        cnx = ConnessioneDB.get_connection()
        cursor = cnx.cursor(dictionary=True)

        # Query base
        query = """
        SELECT 
            a.id,
            a.nome,
            a.tipologia,
            a.epoca,
            a.id_museo
        FROM artefatto a
        JOIN museo m ON a.id_museo = m.id
        WHERE 1 = 1
        """

        params = []

        # Filtro epoca (se presente)
        if epoca is not None:
            query += " AND a.epoca = %s"
            params.append(epoca)

        # Filtro museo (se presente)
        if museo is not None:
            query += " AND m.id = %s"
            params.append(museo.id)

        cursor.execute(query, params)
        result = cursor.fetchall()

        artefatti = []
        for row in result:
            artefatti.append(
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

        return artefatti
