from mean_var_std import calculate
import pandas as pd

# Exemple d'utilisation
if __name__ == "__main__":
    # Test avec une liste de 9 nombres
    result, df = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
    
    # Afficher le dictionnaire
    print("Dictionnaire des résultats :")
    print(result)
    
    # Configurer Pandas pour afficher le tableau complet
    pd.set_option('display.max_rows', None)  # Afficher toutes les lignes
    pd.set_option('display.max_columns', None)  # Afficher toutes les colonnes
    pd.set_option('display.width', None)  # Ajuster la largeur de l'affichage
    pd.set_option('display.max_colwidth', None)  # Afficher tout le contenu des cellules
    
    # Afficher le tableau Pandas complet
    print("\nTableau organisé avec Pandas (complet) :")
    print(df)