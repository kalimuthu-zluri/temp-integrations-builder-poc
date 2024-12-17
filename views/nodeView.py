from nicegui import ui

class NodeView:
    def __init__(self):
        # Initialize the node mapping
        self.node_mapping = {
            "Root": {
                "Child 1": {
                    "Grandchild 1.1": None,
                    "Grandchild 1.2": None,
                },
                "Child 2": None,
            }
        }
        self.container = ui.column().classes("m-4")


    def render_nodes(self, mapping, container=None):
        """Recursively render nodes based on the mapping."""
        if container is None:
            container = ui.column()
        for key, value in mapping.items():
            with container:
                with ui.row():
                    label = ui.label(key).classes("font-bold")
                    # ui.button("+", on_click=lambda k=key, m=mapping: add_node(k, m))
                    ui.button("-", on_click=lambda k=key, m=mapping: self.remove_node(k, m))
                    ui.button("open", on_click=ui.notify("open"))
                
                if isinstance(value, dict):  # Has children
                    child_container = ui.column().classes("pl-4")
                    self.render_nodes(value, child_container)

    def add_node(self, parent_key, mapping):
        """Add a child node to the given parent key."""
        if parent_key in mapping and isinstance(mapping[parent_key], dict):
            mapping[parent_key][f"New Child {len(mapping[parent_key]) + 1}"] = None
        elif parent_key in mapping and mapping[parent_key] is None:
            mapping[parent_key] = {f"New Child 1": None}
        self.update_ui()

    def remove_node(self, key, mapping):
        """Remove a node and its children from the mapping."""
        mapping.pop(key, None)
        key = None
        self.update_ui()

    def update_ui(self):
        """Refresh the UI with updated node mapping."""
        self.container.clear()  # Clear all existing UI components
        with self.container:
            with ui.row():
                ui.button("Add Node", on_click=self.open_add_node_popup)
            self.render_nodes(self.node_mapping)

    def get_all_nodes(self, mapping, prefix=""):
        """Get a list of all nodes in the mapping, with paths for unique identification."""
        nodes = []
        for key, value in mapping.items():
            full_path = f"{prefix}/{key}" if prefix else key
            nodes.append(full_path)
            if isinstance(value, dict):
                nodes.extend(self.get_all_nodes(value, full_path))
        return nodes


    def add_node_to_mapping(self,parent_path, mapping, node_name):
        """Add a child node to the specified parent path."""
        parts = parent_path.split("/")
        current = mapping
        for part in parts:
            if isinstance(current, dict) and part in current:
                current = current[part]
        if isinstance(current, dict):
            current[node_name] = None
        self.update_ui()


    def open_add_node_popup(self):
        """Open a popup to add a new node."""
        with ui.dialog() as popup:
            with ui.card():
                ui.label("Add a new node").classes("font-bold text-lg")
                nodes = self.get_all_nodes(self.node_mapping)
                selected_node = ui.select(nodes, label="Select Parent")
                new_node_name = ui.input(label="Node Name")
                with ui.row():
                    ui.button("Add", on_click=lambda: [
                        self.add_node_to_mapping(selected_node.value, self.node_mapping, new_node_name.value),
                        popup.close()
                    ])
                    ui.button("Cancel", on_click=popup.close)
        popup.open()

    def start(self):
        """Start the UI."""
        self.update_ui()

ui.run()
