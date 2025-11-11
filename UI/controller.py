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
        db_musei = self._model.get_musei()
        for museo in db_musei:
            self._lista_musei.append(
                ft.dropdown.Option(museo.id, museo.nome)
            )
        return self._lista_musei

    def dropdown_epoche(self):
        db_epoche = self._model.get_epoche()
        for epoca in db_epoche:
            self._lista_epoche.append(ft.dropdown.Option(epoca))
        return self._lista_epoche

    # CALLBACKS DROPDOWN
    def callback_scelte(self, museo_selezionato, epoca_selezionata):
        self._view.lista_filtrata.controls.clear() #lista da popolare

        try:
            lista_db = self._model.get_artefatti_filtrati(museo_selezionato, epoca_selezionata)
            for artefatto in lista_db:
                self._view.lista_filtrata.controls.append(ft.Text(f"{artefatto}"))
        except Exception as e:
            self._view.show_alert(f"Errore nel caricamento degli artefatti: {e}")

        self._view.update() #riesegue la view aggiornando tutto




    # AZIONE: MOSTRA ARTEFATTI
    # TODO
