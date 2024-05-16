import pandas as pd # type: ignore
import sympy as sp # type: ignore
from sympy import * # type: ignore
import flet as ft # type: ignore

def NewtonIterativo(txt_x1, txt_fx, txt_cifras_sig, lbl_resultados, container_resultados, tbl_iteraciones, page):
    # Función para crear los Headers
    def headers(df : pd.DataFrame) -> list:
        return [ft.DataColumn(ft.Text(header)) for header in df.columns]

    # Función para generar las filas de la DataTable
    def rows(df : pd.DataFrame) -> list:
        rows = []
        for index, row in df.iterrows():
            rows.append(ft.DataRow(cells = [ft.DataCell(ft.Text(str(row[header]))) for header in df.columns]))
        return rows
    
    # Headers
    df = pd.DataFrame(columns=["Iteracion", "xi", "f(xi)", "f'(xi)", "xi+1", "Error Aproximado"])

    # Variables iniciales
    x = sp.symbols('x')
    xi = float(txt_x1.value)
    cifras_sig = int(txt_cifras_sig.value)
    fx = sp.sympify(txt_fx.value)
    Es = 0.5 * 10 ** (2 - cifras_sig)
    Ea = 0
    iteracion = 0
    
    if  cifras_sig <= 0:# Cifras significativas no válidas
        # Mostrar datos
        lbl_resultados.value = f"ERROR: Las cifras singnificativas deben ser mayores a 0"
        container_resultados.visible = True
        page.update()
        return None
    else: 
        # Bucle iteraciones
        while Ea > Es or iteracion == 0:# Condición para finalizar
            if iteracion > 50:
                print("Parada de emergencia.Se alcanzaron las 50 iteraciones.")
                break
            else:
                iteracion += 1
                # Evaluamos en las funciones
                fxi = fx.subs(x, xi)
                dxi = sp.diff(fx, x).evalf(subs={x: xi})
                # Encontramos xr
                if dxi != 0:
                    # Encontramos Xi+1 o "Xr"
                    xr = xi - (fxi / dxi )
                    if 2*xr == xi or xr == 0:
                        Ea = abs(xr - xi) * 100
                    else:
                        Ea = abs(((xr - xi) / xr) * 100)
                    # Añadimos los resultados a la lista
                    df.loc[iteracion-1] = [iteracion, xi, fxi, dxi, xr, Ea]
                    # Cambiamos valores de la siguiente iteración
                    xi = xr
                else: 
                   lbl_resultados.value = f"ERROR: La derivada de la función ingresada no es válida para este método."
                   container_resultados.visible = True
                   page.update()
                   return None
        # Mostrar datos
        lbl_resultados.value = f"La raíz de la funcion {fx} = {xr}\nCon error de {Ea}%\nCon {iteracion} iteraciones"
        container_resultados.visible = True
        tbl_iteraciones.columns = headers(df)
        tbl_iteraciones.rows = rows(df)
        page.update()