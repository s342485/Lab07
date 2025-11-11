import flet as ft

import database
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view
        self._lista_musei = []
        self._lista_epoche = []

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    def dropdown_musei(self):
        self._lista_musei = [ft.dropdown.Option("Nessun filtro")] #prima opzione nessun filtro
        db_musei = self._model.get_musei()
        for museo in db_musei:
            self._lista_musei.append( #aggiunge alla list view i musei del db
                ft.dropdown.Option(museo.nome)
            )
        return self._lista_musei

    def dropdown_epoche(self):
        self._lista_epoche = [ft.dropdown.Option("Nessun filtro")]
        db_epoche = self._model.get_epoche()
        for epoca in db_epoche:
            self._lista_epoche.append(ft.dropdown.Option(epoca))
        return self._lista_epoche

    def callback_scelte(self, museo_selezionato, epoca_selezionata):
        self._view.lista_filtrata.controls.clear()

        museo = None if not museo_selezionato or museo_selezionato == "Nessun filtro" else museo_selezionato
        epoca = None if not epoca_selezionata or epoca_selezionata == "Nessun filtro" else epoca_selezionata

        try:
            lista_db = self._model.get_artefatti_filtrati(museo, epoca)
            if not lista_db:
                self._view.show_alert("Nessun artefatto trovato con i filtri selezionati.")
            else:
                for a in lista_db:
                    self._view.lista_filtrata.controls.append(
                        ft.Text(f"{a.id} - {a.nome} - {a.tipologia} - {a.epoca}")
                    )
        except Exception as e:
            self._view.show_alert(f"Errore nel caricamento degli artefatti: {e}")

        self._view.update()
