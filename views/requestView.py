from nicegui import ui

class RequestView:
    def __init__(self):
        # Initialize the node mapping
        self.container = ui.row().classes("m-4 bg-gray-300")
    
    # def show(event: ValueChangeEventArguments):
    #     name = type(event.sender).__name__
    #     ui.notify(f"{name}: {event.value}")


    # Function to handle the "Send" button click
    def send_request(self):
        method = self.method_dropdown.value
        url = self.endpoint_input.value
        # Placeholder: Add logic to handle the request based on tabs
        ui.notify(f"Sending {method} request to {url}", color="green")

    def curl_to_req(self):
        ui.notify()
        # curl_msg = curl_input.value.replace("--location ", "").replace(" \ ", " ")
        # print(f'curl_msg : {curl_msg}')
        # msg = uncurl.parse_context(curl_msg)
        # print(msg.url)
        # req = {}
        # req["url"] = msg.url
        # req["method"] = msg.method
        # print(msg.headers.keys())
        # for i in msg.headers.keys():
        #     print(i)
        # print(msg.data)
        # print(req)
        # ui.notify(curl_input.value)


    def add_param_row(self):
        with self.params_container:
            with ui.row().style("margin-bottom: 8px") as row:
                ui.input(placeholder="Key").style("width: 30%")
                ui.input(placeholder="Value").style("width: 30%")
                ui.input(placeholder="Description").style("width: 30%")
                ui.button("✖️", on_click=lambda: row.delete()).style("width: 5%")


    def add_header_row(self):
        with self.header_container:
            with ui.row().style("margin-bottom: 8px") as row:
                ui.input(placeholder="Key", on_change=self.update_header_data).style("width: 30%")
                ui.input(placeholder="Value", on_change=self.update_header_data).style("width: 30%")
                ui.input(placeholder="Description").style("width: 30%")
                ui.button("✖️", on_click=lambda: row.delete()).style("width: 5%")


    def update_header_data():
        print()

    def update_auth_fields(self):
        auth_type = self.auth_type_dropdown.value
        self.auth_fields.clear()  # Clear previous fields

        if auth_type == "Basic":
            with self.auth_fields:
                ui.input("Username", placeholder="Enter username").style(
                    "margin-bottom: 8px;"
                )
                ui.input("Password", placeholder="Enter password", password=True)
        elif auth_type == "Bearer Token":
            with self.auth_fields:
                ui.input("Token", placeholder="Enter token")
        elif auth_type == "API Key":
            with self.auth_fields:
                ui.input("Key", placeholder="Enter key").style("margin-bottom: 8px;")
                ui.input("Value", placeholder="Enter value").style("margin-bottom: 8px;")
                ui.select(["Header", "Query Params"], label="Add to", value="Header")


    def update_body_fields(self):
        body_type = self.body_type_dropdown.value
        self.body_fields.clear()  # Clear previous fields

        if body_type == "raw":
            with self.body_fields:
                ui.textarea("Raw JSON", placeholder="Enter your JSON body here").style(
                    "width: 100%; height: 200px;"
                )
        elif body_type == "form-data":
            with self.body_fields:
                ui.input("Form Key", placeholder="Enter form key").style(
                    "margin-bottom: 8px;"
                )
                ui.input("Form Value", placeholder="Enter form value")
        elif body_type == "x-www-form-urlencoded":
            with self.body_fields:
                ui.input("URL-encoded Key", placeholder="Enter key").style(
                    "margin-bottom: 8px;"
                )
                ui.input("URL-encoded Value", placeholder="Enter value")
        elif body_type == "binary":
            with self.body_fields:
                ui.file("Upload File")

    def renderRequestView(self):

        with self.container:
            self.curl_input = ui.input("Curl input").classes("m-2")
            self.curl_submit_button = (
                ui.button("Convert", on_click=self.curl_to_req)
                .classes("m-2")
                .classes("m-2")
            )

            ui.separator()

            self.method_dropdown = ui.select(
                ["GET", "POST", "PUT", "DELETE"],
                value="GET",
                on_change=self.send_request,
            ).classes("m-2")
            self.protocol_dropdown = ui.select(
                ["http", "https"],
                value="https",
                on_change=self.send_request,
            ).classes("m-2")
            self.domain_input = ui.input("Enter Domain")
            self.endpoint_input = ui.input("Enter Endpoint")
            self.send_button = ui.button(
                "Send", on_click=self.send_request
            ).classes("m-2")

            ui.separator()

            # Tabs for Params, Headers, Authorization, Body
            with ui.tabs() as tabs:
                Params = ui.tab("Params")
                Headers = ui.tab("Headers")
                Authorization = ui.tab("Authorization")
                Body = ui.tab("Body")

            with ui.tab_panels(tabs, value=Headers).classes(
                "w-full m-4 bg-gray-100"
            ):
                with ui.tab_panel(Params):
                    ui.label("Query Parameters").style(
                        "font-weight: bold; margin-bottom: 8px"
                    )

                    # Container to hold rows dynamically
                    with ui.column().style(
                        "max-height: 300px; overflow-y: auto; border: 1px solid #ccc; padding: 8px;"
                    ):
                        self.params_container = (
                            ui.column()
                        )  # Dynamic container for rows
                        self.add_param_row()  # Add initial row

                    # Button to add more rows
                    ui.button(
                        "Add Param", on_click=self.add_param_row
                    ).style("margin-top: 16px")

                with ui.tab_panel(Headers):
                    ui.label("Headers").style(
                        "font-weight: bold; margin-bottom: 8px"
                    )

                    # Container to hold rows dynamically
                    with ui.column().style(
                        "max-height: 300px; overflow-y: auto; border: 1px solid #ccc; padding: 8px;"
                    ):
                        self.header_container = (
                            ui.column()
                        )  # Dynamic container for rows
                        self.headers = {"key": {}, "value": {}}
                        self.add_header_row()  # Add initial row

                    # Button to add more rows
                    ui.button(
                        "Add Param", on_click=self.add_header_row
                    ).style("margin-top: 16px")

                with ui.tab_panel(Authorization):
                    ui.label("Authorization Settings").style(
                        "font-weight: bold; margin-bottom: 8px"
                    )

                    # Dropdown for Auth Type
                    self.auth_type_dropdown = ui.select(
                        ["Basic", "Bearer Token", "API Key"],
                        value="Basic",
                        label="Auth Type",
                        on_change=self.update_auth_fields,
                    ).style("margin-bottom: 16px")

                    # Dynamic container for auth fields
                    self.auth_fields = ui.column()
                    self.update_auth_fields()  # Initialize with the default option

                with ui.tab_panel(Body):
                    ui.label("Request Body").style(
                        "font-weight: bold; margin-bottom: 8px"
                    )

                    # Dropdown for Body Type
                    self.body_type_dropdown = ui.select(
                        [
                            "none",
                            "form-data",
                            "x-www-form-urlencoded",
                            "raw",
                            "binary",
                        ],
                        value="raw",
                        label="Body Type",
                        on_change=self.update_body_fields,
                    ).style("margin-bottom: 16px")

                    # Dynamic container for body fields
                    self.body_fields = ui.column()
                    self.update_body_fields()  # Initialize with raw option

    def start(self):
            """Start the UI."""
            self.renderRequestView()

ui.run()
