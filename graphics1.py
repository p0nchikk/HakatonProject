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
    ui.input(label='Enter your name: ', placeholder='start typing')
    name = ui.label()
    ui.input(label='Enter your phone number: ', placeholder='start typing')
    phone = ui.label()
    ui.button('Next', on_click=lambda: ui.navigate.to("/studentPage", new_tab=False))

    ui.button('Back', on_click=ui.navigate.back)
    ui.button('Back', on_click=ui.navigate.back)
    ui.button('Forward', on_click=ui.navigate.forward)

def adultPage():
    pass


ui.run(root())