from nicegui import ui
from uuid import uuid4

def root() :
    ui.separator()
    ui.sub_pages({'/' : mainPage, '/studentPage' : studentPage, '/adultPage' : adultPage })


def mainPage():
    ui.label('Welcome to our web')
    ui.button('Adult', on_click=lambda: ui.navigate.to( "/adultPage", new_tab=True))
    ui.button('Student', on_click=lambda: ui.navigate.to( "/studentPage", new_tab=False))



def studentPage () :
    ui.input(label='Text', placeholder='start typing',
             on_change=lambda e: result.set_text('you typed: ' + e.value),
             validation={'Input too long': lambda value: len(value) < 20})
    result = ui.label()

    ui.button('Back', on_click=ui.navigate.back)
    ui.button('Back', on_click=ui.navigate.back)
    ui.button('Forward', on_click=ui.navigate.forward)

def adultPage():
    pass


ui.run(root())