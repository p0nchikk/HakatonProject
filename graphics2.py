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
    ui.query('body').classes('bg-slate-100')
    ui.add_head_html('''
        <style type="text/tailwindcss">
            h2 {
                color: white; 
                  background-color: blue; 
                  border: none; 
                  padding: 10px 20px; 
                  border-radius: 5px; 
                  cursor: pointer;
                  --custom-glow: rgba(0,0,0,0.2);
                  font-family: 'David';
                   text-align: center;
            }
        </style>
    ''')
    ui.html('<h2>Welcome to :</h2>', sanitize=False)

    #ui.label('Welcome to :').classes('text-2xl font-italic text-blue-600 w-full text-center').style('font-family : David')
    ui.label('helpUneed').classes('rounded bg-blue-200 text-4xl font-bold text-blue-600 w-full text-center place-content-center').style('font-family : David')
    ui.label('choose what you are :').classes('text-2xl  text-blue-600 place-content-center').style('font-family : David')

    image = ui.image("hello.jpg").classes('w-64 absolute-center')
    with ui.scroll_area().style('border : 1px solid; width: 35vh'):
      with ui.row().classes('w-full items-center justify-center'):
         toggle_dick = {"student" : 'studentPage', "adult" : 'adultPage'}
         toggle_image = ui.toggle(['student','adult']
                             ,on_change=lambda : image.set_source(f'{toggle_dick[toggle_image.value]}.PNG'))

    ui.button('choose', on_click=lambda: ui.navigate.to( f"/{toggle_dick[toggle_image.value]}", new_tab=False)).style('font-family : David')




def studentPage () :
       ui.label('Enter your details :').classes('text-2xl font-italic text-blue-600').style('font-family : David')
       name = ui.input(label='enter name:').classes('text-xl ').style('font-family : David')
       phone = ui.input(label='enter phone number:').classes('text-xl ').style('font-family : David')
    #כפתור שמור
       ui.button("save", on_click=lambda : save_student(name.value, phone.value)).style('font-family : David')
       ui.button('Back', on_click=lambda : ui.navigate.back).style('font-family : David')



def adultPage():
    ui.label('Enter details :').classes('text-2xl font-italic text-blue-600').style('font-family : David')
    name = ui.input(label='enter name:').style('font-family : David')
    phone = ui.input(label='enter phone number:').style('font-family : David')
    city = ui.select(consts.CITY_LIST)
    ui.button('save', on_click=lambda : save_adult(name.value, phone.value, city.value)).style('font-family : David')
    ui.button('Back', on_click= lambda : ui.navigate.back).style('font-family : David')



def requestsPage():
    ui.label(f'requests by {adult.adult['name']}').classes('text-h6').style('font-family : David')

    #מראה לזקן את הבקשות שלו

    #שומר את הרשימה של הבקשות של הזקן מהדטה בייס
    requests_list_by_man = database.get_user_requests(adult.adult['phone'])

    with ui.row():
        ui.button('next', on_click=lambda :next_requests(requests_list_by_man)).style('font-family : David')
        ui.button('last').style('font-family : David')#להוסיף פעולה של לחזור אחורה


#העמוד של החיפוש של הנער
def cityPage():
    ui.label('Choose city filter :').classes('text-2xl font-italic text-blue-600').style('font-family : David')
    select_city = ui.select(consts.CITY_LIST)

#להמשיך אחרי שיהיה כבר משהו בתוך הדטה בייס
    list_to_sow = database.get_requests_by_area('tel aviv')


    # Arrange items vertically inside a stylized container
    with ui.card():
        ui.label('requests').classes('text-h6').style('font-family : David')
        with ui.column():
            ui.button('dadw').style('font-family : David')
            #פרטי הבקשה
    #לולאת וויל שתפסיק כאשר הגיע לאורך הרשימה
    #תעלה משתנה כל פעם ב1 וזה יהיה המיקום ברשימה שמציגים
    #אם נלחץ כפתור בחר ביירק
    #להוסיף דפדוף בין הרשימה
    with ui.row():
        ui.button('Left').style('font-family : David')
        ui.button('Right').style('font-family : David')

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

