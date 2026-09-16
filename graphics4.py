from idlelib import textview

from nicegui import ui
from uuid import uuid4

from nicegui.elements import button

from consts import CITY_LIST

import consts
import database
import adult
import student
import requests


def root() :
    ui.separator()
    database.init_database()
    ui.sub_pages({'/' : mainPage
                     , '/studentPage' : studentPage
                     , '/adultPage' : adultPage
                     , '/cityPage' : cityPage
                    , '/requestsPage' : requestsPage
                  , '/newRequestsPage' : newRequestsPage
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
    with ui.row():
        ui.button('new request', on_click=lambda: ui.navigate.newRequestsPage)
        ui.label(f'requests by {adult.adult['name']}:').classes('text-h6')

    # שומר את הרשימה של הבקשות של הזקן מהדטה בייס
    requests_list_by_man = database.get_user_requests(int(adult.adult['phone']))
    # מראה לזקן את הבקשות שלו
    index = 0
    try:
        while True:
            ui.label(f'Category: {requests_list_by_man[index]['Category']}')
            ui.label(f'description: {requests_list_by_man[index]['Description']}')
            ui.label(f'phone: {requests_list_by_man[index]['Owner_number']}')
    except ImportError:
        if index == len(requests_list_by_man):
            index = 0
        else:
            index = len(requests_list_by_man) - 1
    with ui.row():
        ui.button('next', on_click=lambda: index + 1)
        ui.button('last', on_click=lambda: index - 1)


##################### עמוד יצירת בקשה חדשה
def newRequestsPage():
    ui.label('creat new requests').classes('text-h6')

    with ui.row():
        select_categories = ui.select(consts.CATEGORIES)
        description = ui.textarea(label='Text', placeholder='start typing')
        #מציג את הקבועים
        ui.labl(f'name: {adult.adult.name}')
        ui.labl(f'phone number: {adult.adult.phone}')
        ui.labl(f'city: {adult.adult.city}')

        ui.button('save', on_click=lambda : save_request(select_categories.value, description.value,adult.adult.name,adult.adult.phone, adult.adult.city))


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
    adult.adult = adult.create_adult(name,phone,city)
    ui.navigate.to("/requestsPage", new_tab=False)

def save_request(category, description,owner_name,owner_number, owner_area): #מקבל את כל התנאים של יצירת בקשה
    requests.create_request(category, description,owner_name,owner_number, owner_area)
    ui.navigate.to("/requestsPage", new_tab=False)


def next_requests(list_to_sow):
    '''with ui.card():
        ui.label('requests').classes('text-h6')
        with ui.column():
    #לחזור לזה רק אחרי שיש נתונים בדטה בייס
'''
    pass


ui.run(root())

