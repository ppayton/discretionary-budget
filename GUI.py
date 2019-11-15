from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup

Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '1000')
Config.write()

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<LoginScreen>:
    BoxLayout:
        orientation:'vertical'
        Label:
            text: 'Foot Prints'
            font_size: '130sp'
        Label:
            text: 'Sign In'
            font_size: '50sp'
        Label:
            text: 'Username:'
            font_size: '40sp'
        TextInput:
            id: usernameInput
            multiline: False
            font_size:'50sp'
        Label:
            text: 'Password:'
            font_size: '40sp'
        TextInput:
            id:passwordInput
            multiline: False
            font_size:'50sp'
            password: 'True'
        Button:
            text: 'Login'
            font_size:50
            on_press: root.getInput()
        Label:
            text: 'Or new user:'
            font_size: '40sp'
        Button:
            text: 'Register'
            font_size:50
            on_press: root.manager.current = 'create'

<CreateAccount>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Create Account'
            font_size: '130sp'
        Label:
            text: 'Username: (required)'
            font_size: '40sp'
        TextInput:
            id: createUsernameInput
            multiline: False
            font_size:'50sp'
        Label:
            text: 'Password: (required)'
            font_size: '40sp'
        TextInput:
            id: createPasswordInput
            multiline: False
            font_size:'50sp'
            password: 'True'
        Label:
            text: 'Monthly Budget Amount: (required)'
            font_size: '40sp'
        TextInput:
            id: monthBudget
            multiline: False
            font_size:'50sp'
        Button:
            text: 'Register'
            font_size:50
            on_press: root.createUser()
        Label:
            text: 'Have an account? '
            font_size: '20sp'
        Button:
            text: 'Sign In'
            font_size:50
            on_press: root.manager.current = 'login'

<Dashboard>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Dashboard'
            font_size: '130sp'
        Label:
            text: 'Monthly Budget: '
            font_size: '40sp'
        Label:
            text: 'test amount'
            font_size: '40sp'
        Label:
            text: 'Remaining Monthly Budget: '
            font_size: '40sp'
        Label:
            text: 'test amount'
            font_size: '40sp'
        Button:
            text: 'Update Monthly Budget'
            font_size:50
            on_press: root.manager.current = 'monthB'
        Button:
            text: 'Display Graphs and Reports'
            font_size:50
        Button:
            text: 'Enter Expenses'
            font_size:50
            on_press: root.manager.current = 'expense'
        Button:
            text: 'Logout'
            font_size:50
            on_press: root.manager.current = 'login'

<monthlyBudget>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Update Budget'
            font_size: '130sp'
        Label:
            text: 'New Budget: '
            font_size: '40sp'
        TextInput:
            multiline: 'false'
            font_size:'50sp'
        Button:
            text: 'Save'
            font_size:50
        Button:
            text: 'Back to Dashboard'
            font_size:50
            on_press: root.manager.current = 'dash'

<Graphs>:
    BoxLayout:
        orientation: 'vertical'

<enterExpenses>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Enter Expense'
            font_size: '130sp'
        Label:
            text: 'Category: '
            font_size: '40sp'
        DropDown:
        Label:
            text: 'Sub-Category: '
            font_size: '40sp'
        DropDown:
        Label:
            text: 'Amount:'
            font_size: '40sp'
        TextInput:
            multiline: 'false'
            font_size:'50sp'
        Button:
            text: 'Submit'
            font_size:50
        Button:
            text: 'Back to Dashboard'
            font_size:50
            on_press: root.manager.current = 'dash'
""")


# Declare both screens
class LoginScreen(Screen):
    def getInput(self):
        # get user input for username
        uname = self.ids.usernameInput.text

        # get user input for password
        pwd = self.ids.passwordInput.text

        correctLogin = True #call function to check if username and password are correct

        #print for error checking
       # print(uname)
       # print(pwd)

        if(correctLogin):
            #print for error checking
           # print('pwd is correct!!')
            sm.current = 'dash'
        else:
            #error msg when username or password is not correct
            popup = Popup(title='Error', content=Label(text='Error, username or password is not correct, please enter again. \n \n To close this popup click anywhere.'),size=(700, 600), size_hint=(None, None))
            popup.open()
    pass

class CreateAccount(Screen):
    def createUser(self):
          # get user input for username
        uname = self.ids.createUsernameInput.text

        # get user input for password
        pwd = self.ids.createPasswordInput.text

         # get user input for monthly budget
        mBudget = self.ids.monthBudget.text

        if(mBudget.isdigit()):
            loginSuccessful = True # call function to check if username and password are correct

            if(loginSuccessful):
                sm.current = 'dash'
            else:
                 #error msg when create account is not successful
                popup = Popup(title='Error', content=Label(text='Error, create account was not successful, please enter again. \n \n To close this popup click anywhere.'),size=(700, 600), size_hint=(None, None))
                popup.open()
        else:
            #error msg when monthly budget is not a number
            popup = Popup(title='Error', content=Label(text='Error, monthly budget must be a number, please enter again. \n \n To close this popup click anywhere.'),size=(700, 600), size_hint=(None, None))
            popup.open()

        print(uname)
        print(pwd)
        print(mBudget)

    pass

class Dashboard(Screen):
    pass

class monthlyBudget(Screen):
    pass

class Graphs(Screen):
    pass

class enterExpenses(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(CreateAccount(name='create'))
sm.add_widget(Dashboard(name='dash'))
sm.add_widget(monthlyBudget(name='monthB'))
sm.add_widget(Graphs(name='graph'))
sm.add_widget(enterExpenses(name='expense'))


class TestApp(App):

    def build(self):
        self.title = 'Foot Prints'
        return sm

if __name__ == '__main__':
   TestApp().run()
