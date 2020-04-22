# -*- coding: utf-8 -*-

class dao_erreurForm(object):
    @staticmethod
    def erreurInput(e=""):
        return "Veuillez compléter correctement les champs « nom d\'utilisateur » et « mot de passe » d\'un compte autorisé. Sachez que les deux champs peuvent être sensibles à la casse. "+e