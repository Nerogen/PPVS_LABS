from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList, OneLineListItem
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.app import MDApp
from Lab2.View.ui import KV


class Tab(MDFloatLayout, MDTabsBase):
    pass


class ContentNavigationDrawer(BoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class View(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)

    def on_start(self):
        self.screen.ids.name.text = ''
        self.screen.ids.account_number.text = ''
        self.screen.ids.address.text = ''
        self.screen.ids.mobile_phone.text = ''
        self.screen.ids.home_phone.text = ''

        self.screen.ids.name_for_search.text = ''
        self.screen.ids.account_number_for_search.text = ''
        self.screen.ids.address_for_search.text = ''
        self.screen.ids.mobile_phone_for_search.text = ''
        self.screen.ids.home_phone_for_search.text = ''

        self.screen.ids.name_for_delete.text = ''
        self.screen.ids.account_number_for_delete.text = ''
        self.screen.ids.address_for_delete.text = ''
        self.screen.ids.mobile_phone_for_delete.text = ''
        self.screen.ids.home_phone_for_delete.text = ''

    def update_view_menu(self):
        """Update user form and make list logs"""
        self.clear_fields()
        self.screen.ids.widget_label.clear_widgets()
        self.screen.ids.widget_label_view.clear_widgets()

        for i in self.user_base:
            self.root.ids.widget_label.add_widget(
                OneLineListItem(text=f'Name: {i[0]}  '
                                     f'Account number: {i[1]} '
                                     f'Address: {i[2]} '
                                     f'Mobile phone: {i[3]} '
                                     f'Home phone: {i[4]}')
            )

        for i in self.logger:
            self.root.ids.widget_label_view.add_widget(
                OneLineListItem(text=f"{i}")
            )

    def clear_fields(self):
        """Clear all fields for updating info"""
        self.screen.ids.name.text = ''
        self.screen.ids.account_number.text = ''
        self.screen.ids.address.text = ''
        self.screen.ids.mobile_phone.text = ''
        self.screen.ids.home_phone.text = ''

        self.screen.ids.name_for_search.text = ''
        self.screen.ids.account_number_for_search.text = ''
        self.screen.ids.address_for_search.text = ''
        self.screen.ids.mobile_phone_for_search.text = ''
        self.screen.ids.home_phone_for_search.text = ''

        self.screen.ids.name_for_delete.text = ''
        self.screen.ids.account_number_for_delete.text = ''
        self.screen.ids.address_for_delete.text = ''
        self.screen.ids.mobile_phone_for_delete.text = ''
        self.screen.ids.home_phone_for_delete.text = ''

    def theme(self):
        if self.theme_cls.theme_style is 'Light':
            self.theme_cls.theme_style = 'Dark'
        else:
            self.theme_cls.theme_style = 'Light'

