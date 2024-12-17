from nicegui import ui
from nicegui.events import ValueChangeEventArguments
from views.nodeTreeView import DynamicNodeManager
from views.requestView import RequestView
from views.variableOptionsView import VariableOptionsView
from views.dataMapperView import DataMapperView
from views.dataProcessingView import DataProcessView


def show(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    ui.notify(f"{name}: {event.value}")


with ui.splitter(value=30).classes("w-full h-screen no-wrap") as splitter:
    with splitter.before:
            node_manager = DynamicNodeManager()
            node_manager.start()

    with splitter.after:
        with ui.splitter(horizontal=True, value=55).classes(
            "w-full h-full no-wrap"
        ) as splitter1:

            with splitter1.before:
                with ui.splitter(value=30).classes(
                    "w-full h-full no-wrap"
                ) as splitter2:
                    with splitter2.after:
                        requestView = RequestView()
                        requestView.start()
                        
                    with splitter2.before:
                        variableOptionsView = VariableOptionsView()
                        variableOptionsView.start()
                        
            with splitter1.after:
                with ui.splitter().classes("w-full h-full no-wrap") as splitter:
                    with splitter.before:
                        dataMapperView = DataMapperView()
                        dataMapperView.start()
                    with splitter.after:
                        dataProcessView = DataProcessView()
                        dataProcessView.start()


ui.run()
