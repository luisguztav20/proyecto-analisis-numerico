import flet as ft
import sympy as sp
from methods.biseccion import biseccion
from methods.graficador import graficar
from methods.falsa_posicion import falsa_posicion

def view_unidad_uno(page):
    
    def calcular(event):
        state_x1 = txt_x1.value
        state_xu = txt_xu.value
        state_fx = txt_fx.value
        state_cifras = txt_cifras_sig.value
        try:
            selection_method = int(select_methods.value)
        except:
            show_alert(event)
  
            
        if selection_method == 1 :
            print('BISECCION')
            if state_x1 == '' or state_xu == '' or state_cifras == '' or state_fx == '':
                print('VACIO')
                show_alert(event)
            else:
                biseccion(txt_x1, txt_xu, txt_fx, txt_cifras_sig, lbl_resultados, container_resultados, tbl_iteraciones, page)
                fx = sp.sympify(txt_fx.value)
                graficar(fx, page)
                
        elif selection_method == 2:
            print('FALSA POSICION')
            if state_x1 == '' or state_xu == '' or state_cifras == '' or state_fx == '':
                print('VACIO')
                show_alert(event)
            else:
                falsa_posicion(txt_x1, txt_xu, txt_fx, txt_cifras_sig, lbl_resultados, container_resultados, tbl_iteraciones, page)
                fx = sp.sympify(txt_fx.value)
                graficar(fx, page)
            
            
        elif selection_method == 3:
            print('PUNTO FIJO')
        elif selection_method == 4:
            print('SECANTE')
        elif selection_method == 5:
            print('NEWTON RAPHSON')           
        elif selection_method == 6:
            print('NEWTON RAPHSON MODIFICADO')
        
    def grafica(event):
        
        state_x1 = txt_x1.value
        state_xu = txt_xu.value
        state_fx = txt_fx.value
        state_cifras = txt_cifras_sig.value
        
        if state_x1 == '' and state_xu == '' and state_cifras == '' and state_fx == '':
            show_alert(event)
        else:
            fx = sp.sympify(txt_fx.value)
            graficar(fx, page)
            # ft.app.run(lambda: graficar(fx, page))
            
    def update_inputs(event): # Activa o desactiva los inputs para los diferentes metodos 
        selection_method = int(select_methods.value)
          
        if selection_method == 1:
            txt_x1.label = 'Ingrese el valor de x1'
            txt_xu.disabled=False
            page.update()
              
              
        elif selection_method == 2:
            txt_x1.label = 'Ingrese el valor de x1'
            txt_xu.disabled = False
            page.update()
            
        elif selection_method == 3:
            txt_x1.label = 'Ingrese el valor de x0'
            txt_xu.disable = True
            page.update()
            
        elif selection_method == 4:
            txt_xu.disabled=True
            txt_x1.label = 'Ingrese el valor de x-1'
            txt_xu.label = 'Ingrese el valor de x0'
            page.update()
            
        elif selection_method == 5:
            txt_x1.label = 'Ingrese el valor de x0'
            txt_xu.disabled=True
            page.update()
            
        elif selection_method == 6:
            txt_x1.label = 'Ingrese el valor de x0'
            txt_xu.disabled=True
            page.update()
                                 
    def close_alert(event):
        event.control.page.banner.open = False
        page.update()
       
    def show_alert(event):
        event.control.page.banner = banner
        event.control.page.banner.open = True
        page.update()
        
    def limpiar (event):
        txt_x1.value = ''
        txt_xu.value =''
        txt_fx.value = ''
        txt_cifras_sig.value = ''
        txt_x1.autofocus=True
        container_resultados.visible=False
        container_tbl.visible=False
        page.update()        
    
    txt_x1 = ft.TextField(label='Ingrese el valor de x1', )
    txt_xu = ft.TextField(label='Ingrese el valor de xu')
    txt_cifras_sig = ft.TextField(label='Cifras')
    txt_fx = ft.TextField(label='Ingrese funcion')
    btn_calcular = ft.ElevatedButton(text='Calcular', on_click=calcular, height=45)
    lbl_resultados = ft.Text()
    btn_limpiar = ft.ElevatedButton(text='Limpiar', on_click=limpiar, height=45)
    btn_graficar = ft.ElevatedButton(text='Graficar', on_click=grafica, height=45)
    
    tbl_iteraciones = ft.DataTable()
    
    container_tbl = ft.Row(
            [
                ft.Container(
                    #width=500,
                    #bgcolor='#565656',  #ft.colors.BLUE_100,
                    border_radius=ft.border_radius.all(20),
                    padding=20,
                    content=ft.Row(
                        [
                        tbl_iteraciones
                        ]
                        
                    ),
                )   
            ], 
            scroll=ft.ScrollMode.ALWAYS #Permite el scroll
        
    )
    
    container_resultados = ft.Container(
                    visible=False,
                    bgcolor='#565656',  #ft.colors.BLUE_100,
                    border_radius=ft.border_radius.all(20),
                    padding=20,
                    content=ft.ResponsiveRow(
                        [
                        ft.Container(
                            lbl_resultados,
                            col={"sm": 6, "md": 4, "xl": 12},
                        ),
                    ]
                )
            
    )
    
    select_methods = ft.Dropdown(
        label='Seleccione un metodo',
        on_change =  update_inputs,
        height=60,
        options=[
            ft.dropdown.Option(text='Bisecciòn', key=1),
            ft.dropdown.Option(text='Falsa Posiciòn', key=2),
            ft.dropdown.Option(text='Punto Fijo', key=3),
            ft.dropdown.Option(text='Secante', key=4),
            ft.dropdown.Option(text='Newton Raphson', key=5),
            ft.dropdown.Option(text='Newton modificado', key=6)
        ]
    )

    container_input = ft.Container(
            bgcolor='#565656',  #ft.colors.BLUE_100,
            border_radius=ft.border_radius.all(20),
            padding=20,
            content=ft.ResponsiveRow(
                [   
                    ft.Container(
                        select_methods,
                        col={"sm": 6, "md": 6, "xl": 3}, #la fila se divide en 12 
                    ),
                    ft.Container(
                        txt_x1,
                        col={"sm": 6, "md": 6, "xl": 2}, #la fila se divide en 12 
                    ),
                    ft.Container(
                        txt_xu,
                        col={"sm": 6, "md": 6, "xl": 2},
                    ),
                    ft.Container(
                        txt_cifras_sig,
                        col={"sm": 6, "md": 6, "xl": 2},
                    ),
                    ft.Container(
                        txt_fx,
                        col={"sm": 6, "md": 6, "xl": 3},
                    ),
                    ft.Container(
                        btn_calcular,
                        btn_limpiar,
                        col={"sm": 2, "md": 2, "xl": 2},
                    ),
                    ft.Container(
                        btn_limpiar,
                        col={"sm": 2, "md": 2, "xl": 2},
                    ),
                    ft.Container(
                        btn_graficar,
                        col={"sm": 2, "md": 2, "xl": 2},
                    ),
                ], alignment=ft.MainAxisAlignment.CENTER,   
            )
        
    )
    
    banner = ft.Banner(
        bgcolor='#565656',
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
        content=ft.Text(
            "Por favor ingrese valores para calcular"
        ),
        actions=[
            ft.TextButton("Ok", on_click=close_alert),
            
        ],
    )
    
    view_controls = ft.ResponsiveRow(
            controls=[
                container_input,
                container_resultados,
                container_tbl,
            ]
    )

    
    listview = ft.ListView(expand=1, auto_scroll=True )
    listview.controls.append(view_controls)

    return( listview )

