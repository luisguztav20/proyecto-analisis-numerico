import flet as ft



def main(page: ft.Page):
    page.title = "Routes Example"


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
    def route_change(e):
        page.views.clear()
        page.views.append(
            ft.View(
                route="/",
                controls=[
                    ft.AppBar(title=ft.Text("Proyecto Analisis Numerico"), bgcolor=ft.colors.SURFACE_VARIANT,),
                    listview
                ],
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        if page.route == "/unidad_uno":
            page.views.append(
                ft.View(
                    route="/unidad_uno",
                    controls=
                    [
                        ft.AppBar(title=ft.Text("Unidad 1"), bgcolor=ft.colors.SURFACE_VARIANT),
                        
                        
                        
                    ],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        elif page.route == "/unidad_dos":
            page.views.append(
                ft.View(
                    route="/unidad_dos",
                    controls=
                    [
                        ft.AppBar(title=ft.Text("Unidad 2"), bgcolor=ft.colors.SURFACE_VARIANT),
                       
                    ],
                )
            )
        elif page.route == "/unidad_tres":
            page.views.append(
                ft.View(
                    route="/unidad_tres",
                    controls=
                    [
                        ft.AppBar(title=ft.Text("Unidad 3"), bgcolor=ft.colors.SURFACE_VARIANT),
                       
                    ],
                )
            )
        elif page.route == "/unidad_cuatro":
            page.views.append(
                ft.View(
                    route="/unidad_cuatro",
                    controls=
                    [
                        ft.AppBar(title=ft.Text("Unidad 4"), bgcolor=ft.colors.SURFACE_VARIANT),
                       
                    ],
                )
            )
        elif page.route == "/unidad_cinco":
            page.views.append(
                ft.View(
                    route="/unidad_cinco",
                    controls=
                    [
                        ft.AppBar(title=ft.Text("Unidad 5"), bgcolor=ft.colors.SURFACE_VARIANT),
                        #ft.ElevatedButton("Regresar", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        page.update()

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route)


ft.app(main)