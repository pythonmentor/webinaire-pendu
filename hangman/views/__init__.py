class HomeMenuView:
    def __init__(self, menu):
        self.menu = menu

    def _display_menu(self):
        print("Accueil de notre jeu:")
        for key, entry in self.menu.items():
            print(f"{key}: {entry.option}")
        print()

    def get_user_choice(self):
        while True:
            # afficher le menu à l'utilisateur
            self._display_menu()
            # demander à l'utilisateur de faire un choix
            choice = input(">> ")
            # valider de l'utilisateur
            if choice in self.menu:
                # retourner le choix de l'utilisateur
                return self.menu[choice]
