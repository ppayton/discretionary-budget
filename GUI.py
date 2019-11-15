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
from kivy.properties import StringProperty

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
            text: root.monthlyBudgetAmt
            font_size: '40sp'
        Label:
            text: 'Remaining Monthly Budget: '
            font_size: '40sp'
        Label:
            text: root.remMonthlyBudgetAmt
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
            id: monthlyBudgetAmt
            multiline: False
            font_size:'50sp'
        Button:
            text: 'Save'
            font_size:50
            on_press: root.updateBudget()
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

        Button:
            id: categoryBtn
            text: 'Category'
            on_release: categoryDropdown.open(self)
            size_hint_y: None
            height: '48dp'

            Widget:
                on_parent: categoryDropdown.dismiss()

            DropDown:
                id: categoryDropdown
                on_select: categoryBtn.text = 'Selected value: {}'.format(args[1])

                Button:
                    text: 'Value A'
                    size_hint_y: None
                    height: '48dp'
                    on_release: categoryDropdown.select('A')

                Button:
                    text: 'Value B'
                    size_hint_y: None
                    height: '48dp'
                    on_release: categoryDropdown.select('B')

                Button:
                    text: 'Value C'
                    size_hint_y: None
                    height: '48dp'
                    on_release: categoryDropdown.select('C')

        Button:
            id: subBtn
            text: 'Sub-Category'
            on_release: subCategoryDropdown.open(self)
            size_hint_y: None
            height: '48dp'

            Widget:
                on_parent: subCategoryDropdown.dismiss()

            DropDown:

                id: subCategoryDropdown
                on_select: subBtn.text = 'Selected value: {}'.format(args[1])

                Button:
                    text: 'Value A'
                    size_hint_y: None
                    height: '48dp'
                    on_release: subCategoryDropdown.select('A')

                Button:
                    text: 'Value B'
                    size_hint_y: None
                    height: '48dp'
                    on_release: subCategoryDropdown.select('B')

                Button:
                    text: 'Value C'
                    size_hint_y: None
                    height: '48dp'
                    on_release: subCategoryDropdown.select('C')

        Label:
            text: 'Amount:'
            font_size: '40sp'
        TextInput:
            multiline: False
            font_size:'50sp'
        Button:
            text: 'Submit'
            font_size:50
            on_press: root.addExpense()
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
        if(uname != '' and pwd != ''):
            if(correctLogin):
                #print for error checking
               # print('pwd is correct!!')
                sm.current = 'dash'
            else:
                #error msg when username or password is not correct
                popup = Popup(title='Error', content=Label(text='Error, username or password is not correct, please enter again. \n \n To close this popup click anywhere.'),size=(700, 600), size_hint=(None, None))
                popup.open()
        else:
         #error msg when fields are empty
            popup = Popup(title='Error', content=Label(text='Error, all fields must be filled out, please enter again. \n \n To close this popup click anywhere.'),size=(700, 600), size_hint=(None, None))
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
        if(uname == ''):
            print('this is empty')

        if(mBudget.isdigit()):
            if(uname != '' and pwd != '' and mBudget != ''):
                loginSuccessful = True # call function to check if username and password are correct

                if(loginSuccessful):
                    sm.current = 'dash'
                else:
                     #error msg when create account is not successful
                    popup = Popup(title='Error', content=Label(text='Error, create account was not successful, please enter again. \n \n To close this popup click anywhere.'),size=(700, 600), size_hint=(None, None))
                    popup.open()
            else:
                #error msg when fields are empty
                popup = Popup(title='Error', content=Label(text='Error, all fields must be filled out, please enter again. \n \n To close this popup click anywhere.'),size=(700, 600), size_hint=(None, None))
                popup.open()
        else:
                #error msg when monthly budget is not a number
                popup = Popup(title='Error', content=Label(text='Error, monthly budget must be a number, please enter again. \n \n To close this popup click anywhere.'),size=(700, 600), size_hint=(None, None))
                popup.open()

        #print for error checking
        #print(pwd)
        #print(mBudget)

    pass

class Dashboard(Screen):
    # need function to get current values for monthly budget and remaining monthly budget from database
    monthlyBudgetAmt = StringProperty()
    monthlyBudgetAmt = '500';

    remMonthlyBudgetAmt = StringProperty()
    remMonthlyBudgetAmt = '200';

    pass

class monthlyBudget(Screen):
    def updateBudget(self):
         # get user input for monthly budget
        mBudget = self.ids.monthlyBudgetAmt.text

        if(mBudget.isdigit()):
            if(mBudget != ''):
                budgetSuccessful = True # call function to change monthly budget

                if(budgetSuccessful):
                    #error msg when create account is not successful
                    popup = Popup(title='Success', content=Label(text='Success, monthly budget has been updated. \n \n To close this popup click anywhere.'),size=(700, 600), size_hint=(None, None))
                    popup.open()
                else:
                     #error msg when budget is not successful
                    popup = Popup(title='Error', content=Label(text='Error, budget change was not successful, please enter again. \n \n To close this popup click anywhere.'),size=(700, 600), size_hint=(None, None))
                    popup.open()
            else:
                #error msg when budget is empty
                popup = Popup(title='Error', content=Label(text='Error, budget must be filled out, please enter again. \n \n To close this popup click anywhere.'),size=(700, 600), size_hint=(None, None))
                popup.open()
        else:
                #error msg when monthly budget is not a number
                popup = Popup(title='Error', content=Label(text='Error, monthly budget must be a number, please enter again. \n \n To close this popup click anywhere.'),size=(700, 600), size_hint=(None, None))
                popup.open()

       #printing for error checking
        # print(mBudget)

    pass

class Graphs(Screen):
    pass

class enterExpenses(Screen):
     def addExpense(self):
        print('I come here')
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
