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
            height: '95dp'

            Widget:
                on_parent: categoryDropdown.dismiss()
                categoryDropdown: categoryDropdown.__self__

            DropDown:
                id: categoryDropdown
                on_select: categoryBtn.text = '{}'.format(args[1])

                Button:
                    text: 'Improvements/Upgrades'
                    size_hint_y: None
                    height: '95dp'
                    on_release: categoryDropdown.select('Improvements/Upgrades')

                Button:
                    text: 'Social/Entertainment'
                    size_hint_y: None
                    height: '95dp'
                    on_release: categoryDropdown.select('Social/Entertainment')

                Button:
                    text: 'Personal Care & Hygiene'
                    size_hint_y: None
                    height: '95dp'
                    on_release: categoryDropdown.select('Personal Care & Hygiene')

                Button:
                    text: 'Savings'
                    size_hint_y: None
                    height: '95dp'
                    on_release: categoryDropdown.select('Savings')

        Button:
            id: subBtn
            text: 'Sub-Category'
            on_release: subCategoryDropdown.open(self)
            size_hint_y: None
            height: '95dp'

            Widget:
                on_parent: subCategoryDropdown.dismiss()
                subCategoryDropdown: subCategoryDropdown.__self__

            DropDown:
                id: subCategoryDropdown
                on_select: subBtn.text = '{}'.format(args[1])

                Button:
                    text: 'Home'
                    size_hint_y: None
                    height: '40dp'
                    on_release: subCategoryDropdown.select('Home')

                Button:
                    text: 'Automotive'
                    size_hint_y: None
                    height: '40dp'
                    on_release: subCategoryDropdown.select('Automotive')

                Button:
                    text: 'Electronic'
                    size_hint_y: None
                    height: '40dp'
                    on_release: subCategoryDropdown.select('Electronic')

                Button:
                    text: 'Dining Out'
                    size_hint_y: None
                    height: '40dp'
                    on_release: subCategoryDropdown.select('Dining Out')

                Button:
                    text: 'Special Events'
                    size_hint_y: None
                    height: '40dp'
                    on_release: subCategoryDropdown.select('Special Events')

                Button:
                    text: 'Games'
                    size_hint_y: None
                    height: '40dp'
                    on_release: subCategoryDropdown.select('Games')

                Button:
                    text: 'Gifts'
                    size_hint_y: None
                    height: '40dp'
                    on_release: subCategoryDropdown.select('Gifts')

                Button:
                    text: 'Subscriptions'
                    size_hint_y: None
                    height: '40dp'
                    on_release: subCategoryDropdown.select('Subscriptions')

                Button:
                    text: 'Cosmetics'
                    size_hint_y: None
                    height: '40dp'
                    on_release: subCategoryDropdown.select('Cosmetics')

                Button:
                    text: 'Clothes'
                    size_hint_y: None
                    height: '40dp'
                    on_release: subCategoryDropdown.select('Clothes')

                Button:
                    text: 'Toiletries'
                    size_hint_y: None
                    height: '40dp'
                    on_release: subCategoryDropdown.select('Toiletries')

                Button:
                    text: 'Memberships'
                    size_hint_y: None
                    height: '40dp'
                    on_release: subCategoryDropdown.select('Memberships')

                Button:
                    text: 'Emergency Fund'
                    size_hint_y: None
                    height: '40dp'
                    on_release: subCategoryDropdown.select('Emergency Fund')

                Button:
                    text: 'Asset Deposits'
                    size_hint_y: None
                    height: '40dp'
                    on_release: subCategoryDropdown.select('Asset Deposits')

                Button:
                    text: 'Vacations'
                    size_hint_y: None
                    height: '40dp'
                    on_release: subCategoryDropdown.select('Vacations')

                Button:
                    text: 'Appliances'
                    size_hint_y: None
                    height: '40dp'
                    on_release: subCategoryDropdown.select('Appliances')

                Button:
                    text: 'Other'
                    size_hint_y: None
                    height: '40dp'
                    on_release: subCategoryDropdown.select('Other')

        Label:
            text: 'Amount:'
            font_size: '40sp'
        TextInput:
            id: expenseAmt
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

def validSelection(category, subcategory ):
    print('this is a test ')
    improveGroup = ('Improvements/Upgrades','Home','Automotive','Electronic','Other' )
    socialGroup = ('Social/Entertainment','Dining Out','Special Events','Games', 'Gifts','Subscriptions','Other')
    personalGroup = ('Personal Care & Hygiene', 'Cosmetics', 'Clothes', 'Toiletries', 'Memberships', 'Other')
    savingGroup = ('Savings','Emergency Fund', 'Asset Deposits', 'Vacations', 'Appliances', 'Other')
    return True

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
                    #error msg when update budget is successful
                    popup = Popup(title='Success', content=Label(text='Success, monthly budget has been updated. \n \n To close this popup click anywhere.'),size=(700, 600), size_hint=(None, None))
                    popup.open()
                else:
                     #error msg when update budget is not successful
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

         #get value for category
         category = self.ids.categoryBtn.text

         #get value for sub-category
         subcategory = self.ids.subBtn.text

         expenseAmt = self.ids.expenseAmt.text

         #printing for error checking
         print(category)
         print(subcategory)
         print(expenseAmt)

         if(category == 'Category' or subcategory == 'Sub-Category' or expenseAmt == ''):
          #error msg when field is empty
                popup = Popup(title='Error', content=Label(text='Error, all fields must be filled out, please enter again. \n \n To close this popup click anywhere.'),size=(700, 600), size_hint=(None, None))
                popup.open()
         else:
                if(expenseAmt.isdigit()):
                    expenseSuccessful = True #function call to enter in an expense

                    if(validSelection(category, subcategory)):
                        if(expenseSuccessful):
                            #error msg when enter expense is  successful
                            popup = Popup(title='Success', content=Label(text='Success, expense has been entered. \n \n To close this popup click anywhere.'),size=(700, 600), size_hint=(None, None))
                            popup.open()
                        else:
                             #error msg when enter expense is not successful
                            popup = Popup(title='Error', content=Label(text='Error, enter expense was not successful, please enter again. \n \n To close this popup click anywhere.'),size=(700, 600), size_hint=(None, None))
                            popup.open()
                else:
                     #error msg when expense is not a number
                    popup = Popup(title='Error', content=Label(text='Error, expense amount must be a number, please enter again. \n \n To close this popup click anywhere.'),size=(700, 600), size_hint=(None, None))
                    popup.open()

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
