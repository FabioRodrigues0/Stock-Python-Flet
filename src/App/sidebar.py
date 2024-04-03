import flet as ft
from flet import (UserControl, Column, Container, Row, Text, NavigationRail, NavigationRailDestination, alignment,
                  border_radius, colors, icons, padding, margin, TextAlign)


class Sidebar(UserControl):
    def __init__(self, app_layout, page):
        super().__init__()
        self.app_layout = app_layout
        self.page = page
        self.top_nav_items = [
            NavigationRailDestination(
                label_content=Text("Stock"),
                label="Stock",
                icon=icons.BOOK_OUTLINED,
                selected_icon=icons.BOOK_OUTLINED
            ),
            NavigationRailDestination(
                label_content=Text("Suppliers"),
                label="Suppliers",
                icon=icons.PERSON_2,
                selected_icon=icons.PERSON_2
            ),
            NavigationRailDestination(
                label_content=Text("Users"),
                label="Users",
                icon=icons.PERSON,
                selected_icon=icons.PERSON
            ),

        ]
        self.top_nav_rail = NavigationRail(
            selected_index=None,
            label_type=ft.NavigationRailLabelType.ALL,
            on_change=self.top_nav_change,
            destinations=self.top_nav_items,
            bgcolor=colors.LIGHT_BLUE_ACCENT_700,
            extended=True,
            expand=True,
        )

    def build(self):
        self.view = Container(
            content=Column([
                Row([
                    Text("Menu", text_align=TextAlign.CENTER)
                ]),
                # divider
                Container(
                    bgcolor=colors.BLACK26,
                    border_radius=border_radius.all(30),
                    height=1,
                    alignment=alignment.center_right,
                    width=150
                ),
                self.top_nav_rail,
                # divider
                Container(
                    bgcolor=colors.BLACK26,
                    border_radius=border_radius.all(30),
                    height=1,
                    alignment=alignment.center_right,
                    width=150,
                ),
            ], tight=True),
            padding=padding.all(10),
            margin=margin.all(0),
            width=170,
            expand=True,
            bgcolor=colors.LIGHT_BLUE_ACCENT_700,
        )
        return self.view

    def top_nav_change(self, e):
        self.top_nav_rail.selected_index = e.control.selected_index
        self.update()
