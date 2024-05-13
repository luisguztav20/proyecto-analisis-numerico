import flet as ft
from pages.page_unidad_uno import view_unidad_uno
from pages.page_home import container_controls_home


def main(page: ft.Page):
    page.title = "Proyecto analisis numerico"

    listview = container_controls_home(page)
    
    
    def route_change(e):
        page.views.clear()
        page.views.append(
            ft.View(
                route="/",
                controls=[
                    ft.AppBar(title=ft.Text("Proyecto Analisis Numerico"), bgcolor=ft.colors.BLUE_600, center_title=True,),
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
                        view_unidad_uno(page)
                        
                        
                    ],
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


ft.app(main, )