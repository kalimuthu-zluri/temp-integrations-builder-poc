from nicegui import ui

class VariableOptionsView:
    def __init__(self):
        # Initialize the node mapping
        self.container = ui.row().classes("m-4 bg-gray-300")

    def render(self):
        ui.label("Variable Options Screen")
        print()

    def start(self):
        """Start the UI."""
        self.render()

ui.run()