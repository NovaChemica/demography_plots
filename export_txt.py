"""Classe utilisable pour représenter des données en .txt"""

class Data:
    """Représente un ensemble de données"""
    def __init__(self, data):
        """Initialisation d'une instance par un jeu de données"""
        self.data = data
        
    def to_txt(self):
        """tranformation du fichier en fichier txt"""
        with open(self) as data_object:
            lines = data_object.readlines()
            enumerate(colonnes, 1) = lines.split(',')
            

    