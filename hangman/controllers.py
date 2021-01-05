from ..utils.menus import Menu
from ..views import HomeMenuView


class ApplicationController:
    def __init__(self):
        self.controller = None

    def start(self):
        self.controller = HomeMenuController(self)
        while self.controller:
            self.controller = self.controller()


class HomeMenuController:
    def __init__(self, app):
        self.app = app
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self):
        # 1. Construire un menu
        self.menu.add("auto", "se connecter", ConnectionMenuController())
        self.menu.add("auto", "commencer une partie", NewGameController())
        self.menu.add("q", "quitter", EndScreenController())

        # 2. Demander à la vue d'afficher le menu et de collecter la réponse de l'utilisateur
        user_choice = self.view.get_user_choice()

        # 3. Retourner le controller associé au choix de l'utilisateur au contrôleur principal
        return user_choice.handler


class ConnectionMenuController:
    def __call__(self):
        print("dans le controleur de connection")
        return HomeMenuController()


class SignupMenuController:
    pass


class NewGameController:
    def __call__(self):
        print("dans le controleur de nouvelle partie")
        return EndScreenController()


class OngoingGameController:
    pass


class RankingController:
    pass


class EndScreenController:
    def __call__(self):
        print("dans le controleur de fin: bye bye")