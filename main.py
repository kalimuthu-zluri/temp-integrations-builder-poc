from nicegui import ui
from nicegui.events import ValueChangeEventArguments
from views.nodeView import NodeView
from views.requestView import RequestView
from views.variableOptionsView import VariableOptionsView
from views.dataMapperView import DataMapperView
from views.dataProcessingView import DataProcessView


def show(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    ui.notify(f"{name}: {event.value}")


def initView(view):
    view.start()


full_stretch_class = "w-full h-full"

with ui.splitter(value=30).classes("w-full h-screen") as navScreenDivider:
    with navScreenDivider.before:
        nodeView = NodeView()
        initView(nodeView)

    with navScreenDivider.after:
        with ui.splitter(horizontal=True, value=55).classes(
            full_stretch_class
        ) as apiIODivider:

            with apiIODivider.before:
                with ui.splitter(value=30).classes(
                    full_stretch_class
                ) as requestSplitter:
                    with requestSplitter.after:
                        requestView = RequestView()
                        initView(requestView)

                    with requestSplitter.before:
                        variableOptionsView = VariableOptionsView()
                        initView(variableOptionsView)

            with apiIODivider.after:
                with ui.splitter().classes(full_stretch_class) as responseSplitter:
                    with responseSplitter.before:
                        dataMapperView = DataMapperView()
                        initView(dataMapperView)
                    with responseSplitter.after:
                        dataProcessView = DataProcessView()
                        initView(dataProcessView)


ui.run()
