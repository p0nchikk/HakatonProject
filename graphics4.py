from idlelib import textview

from nicegui import ui
from uuid import uuid4

from nicegui.elements import button

from consts import CITY_LIST

import consts
import database
import adult
import student


def root() :
    ui.separator()
    ui.sub_pages({'/' : mainPage
                     , '/studentPage' : studentPage
                     , '/adultPage' : adultPage
                     , '/cityPage' : cityPage
                    , '/requestsPage' : requestsPage
                  })


def mainPage():
    ui.label('Welcome to our web')

    image = ui.image("hello.png").classes('w-64')
    toggle_dick = {"student" : 'studentPage', "adult" : 'adultPage'}
    toggle_image = ui.toggle(['student','adult']
                             ,on_change=lambda : image.set_source(f'{toggle_dick[toggle_image.value]}.PNG'))

    ui.button('chose', on_click=lambda: ui.navigate.to( f"/{toggle_dick[toggle_image.value]}", new_tab=False))




def studentPage () :
    ui.label('studentPage')

    name = ui.input(label='enter name:')
    phone = ui.input(label='enter phone number:')
    #כפתור שמור
    ui.button("save", on_click=lambda : save_student(name.value, phone.value))
    ui.button('Back', on_click=lambda : ui.navigate.back)



def adultPage():

    name = ui.input(label='enter name:')
    phone = ui.input(label='enter phone number:')
    city = ui.select(consts.CITY_LIST)

    ui.button('save', on_click=lambda : save_adult(name.value, phone.value, city.value))
    ui.button('Back', on_click= lambda : ui.navigate.back)



def requestsPage():
    ui.label(f'requests by {adult.adult['name']}').classes('text-h6')
    #מראה לזקן את הבקשות שלו

    #שומר את הרשימה של הבקשות של הזקן מהדטה בייס
    requests_list_by_man = database.get_user_requests(adult.adult['phone'])

    with ui.row():
        ui.button('next', on_click=lambda :next_requests(requests_list_by_man))
        ui.button('last')#להוסיף פעולה של לחזור אחורה


#העמוד של החיפוש של הנער
def cityPage():
    ui.label('chose city filter:')
    select_city = ui.select(consts.CITY_LIST)

#להמשיך אחרי שיהיה כבר משהו בתוך הדטה בייס
    #list_to_sow = database.get_requests_by_city('tel aviv')


    # Arrange items vertically inside a stylized container
    with ui.card():
        ui.label('requests').classes('text-h6')
        with ui.column():
            ui.button('dadw')
            #פרטי הבקשה
    #לולאת וויל שתפסיק כאשר הגיע לאורך הרשימה
    #תעלה משתנה כל פעם ב1 וזה יהיה המיקום ברשימה שמציגים
    #אם נלחץ כפתור בחר ביירק
    #להוסיף דפדוף בין הרשימה
    with ui.row():
        ui.button('Left')
        ui.button('Right')

    """for city in list_to_sow:
        ui.label(city)
    ui.separator().classes('my-4')"""

#הפעולה שנראת כאשר לוחצים על כתפור שמור ביצירת תלמיד
def save_student(name, phone):
    student.student = student.create_student(name, phone)
    ui.navigate.to("/cityPage", new_tab=False)

def save_adult(name, phone ,city):
    adult.adult = adult.create_adult(name,int(phone),city)
    ui.navigate.to("/requestsPage", new_tab=False)

def save_request(): #מקבל את כל התנאים של יצירת בקשה
    pass

def next_requests(list_to_sow):
    '''with ui.card():
        ui.label('requests').classes('text-h6')
        with ui.column():
    #לחזור לזה רק אחרי שיש נתונים בדטה בייס
'''
    pass


ui.run(root())

