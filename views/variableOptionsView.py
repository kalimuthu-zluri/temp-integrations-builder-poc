from nicegui import ui
from typing import Dict, List

class VariableOptionsView:
    def __init__(self):
        # Initialize the node mapping
        self.container = ui.row().classes("m-4 bg-gray-300")

        self.TABS = {
        "Formfields": ['client_id', 'client_secret'],
        "Parent Context": ['id', 'email'], 
        "Pagination Variables": ['page', 'limit'], 
        "Additional Variables": ['path', 'dataFetchStartDate', 'dataFetchEndDate', 'response']
    }

    def create_dynamic_tabs(cls):
        """
        Create tabs dynamically based on the TABS class dictionary
        """
        # Create tabs
        with ui.tabs() as tabs:
            # Dynamically create tab headers
            tab_headers = {name: ui.tab(name) for name in cls.TABS.keys()}

        # Create tab panels
        with ui.tab_panels(tabs, value=list(tab_headers.values())[0]):
            # Iterate through tabs dynamically
            for tab_name, buttons in cls.TABS.items():
                with ui.tab_panel(tab_headers[tab_name]):
                    ui.label(f"{tab_name} Tab").classes('text-h6')
                    
                    # Create a column of buttons for each tab
                    with ui.column():
                        for button_name in buttons:
                            ui.button(
                                button_name, 
                                on_click=lambda name=button_name: cls.on_button_click(name)
                            )

    @staticmethod
    def on_button_click(button_name: str):
        """
        Generic button click handler
        """
        ui.notify(f"{button_name} button clicked")
        ui.clipboard.write( '{{'  + button_name + '}}')


    def render(self):
        ui.label("Variable Options Screen")
        self.create_dynamic_tabs()

    def start(self):
        """Start the UI."""
        self.render()

ui.run()