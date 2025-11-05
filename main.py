import flet as ft

from model.model import Model
from UI.view import View
from UI.controller import Controller
from database import artefatto_DAO

def main(page: ft.Page):
    my_model = Model()
    my_view = View(page)
    my_controller = Controller(my_view, my_model)
    my_view.set_controller(my_controller)

    #dao = artefatto_DAO.ArtefattoDAO()
    #print(dao.get_all_epoche())

    my_view.load_interface()


ft.app(target=main)
