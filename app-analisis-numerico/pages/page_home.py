import flet as ft 
from flet import Page as page

def container_controls_home(page):
    container_controls = ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.ResponsiveRow(
                        [
                            ft.Container(
                                ft.Text('Unidad 1'),
                                    bgcolor='#565656',  #ft.colors.BLUE_100,
                                    border_radius=ft.border_radius.all(15),
                                    padding=50,
                                    margin=20,
                                    alignment=ft.alignment.center,
                                    ink=True,
                                    on_click=lambda _: page.go("/unidad_uno"),
                                    col={"sm": 6, "md": 6, "xl": 4}, #la fila se divide en 12 
                                ),
                                ft.Container(
                                    ft.Text('Unidad 2'),
                                    bgcolor='#565656',  #ft.colors.BLUE_100,
                                    border_radius=ft.border_radius.all(15),
                                    padding=50,
                                    margin=20,
                                    alignment=ft.alignment.center,
                                    ink=True,
                                    on_click=lambda _: page.go("/unidad_dos"),
                                    col={"sm": 6, "md": 6, "xl": 4}, #la fila se divide en 12 
                                ),
                                ft.Container(
                                    ft.Text('Unidad 3'),
                                    bgcolor='#565656',  #ft.colors.BLUE_100,
                                    border_radius=ft.border_radius.all(15),
                                    padding=50,
                                    margin=20,
                                    alignment=ft.alignment.center,
                                    ink=True,
                                    on_click=lambda _: page.go("/unidad_tres"),
                                    col={"sm": 6, "md": 6, "xl": 4}, #la fila se divide en 12 
                                ),
                                ft.Container(
                                    ft.Text('Unidad 4'),
                                    bgcolor='#565656',  #ft.colors.BLUE_100,
                                    border_radius=ft.border_radius.all(15),
                                    padding=50,
                                    margin=20,
                                    alignment=ft.alignment.center,
                                    ink=True,
                                    on_click=lambda _: page.go("/unidad_cuatro"),
                                    col={"sm": 6, "md": 6, "xl": 6}, #la fila se divide en 12 
                                ),
                                ft.Container(
                                    ft.Text('Unidad 5'),
                                    bgcolor='#565656',  #ft.colors.BLUE_100,
                                    border_radius=ft.border_radius.all(15),
                                    padding=50,
                                    margin=20,
                                    alignment=ft.alignment.center,
                                    ink=True,
                                    on_click=lambda _: page.go("/unidad_cinco"),
                                    col={"sm": 6, "md": 6, "xl": 6}, #la fila se divide en 12 
                                ),
                                
                            ]
                        )
                        
                    )
    listview = ft.ListView(expand=True, auto_scroll=True )
    listview.controls.append(container_controls)
    
    return listview
