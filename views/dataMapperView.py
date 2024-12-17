from nicegui import ui


class DataMapperView:
    def __init__(self):
        # Initialize the node mapping
        self.container = ui.row().classes("m-4 bg-gray-300")

    def render(self):
        ui.label("Data Mapper Screen")
        with ui.row():
            json = {
                "array": [1, 2, 3],
                "boolean": True,
                "color": "#82b92c",
                None: None,
                "number": 123,
                "object": {
                    "a": "b",
                    "c": "d",
                    "d": {
                        "name": "kali"
                    }
                },
                "time": 1575599819000,
                "string": "Hello World",
            }
            ui.json_editor(
                {"content": {"json": json}},
                on_select=lambda e: ui.notify(f"Select: {e}"),
                on_change=lambda e: ui.notify(f"Change: {e}"),
            )
            with ui.column().classes("space-y-2"):
                ui.tree(
                    self.parse_dict_to_hierarchical(json),
                    label_key="id",
                    tick_strategy="leaf",
                    on_tick=lambda e: ui.notify(e),
                )

    def update_locator(self, locator_input):
        ui.notify(locator_input)

    def parse_dict_to_hierarchical(self, input_dict):
        """
        Convert a flat dictionary to a hierarchical structure with 'id' and 'children'
        
        :param input_dict: Input dictionary to parse
        :return: List of hierarchical structures
        """
        def create_node(key, value):
            """
            Create a node with 'id' and optionally 'children'
            
            :param key: Key of the dictionary
            :param value: Value of the dictionary
            :return: Node dictionary
            """
            # Handle None key by converting to string
            node = {"id": str(key) if key is not None else "None"}
            
            # Check if value is a complex type that can have children
            if isinstance(value, dict):
                # Recursively create children from dictionary
                node['children'] = [
                    create_node(k, v) for k, v in value.items()
                ]
            elif isinstance(value, list):
                # Handle list of values
                node['children'] = [
                    {"id": str(item) if item is not None else "None"} 
                    for item in value
                ]
            
            return node

    # Convert the entire dictionary to a list of hierarchical structures
        return [
            create_node(key, value) 
            for key, value in input_dict.items()
        ]

    def start(self):
        """Start the UI."""
        self.render()


ui.run()
