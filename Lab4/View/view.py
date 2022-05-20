from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import OneLineIconListItem, MDList, OneLineListItem
from kivymd.uix.tab import MDTabsBase

from Lab4.View.KV import KV


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
        self.screen.ids.account_number_of_get_account_info.text = ''
        self.screen.ids.card_number_of_get_account_info.text = ''
        self.screen.ids.pin_code_of_get_account_info.text = ''

        self.screen.ids.account_number_of_put_money_on_the_card.text = ''
        self.screen.ids.amount_of_money_of_put_money_on_the_card.text = ''
        self.screen.ids.card_number_of_put_money_on_the_card.text = ''
        self.screen.ids.pin_code_of_put_money_on_the_card.text = ''

        self.screen.ids.account_number_of_take_money_from_the_card.text = ''
        self.screen.ids.amount_of_money_of_take_money_from_the_card.text = ''
        self.screen.ids.card_number_of_take_money_from_the_card.text = ''
        self.screen.ids.pin_code_of_take_money_from_the_card.text = ''

        self.screen.ids.account_of_registration_new_credit_card.text = ''
        self.screen.ids.credit_card_number_of_registration_new_credit_card.text = ''
        self.screen.ids.pin_code_of_registration_new_credit_card.text = ''

        self.screen.ids.phone_number_of_registration_new_phone.text = ''

        self.screen.ids.phone_of_put_money_on_phone.text = ''
        self.screen.ids.account_of_put_money_on_phone.text = ''
        self.screen.ids.amount_of_money_of_put_money_on_phone.text = ''
        self.screen.ids.card_number_of_put_money_on_phone.text = ''
        self.screen.ids.pin_code_of_put_money_on_phone.text = ''

    def update_view_menu(self, info, cash, phone: bool = False):
        """Update status transaction in logs"""
        self.clear_fields()
        self.screen.ids.widget_label_logs.clear_widgets()
        self.root.ids.widget_label_logs.add_widget(OneLineListItem(text=f'Human status of transaction'))
        self.root.ids.widget_label_logs.add_widget(OneLineListItem(text=f'Cash: {cash}'))
        for key, value in info.items():
            if phone:
                self.root.ids.widget_label_logs.add_widget(
                    OneLineListItem(text=f"Account: {key} | Amount of money: {value.phone_account}"))
            else:
                self.root.ids.widget_label_logs.add_widget(
                    OneLineListItem(text=f"Account: {key} | Amount of money: {value.bank_account}"))

    def user_info(self, info):
        """Get card info"""
        self.clear_fields()
        self.screen.ids.widget_label_logs.clear_widgets()
        self.root.ids.widget_label_logs.add_widget(OneLineListItem(text=f'Client status'))
        self.root.ids.widget_label_logs.add_widget(OneLineListItem(text=f'{info}'))

    def clear_fields(self):
        """Clear all fields for updating info"""
        self.screen.ids.account_number_of_get_account_info.text = ''
        self.screen.ids.card_number_of_get_account_info.text = ''
        self.screen.ids.pin_code_of_get_account_info.text = ''

        self.screen.ids.account_number_of_put_money_on_the_card.text = ''
        self.screen.ids.amount_of_money_of_put_money_on_the_card.text = ''
        self.screen.ids.card_number_of_put_money_on_the_card.text = ''
        self.screen.ids.pin_code_of_put_money_on_the_card.text = ''

        self.screen.ids.account_number_of_take_money_from_the_card.text = ''
        self.screen.ids.amount_of_money_of_take_money_from_the_card.text = ''
        self.screen.ids.card_number_of_take_money_from_the_card.text = ''
        self.screen.ids.pin_code_of_take_money_from_the_card.text = ''

        self.screen.ids.account_of_registration_new_credit_card.text = ''
        self.screen.ids.credit_card_number_of_registration_new_credit_card.text = ''
        self.screen.ids.pin_code_of_registration_new_credit_card.text = ''

        self.screen.ids.phone_number_of_registration_new_phone.text = ''

        self.screen.ids.phone_of_put_money_on_phone.text = ''
        self.screen.ids.account_of_put_money_on_phone.text = ''
        self.screen.ids.amount_of_money_of_put_money_on_phone.text = ''
        self.screen.ids.card_number_of_put_money_on_phone.text = ''
        self.screen.ids.pin_code_of_put_money_on_phone.text = ''
