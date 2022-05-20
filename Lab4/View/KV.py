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

        MDList:
            id: md_list
            OneLineIconListItem:
                text: "Upload data base"
                on_release: app.read_from_file()
                IconLeftWidget:
                    icon: "upload"
                    
            


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
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['clock-time-eight-outline']}[/size][/font] View logs"
                            ScrollView:
                                MDList:
                                    id: widget_label_logs
                                    
                        Tab:
                            id: tab2
                            name: "tab 2"
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['account-cog']}[/size][/font] Get account info"
                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"

                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "account"

                                    MDTextField:
                                        id: account_number_of_get_account_info
                                        hint_text: 'Account number'

                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "badge-account-horizontal-outline"

                                    MDTextField:
                                        id: card_number_of_get_account_info
                                        hint_text: 'Card number'


                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "numeric"

                                    MDTextField:
                                        id: pin_code_of_get_account_info
                                        hint_text: 'Pin code'

                                BoxLayout:
                                
                                    MDRectangleFlatButton:
                                        text: "Confirm operation"
                                        theme_text_color: "Custom"
                                        text_color: 1, 0, 1, 1
                                        line_color: 0, 0, 1, 1
                                        on_release: app.get_info()

                                    MDRectangleFlatButton:
                                        text: "Back and clear all info fields"
                                        theme_text_color: "Custom"
                                        text_color: 1, 0, 1, 1
                                        line_color: 0, 0, 1, 1
                                        on_release: app.clear_fields()
                        Tab:
                            id: tab3
                            name: "tab 3"
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['account-arrow-up']}[/size][/font] Put money on the card"
                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"

                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "account"

                                    MDTextField:
                                        id: account_number_of_put_money_on_the_card
                                        hint_text: 'Account number'

                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "account-cash"

                                    MDTextField:
                                        id: amount_of_money_of_put_money_on_the_card
                                        hint_text: 'Amount of money'


                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "badge-account-horizontal-outline"

                                    MDTextField:
                                        id: card_number_of_put_money_on_the_card
                                        hint_text: 'Card number'

                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "numeric"

                                    MDTextField:
                                        id: pin_code_of_put_money_on_the_card
                                        hint_text: 'Pin code'

                                BoxLayout:
                                
                                    MDRectangleFlatButton:
                                        text: "Confirm operation"
                                        theme_text_color: "Custom"
                                        text_color: 1, 0, 1, 1
                                        line_color: 0, 0, 1, 1
                                        on_release: app.put_money()

                                    MDRectangleFlatButton:
                                        text: "Back and clear all info fields"
                                        theme_text_color: "Custom"
                                        text_color: 1, 0, 1, 1
                                        line_color: 0, 0, 1, 1
                                        on_release: app.clear_fields()

                        Tab:
                            id: tab4
                            name: "tab 4"
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['account-arrow-down']}[/size][/font] Take money from the card"
                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"

                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "account"

                                    MDTextField:
                                        id: account_number_of_take_money_from_the_card
                                        hint_text: 'Account number'

                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "account-cash"

                                    MDTextField:
                                        id: amount_of_money_of_take_money_from_the_card
                                        hint_text: 'Amount of money'


                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "badge-account-horizontal-outline"

                                    MDTextField:
                                        id: card_number_of_take_money_from_the_card
                                        hint_text: 'Card number'

                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "numeric"

                                    MDTextField:
                                        id: pin_code_of_take_money_from_the_card
                                        hint_text: 'Pin code'

                                BoxLayout:
                                
                                    MDRectangleFlatButton:
                                        text: "Confirm operation"
                                        theme_text_color: "Custom"
                                        text_color: 1, 0, 1, 1
                                        line_color: 0, 0, 1, 1
                                        on_release: app.take_money()

                                    MDRectangleFlatButton:
                                        text: "Back and clear all info fields"
                                        theme_text_color: "Custom"
                                        text_color: 1, 0, 1, 1
                                        line_color: 0, 0, 1, 1
                                        on_release: app.clear_fields()
                                        
                        Tab:
                            id: tab5
                            name: "tab 5"
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['account-multiple-plus']}[/size][/font] Registration new credit card"
                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"
                                
                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "account"

                                    MDTextField:
                                        id: account_of_registration_new_credit_card
                                        hint_text: 'Account'

                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "account"

                                    MDTextField:
                                        id: credit_card_number_of_registration_new_credit_card
                                        hint_text: 'Credit card number'
                                        
                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "account"

                                    MDTextField:
                                        id: pin_code_of_registration_new_credit_card
                                        hint_text: 'Pin code'


                                BoxLayout:
                                    MDRectangleFlatButton:
                                        text: "Confirm operation"
                                        theme_text_color: "Custom"
                                        text_color: 1, 0, 1, 1
                                        line_color: 0, 0, 1, 1
                                        on_release: app.registration_new_account()

                                    MDRectangleFlatButton:
                                        text: "Back and clear all info field"
                                        theme_text_color: "Custom"
                                        text_color: 1, 0, 1, 1
                                        line_color: 0, 0, 1, 1
                                        on_release: app.clear_fields()
                        
                        Tab:
                            id: tab6
                            name: "tab 6"
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['account-multiple-plus']}[/size][/font] Registration new phone"
                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"

                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "account"

                                    MDTextField:
                                        id: phone_number_of_registration_new_phone
                                        hint_text: 'Phone number'
                                        
                                BoxLayout:
                                    MDRectangleFlatButton:
                                        text: "Confirm operation"
                                        theme_text_color: "Custom"
                                        text_color: 1, 0, 1, 1
                                        line_color: 0, 0, 1, 1
                                        on_release: app.registration_new_phone()
    
                                    MDRectangleFlatButton:
                                        text: "Back and clear all info fields"
                                        theme_text_color: "Custom"
                                        text_color: 1, 0, 1, 1
                                        line_color: 0, 0, 1, 1
                                        on_release: app.clear_fields()
                        
                        Tab:
                            id: tab7
                            name: "tab 7"
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['alpha-p-box']}[/size][/font] Put money on phone"
                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"

                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "phone"

                                    MDTextField:
                                        id: phone_of_put_money_on_phone
                                        hint_text: 'Phone'

                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "account"

                                    MDTextField:
                                        id: account_of_put_money_on_phone
                                        hint_text: 'Account number'


                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "account-cash"

                                    MDTextField:
                                        id: amount_of_money_of_put_money_on_phone
                                        hint_text: 'Amount of money'

                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "badge-account-horizontal-outline"

                                    MDTextField:
                                        id: card_number_of_put_money_on_phone
                                        hint_text: 'Card number'
                                        

                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "numeric"

                                    MDTextField:
                                        id: pin_code_of_put_money_on_phone
                                        hint_text: 'Pin code'

                                BoxLayout:
                                    MDRectangleFlatButton:
                                        text: "Confirm operation"
                                        theme_text_color: "Custom"
                                        text_color: 1, 0, 1, 1
                                        line_color: 0, 0, 1, 1
                                        on_release: app.put_on_phone()

                                    MDRectangleFlatButton:
                                        text: "Back and clear all info fields"
                                        theme_text_color: "Custom"
                                        text_color: 1, 0, 1, 1
                                        line_color: 0, 0, 1, 1
                                        on_release: app.clear_fields()         
                            
        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer
'''