import pandas as pd # type: ignore
import sympy as sp # type: ignore
from sympy import * # type: ignore
import flet as ft # type: ignore

def NewtonIterativo(txt_x1, txt_fx, txt_cifras_sig, lbl_resultados, container_resultados, tbl_iteraciones, page):
    # Función para obetener Es (nivel de tolerancia)
    def tolerancia(cifras_sig):
        Es = 0.5 * 10 ** (2 - cifras_sig)
        return Es
    
    # Función para crear los Headers
    def headers(df : pd.DataFrame) -> list:
        return [ft.DataColumn(ft.Text(header)) for header in df.columns]

    # Función para generar las filas de la DataTable
    def rows(df : pd.DataFrame) -> list:
        rows = []
        for index, row in df.iterrows():
            rows.append(ft.DataRow(cells = [ft.DataCell(ft.Text(str(row[header]))) for header in df.columns]))
        return rows
    
    # Variables iniciales
    x = sp.symbols('x')
    xi = float(txt_x1.value)
    cifras_sig = float(txt_cifras_sig.value)
    fx = sp.sympify(txt_fx.value)
    Es = tolerancia(cifras_sig)
    Ea = 100
    iteracion = 0
    
     # Headers
    df = pd.DataFrame(columns=["Iteracion", "xi", "f(xi)", "f'(xi)", "xi+1", "Error Aproximado"])

    # Bucle iteraciones
    while Ea > Es:# Condición para finalizar
        if iteracion > 50:
            print("Parada de emergencia.Se alcanzaron las 50 iteraciones.")
            break
        else:
            iteracion += 1
            # Evaluamos en las funciones
            fx_Evaluada = fx.subs(x, xi)
            fx_Derivada = sp.diff(fx, x).evalf(subs={x: xi})
            # Encontramos xr
            if fx_Derivada != 0:
                # Encontramos Xi+1 o "Xr"
                xi_más_uno = xi - (fx_Evaluada / fx_Derivada )
                Ea = abs(((xi_más_uno - xi) / xi_más_uno) * 100)
                # Añadimos los resultados a la lista
                df.loc[iteracion-1] = [iteracion, xi, fx_Evaluada, fx_Derivada, xi_más_uno, Ea]
                # Cambiamos valores de la siguiente iteración
                xi = xi_más_uno
            else: 
                print("Error: La derivada de la función ingresada no es válida para este método.")
                print("ZeroDivisionError.")
    # Mostrar datos
    lbl_resultados.value = f"La riz de la funcion {fx} = {xi_más_uno}\nCon error de {Ea}%\nCon {iteracion} iteraciones"
    container_resultados.visible = True
    
    tbl_iteraciones.columns = headers(df)
    tbl_iteraciones.rows = rows(df)
    
    page.update()