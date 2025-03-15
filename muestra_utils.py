import numpy as np
from scipy import stats

def calculate_z_score(sample_proportion, poblational_proportion, n):
    """
    Calcula el Z-score dado un valor de proporción muestral, proporción poblacional y tamaño de la muestra.
    
    Parámetros:
    sample_proportion (float): Proporción observada en la muestra.
    poblational_proportion (float): Proporción esperada en la población.
    n (int): Tamaño de la muestra.
    
    Retorna:
    float: Valor del Z-score.
    """
    if n <= 0:
        raise ValueError("El tamaño de la muestra (n) debe ser mayor que cero.")
    
    denominator = np.sqrt((poblational_proportion * (1 - poblational_proportion)) / n)
    
    if denominator == 0:
        raise ValueError("El denominador no puede ser cero. Verifica la proporción poblacional y el tamaño de la muestra.")
    
    z_score = (sample_proportion - poblational_proportion) / denominator
    return z_score

def calculate_p_value(z_score):
    """
    Calcula el p-valor basado en el Z-score.
    
    Parámetros:
    z_score (float): Valor del Z-score calculado.
    
    Retorna:
    float: p-valor asociado al Z-score.
    """
    p_value = 2 * (1 - stats.norm.cdf(abs(z_score)))
    return p_value

def calculate_contraste_hipotesis(p_value,alpha):
    """
    Calcula el contraste de hipótesis dado el p-value y nivel significancia.
    
    Parámetros:
    p_value (float)
    alpha (float): Nivel de significancia
    
    Retorna:
    string: contraste de hipòtesis.
    """
    if p_value < alpha:
        print("Rechazamos la hipótesis nula, la proporción no es 50%")
    else:
        print("No podemos rechazar la hipótesis nula, la proporción podría ser 50%")