from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList, OneLineListItem
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout

KV = '''

#:import md_icons kivymd.icon_definitions.md_icons
#:import fonts kivymd.font_definitions.fonts

# Menu item in the DrawerList list.
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color


<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "data/logo/kivy-icon-256.png"

    MDLabel:
        text: "Client base app"
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    MDLabel:
        text: "author Nero"
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]

    ScrollView:

        DrawerList:
            id: md_list



Screen:

    MDNavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "Client base"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                        md_bg_color: 0,0,0,1

                    MDTabs:
                        id: tabs
                        height: "48dp"
                        tab_indicator_anim: False
                        background_color: 0.1,0.1,0.1,1
                        
                        Tab:
                            id: tab1
                            name: 'tab 1'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['table-large']}[/size][/font] Table"
                            ScrollView:
                                MDList:
                                    id: widget_label
                                
                                
                        Tab:
                            id: tab2
                            name: 'tab 2'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['clock-time-eight-outline']}[/size][/font] View logs"
                            ScrollView:
                                MDList:
                                    id: widget_label_view
                            
                            
                        Tab:
                            id: tab3
                            name: "tab 3"
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['account-arrow-up']}[/size][/font] Create user"
                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"

                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "account"

                                    MDTextField:
                                        id: name
                                        hint_text: 'Name'
                                        
                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "numeric"

                                    MDTextField:
                                        id: account_number
                                        hint_text: 'Account number'
                                        
                                        
                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "badge-account-horizontal-outline"

                                    MDTextField:
                                        id: address
                                        hint_text: 'Address'
                                        
                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "cellphone"

                                    MDTextField:
                                        id: mobile_phone
                                        hint_text: 'Mobile phone'
                                        
                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "phone"

                                    MDTextField:
                                        id: home_phone
                                        hint_text: 'Home phone'
                                        
                                BoxLayout:
                                    MDRectangleFlatButton:
                                        text: "Confirm new user and save info"
                                        theme_text_color: "Custom"
                                        text_color: 1, 0, 0, 1
                                        line_color: 0, 0, 1, 1
                                        on_release: app.update_user_base()
                                        
                                    MDRectangleFlatButton:
                                        text: "Back and clear all info fields"
                                        theme_text_color: "Custom"
                                        text_color: 1, 0, 0, 1
                                        line_color: 0, 0, 1, 1
                            
                        Tab:
                            id: tab4
                            name: "tab 4"
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['account-search']}[/size][/font] Search user"
                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"

                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "account"

                                    MDTextField:
                                        id: name_for_search
                                        hint_text: 'Name'
                                        
                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "numeric"

                                    MDTextField:
                                        id: account_number_for_search
                                        hint_text: 'Account number'
                                        
                                        
                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "badge-account-horizontal-outline"

                                    MDTextField:
                                        id: address_for_search
                                        hint_text: 'Address'
                                        
                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "cellphone"

                                    MDTextField:
                                        id: mobile_phone_for_search
                                        hint_text: 'Mobile phone'
                                        
                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "phone"

                                    MDTextField:
                                        id: home_phone_for_search
                                        hint_text: 'Home phone'
                                        
                                BoxLayout:
                                    MDRectangleFlatButton:
                                        text: "Search user in base"
                                        theme_text_color: "Custom"
                                        text_color: 1, 0, 0, 1
                                        line_color: 0, 0, 1, 1
                                        on_release: app.search_user_info()
                                        
                                    MDRectangleFlatButton:
                                        text: "Back and clear all info fields"
                                        theme_text_color: "Custom"
                                        text_color: 1, 0, 0, 1
                                        line_color: 0, 0, 1, 1
                        
                        Tab:
                            id: tab5
                            name: "tab 5"
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['delete']}[/size][/font] Delete user"
                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"

                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "account"

                                    MDTextField:
                                        id: name_for_delete
                                        hint_text: 'Name'
                                        
                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "numeric"

                                    MDTextField:
                                        id: account_number_for_delete
                                        hint_text: 'Account number'
                                        
                                        
                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "badge-account-horizontal-outline"

                                    MDTextField:
                                        id: address_for_delete
                                        hint_text: 'Address'
                                        
                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "cellphone"

                                    MDTextField:
                                        id: mobile_phone_for_delete
                                        hint_text: 'Mobile phone'
                                        
                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "phone"

                                    MDTextField:
                                        id: home_phone_for_delete
                                        hint_text: 'Home phone'
                                        
                                BoxLayout:
                                    MDRectangleFlatButton:
                                        text: "Confirm new user and save info"
                                        theme_text_color: "Custom"
                                        text_color: 1, 0, 0, 1
                                        line_color: 0, 0, 1, 1
                                        on_release: app.delete_user_info()
                                        
                                    MDRectangleFlatButton:
                                        text: "Back and clear all info fields"
                                        theme_text_color: "Custom"
                                        text_color: 1, 0, 0, 1
                                        line_color: 0, 0, 1, 1
                        
        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer
'''


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


class ClientBaseApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        self.user_base = []
        self.logger = []

    def build(self):
        return self.screen

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

        icons_bar = {
            "upload": "Upload data",
            "shield-sun": "Dark/Light"
        }

        for icon_name in icons_bar.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_bar[icon_name])
            )

    def update_user_base(self):
        """Get all info from fields and update two - dimensional list, update label info"""
        box = [
            self.screen.ids.name.text[:],
            self.screen.ids.account_number.text[:],
            self.screen.ids.address.text[:],
            self.screen.ids.mobile_phone.text[:],
            self.screen.ids.home_phone.text[:]
        ]

        self.user_base.append(box)
        self.logger.append(f'Add user {box[0]} successful!')
        self.change_label_after_add()
        self.update_view_menu()

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

    def search_user_info(self, search=True):
        """Search info from box with all fields, return place of user in data base"""
        if search:
            box = [
                self.screen.ids.name_for_search.text[:],
                self.screen.ids.account_number_for_search.text[:],
                self.screen.ids.address_for_search.text[:],
                self.screen.ids.mobile_phone_for_search.text[:],
                self.screen.ids.home_phone_for_search.text[:]
            ]

        else:
            box = [
                self.screen.ids.name_for_delete.text[:],
                self.screen.ids.account_number_for_delete.text[:],
                self.screen.ids.address_for_delete.text[:],
                self.screen.ids.mobile_phone_for_delete.text[:],
                self.screen.ids.home_phone_for_delete.text[:]
            ]

        for i in range(len(self.user_base)):
            for j in box:
                if j in self.user_base[i]:
                    self.logger.append(f'User {box[0]} find!')
                    self.update_view_menu()
                    return i
        else:
            self.logger.append(f'User {box[0]} not found!')
            self.update_view_menu()

    def delete_user_info(self):
        """Use function for get place of user and then delete from data base"""
        place = self.search_user_info(False)
        if place is None:
            self.update_view_menu()
        else:
            del self.user_base[place]
            self.logger[-1] = self.logger[-1] + ' And was delete!'
            self.update_view_menu()

    def change_label_after_add(self):
        self.clear_fields()
        self.screen.ids.widget_label.clear_widgets()
        self.screen.ids.widget_label_view.clear_widgets()

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


if __name__ == '__main__':
    ClientBaseApp().run()
