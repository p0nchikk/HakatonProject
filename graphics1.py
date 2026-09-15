from nicegui import ui
from uuid import uuid4

def root () :
    ui.label(f'This ID {str(uuid4())[:6]} changes only reload')
    ui.separator()
    ui.sub_pages({'/' : mainPage, '/studentPage' : studentPage })

#'/adultPage' : adultPage
ui.page('/mainPage')
def mainPage():
    ui.label('Welcome to our app')
    ui.button('Adult', on_click=lambda: ui.notify('You clicked me!'))
    ui.button('Student', on_click=lambda: ui.notify('You clicked me!'))
    ui.link('Student', "/studentPage")
    ui.link('Adult', "/adultPage")



ui.page('/studentPage')
def studentPage () :
    ui.textarea(label='Enter your name :', placeholder='start typing')




ui.button('student', on_click=lambda : ui.navigate.to('/studentPage'))
ui.run()