from nicegui import ui
from nicegui.events import ValueChangeEventArguments
from nodeTree import DynamicNodeManager
import uncurl



def show(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    ui.notify(f"{name}: {event.value}")


# Function to handle the "Send" button click
def send_request():
    method = method_dropdown.value
    url = endpoint_input.value
    # Placeholder: Add logic to handle the request based on tabs
    ui.notify(f"Sending {method} request to {url}", color="green")

def curl_to_req():
    ui.notify(demo.static_request_config["Auth"]["token"])
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


def add_param_row():
    with params_container:
        with ui.row().style("margin-bottom: 8px") as row:
            ui.input(placeholder="Key").style("width: 30%")
            ui.input(placeholder="Value").style("width: 30%")
            ui.input(placeholder="Description").style("width: 30%")
            ui.button("✖️", on_click=lambda: row.delete()).style("width: 5%")


def add_header_row():
    with header_container:
        with ui.row().style("margin-bottom: 8px") as row:
            ui.input(placeholder="Key", on_change=update_header_data).style("width: 30%")
            ui.input(placeholder="Value", on_change=update_header_data).style("width: 30%")
            ui.input(placeholder="Description").style("width: 30%")
            ui.button("✖️", on_click=lambda: row.delete()).style("width: 5%")


def update_header_data():
    print()

def update_auth_fields():
    auth_type = auth_type_dropdown.value
    auth_fields.clear()  # Clear previous fields

    if auth_type == "Basic":
        with auth_fields:
            ui.input("Username", placeholder="Enter username").style(
                "margin-bottom: 8px;"
            )
            ui.input("Password", placeholder="Enter password", password=True)
    elif auth_type == "Bearer Token":
        with auth_fields:
            ui.input("Token", placeholder="Enter token")
    elif auth_type == "API Key":
        with auth_fields:
            ui.input("Key", placeholder="Enter key").style("margin-bottom: 8px;")
            ui.input("Value", placeholder="Enter value").style("margin-bottom: 8px;")
            ui.select(["Header", "Query Params"], label="Add to", value="Header")


def update_body_fields():
    body_type = body_type_dropdown.value
    body_fields.clear()  # Clear previous fields

    if body_type == "raw":
        with body_fields:
            ui.textarea("Raw JSON", placeholder="Enter your JSON body here").style(
                "width: 100%; height: 200px;"
            )
    elif body_type == "form-data":
        with body_fields:
            ui.input("Form Key", placeholder="Enter form key").style(
                "margin-bottom: 8px;"
            )
            ui.input("Form Value", placeholder="Enter form value")
    elif body_type == "x-www-form-urlencoded":
        with body_fields:
            ui.input("URL-encoded Key", placeholder="Enter key").style(
                "margin-bottom: 8px;"
            )
            ui.input("URL-encoded Value", placeholder="Enter value")
    elif body_type == "binary":
        with body_fields:
            ui.file("Upload File")


class Entity:
    def __init__(self):
        self.static_request_config = {
            "Headers": [{ "Headerkey": 'added Header Value' }],
            "Params": [{ "queryKey": 'added query Value' }],
            "URL": {
                "protocol": 'https',
                "method": 'GET',
                "domain": 'pokeapi.co',
                "endpoint": 'api/v2/pokemon'
            },
            "Auth": {
                "type": 'Bearer',
                "token": '123'
            },
            "Body": {
                "type": 'JSON',
                "data": {}
            }
        }

        self.pagination_config = {
            "type": 'LIMIT_OFFSET',
            "limit": 100,
            "limitKey": 'limit',
            "offsetKey": 'offset',
            "breakCondition": ''
        }

        self.depenpencies = [
            {
                "entity": 'User',
                "fields": ['name']
            }
        ]

        self.responseContext = {
            "entity_locator": 'response.data.results',
            "save_path": 'pokemon_details'
        }


demo = Entity()

with ui.splitter(value=30).classes("w-full h-screen no-wrap") as splitter:
    with splitter.before:
        # Entities Screen
        with ui.column().classes(
            "w-full h-full items-center justify-top bg-gray-100 no-wrap"
        ):
            node_manager = DynamicNodeManager()
            node_manager.start()

    with splitter.after:
        # Entity Info Screen
        with ui.splitter(horizontal=True, value=55).classes(
            "w-full h-full no-wrap"
        ) as splitter1:
            with splitter1.separator:
                ui.separator()
            with splitter1.before:
                # Request Config Screen
                with ui.splitter(value=30).classes(
                    "w-full h-full no-wrap"
                ) as splitter2:

                    with splitter2.separator:
                        ui.separator()

                    with splitter2.after:
                        # Static Request Screen
                        with ui.row().classes("m-4 bg-gray-300"):
                            curl_input = ui.input("Curl input").classes("m-2")
                            curl_submit_button = (
                                ui.button("Convert", on_click=curl_to_req)
                                .classes("m-2")
                                .classes("m-2")
                            )

                            ui.separator()

                            method_dropdown = ui.select(
                                ["GET", "POST", "PUT", "DELETE"],
                                value="GET",
                                on_change=send_request,
                            ).classes("m-2")
                            protocol_dropdown = ui.select(
                                ["http", "https"],
                                value="https",
                                on_change=send_request,
                            ).classes("m-2")
                            domain_input = ui.input("Enter Domain")
                            endpoint_input = ui.input("Enter Endpoint").bind_value(demo.static_request_config["Auth"], 'token')
                            send_button = ui.button(
                                "Send", on_click=send_request
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
                                        params_container = (
                                            ui.column()
                                        )  # Dynamic container for rows
                                        add_param_row()  # Add initial row

                                    # Button to add more rows
                                    ui.button(
                                        "Add Param", on_click=add_param_row
                                    ).style("margin-top: 16px")

                                with ui.tab_panel(Headers):
                                    ui.label("Headers").style(
                                        "font-weight: bold; margin-bottom: 8px"
                                    )

                                    # Container to hold rows dynamically
                                    with ui.column().style(
                                        "max-height: 300px; overflow-y: auto; border: 1px solid #ccc; padding: 8px;"
                                    ):
                                        header_container = (
                                            ui.column()
                                        )  # Dynamic container for rows
                                        headers = {"key": {}, "value": {}}
                                        add_header_row()  # Add initial row

                                    # Button to add more rows
                                    ui.button(
                                        "Add Param", on_click=add_header_row
                                    ).style("margin-top: 16px")

                                with ui.tab_panel(Authorization):
                                    ui.label("Authorization Settings").style(
                                        "font-weight: bold; margin-bottom: 8px"
                                    )

                                    # Dropdown for Auth Type
                                    auth_type_dropdown = ui.select(
                                        ["Basic", "Bearer Token", "API Key"],
                                        value="Basic",
                                        label="Auth Type",
                                        on_change=update_auth_fields,
                                    ).style("margin-bottom: 16px")

                                    # Dynamic container for auth fields
                                    auth_fields = ui.column()
                                    update_auth_fields()  # Initialize with the default option

                                with ui.tab_panel(Body):
                                    ui.label("Request Body").style(
                                        "font-weight: bold; margin-bottom: 8px"
                                    )

                                    # Dropdown for Body Type
                                    body_type_dropdown = ui.select(
                                        [
                                            "none",
                                            "form-data",
                                            "x-www-form-urlencoded",
                                            "raw",
                                            "binary",
                                        ],
                                        value="raw",
                                        label="Body Type",
                                        on_change=update_body_fields,
                                    ).style("margin-bottom: 16px")

                                    # Dynamic container for body fields
                                    body_fields = ui.column()
                                    update_body_fields()  # Initialize with raw option

                    with splitter2.before:
                        # Dynamic Request Screen
                        ui.label("Dynamic Request Screen")
            with splitter1.after:
                # Response Screen
                ui.label("Response Structure Screen")
                with ui.splitter().classes("w-full h-full no-wrap") as splitter:
                    with splitter.before:
                        # Result Screen
                        ui.label("Result Screen")

                    with splitter.after:
                        ui.label("Post Proc Screen")
                # with ui.row().classes(
                #     "w-full h-full items-center justify-center bg-gray-300"
                # ):

ui.run()
