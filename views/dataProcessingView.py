from nicegui import ui

class DataProcessView:
    def __init__(self):
        # Initialize the node mapping
        self.container = ui.row().classes("m-4 bg-gray-300")

    def render(self):
        ui.label("Post Proc Screen")

    def start(self):
        """Start the UI."""
        self.render()

ui.run()