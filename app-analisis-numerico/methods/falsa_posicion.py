import pandas as pd # type: ignore
import sympy as sp # type: ignore
from sympy import * # type: ignore
import flet as ft # type: ignore

def falsa_posicion(txt_x1, txt_xu, txt_fx, txt_cifras_sig, lbl_resultados, container_resultados, tbl_iteraciones, page):
    
    def eval_infx(xn, fx):
        return fx.subs(x, xn)
    
    def tolerancia(cifras_sig):
        Es = 0.5 * 10 ** (2 - cifras_sig)
        return Es
    
    def headers(df : pd.DataFrame) -> list:
        return [ft.DataColumn(ft.Text(header)) for header in df.columns]

#    Función para generar las filas de la DataTable
    def rows(df : pd.DataFrame) -> list:
        rows = []
        for index, row in df.iterrows():
            rows.append(ft.DataRow(cells = [ft.DataCell(ft.Text(str(row[header]))) for header in df.columns]))
        return rows
    

    x = sp.symbols('x')
    x1 = float(txt_x1.value)
    xu = float(txt_xu.value)
    cifras_sig = float(txt_cifras_sig.value)
    fx = sp.sympify(txt_fx.value)
    
    Es = tolerancia(cifras_sig)
    
    
    iteracion = 1
    aprox_anterior = 0
    aprox_actual = 0


    df = pd.DataFrame(columns=["Iteracion", "x1", "xu", "f(x1)", "f(xu)", "xr", "f(xr)", "f(x1)*f(xr)", "Condicion", "Error Aproximado"])

    print('Intervalo [', x1,',',xu,']')

    while True:
        fx1 = eval_infx(x1, fx)
        fxu = eval_infx(xu, fx)
        
        xr = xu - (fxu*(x1-xu)/(fx1-fxu))
        fxr = eval_infx(xr, fx)
        producto = fx1*fxr

        if producto < 0:
            condicon = '< 0'
        else:
            condicon = '> 0'

        Ea = abs(((xr - aprox_anterior)/xr)*100)

        df.loc[iteracion-1] = [iteracion, x1, xu, fx1, fxu, xr, fxr, producto, condicon,  Ea]
    
        if producto < 0:
            xu = xr
        elif producto > 0:
            x1 = xr
        else:
            break
        if Ea < Es:
            break
        
        aprox_anterior = xr
        iteracion += 1
        
    
    lbl_resultados.value = f"La raíz de la funcion {fx} = {xr}\nCon error de {Ea}%\nCon {iteracion} iteraciones"
    container_resultados.visible = True
    
    tbl_iteraciones.columns = headers(df)
    tbl_iteraciones.rows = rows(df)
    
    page.update()


