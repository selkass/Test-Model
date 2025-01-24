import numpy as np
import pandas as pd  # Importer Pandas

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convertir la liste en une matrice 3x3
    matrix = np.array(lst).reshape(3, 3)
    
    # Calculer les statistiques
    calculations = {
        'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().tolist()],
        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var().tolist()],
        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().tolist()],
        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().tolist()],
        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().tolist()],
        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().tolist()]
    }
    
    # Créer un DataFrame Pandas pour organiser les résultats
    df = pd.DataFrame(calculations, index=['Axis 0 (Columns)', 'Axis 1 (Rows)', 'Flattened'])
    
    return calculations, df  # Retourner à la fois le dictionnaire et le DataFrame