import os
from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.h4("I need an Environment Variable called NAME"),
    ui.output_text_verbatim("txt"),
)


def server(input, output, session):
    @output
    @render.text
    def txt():
        return f"Your name is: {os.getenv('NAME')}"


app = App(app_ui, server)
