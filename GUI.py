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
from kivy.uix.spinner import Spinner
import matplotlib
import matplotlib.pyplot as plt
import re
import os
import numpy as np


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
            text: 'View and Download Graphs'
            font_size:50
            on_press: root.manager.current = 'graph'
        Button:
            text: 'Enter Expenses'
            font_size:50
            on_press: root.manager.current = 'expense'
        Button:
            text: 'Delete Expense'
            font_size:50
            on_press: root.manager.current = 'delete'
        Button:
            text: 'Logout'
            font_size:50
            on_press: root.logoutUser()

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

        Label:
            text: 'View/Download'
            font_size: '130sp'
        Label:
            text: 'Graphs'
            font_size: '130sp'
        Label:
            text: 'Generate graphs for: '
            font_size: '40sp'
        Spinner:
            id: timeList
            size_hint: None, None
            size: 1000, 44
            pos_hint: {'center': (.5, .5)}
            text: 'Month or Year'
        Label:
            text: 'Select type of graph to generate: '
            font_size: '40sp'
        Spinner:
            id: graphList
            size_hint: None, None
            size: 1000, 44
            pos_hint: {'center': (.5, .5)}
            text: 'Type of Graph'
        Label:
            text: 'Location to Save Graph:'
            font_size: '40sp'
        TextInput:
            id: saveLocation
            multiline: False
            font_size:'50sp'
        Button:
            text: 'Download Graph'
            font_size:50
            on_press:  root.downloadGraph()
        Button:
            text: 'View Graph'
            font_size:50
            on_press:  root.viewGraph()
        Button:
            text: 'Back to Dashboard'
            font_size:50
            on_press: root.manager.current = 'dash'
<enterExpenses>:
    BoxLayout:
        orientation: 'vertical'

        Label:
            text: 'Enter Expense'
            font_size: '130sp'
        Spinner:
            id: categoryDropdown
            size_hint: None, None
            size: 1000, 44
            pos_hint: {'center': (.5, .5)}
            text: 'Category'
            on_text : root.updateSub()
        Spinner:
            id: subCategoryDropdown
            size_hint: None, None
            size: 1000, 44
            pos_hint: {'center': (.5, .5)}
            text: 'Sub-Category'
        Label:
            text: 'Date (mm/dd/yyyy):'
            font_size: '40sp'
        TextInput:
            id: dateInput
            multiline: False
            font_size:'50sp'
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

<deleteExpense>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Delete Expense'
            font_size: '130sp'
        Spinner:
            id: expenseList
            size_hint: None, None
            size: 1000, 44
            pos_hint: {'center': (.5, .5)}
            text: 'Select an expense to delete'
        Label:
            text: ''
        Button:
            text: 'Delete'
            font_size:50
            on_press: root.deleteExpense()
        Button:
            text: 'Back to Dashboard'
            font_size:50
            on_press: root.manager.current = 'dash'

""")
#function to display percent and total of pie chart pieces
def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d} )".format(pct, absolute)

def generateGraphs(location, timeInput, graphType):
    # get relevant information from the database for correct graph, return as array. also need to size figures
    if graphType == 'Pie Chart':
        # Data to plot
        labels =  ['Improvements/Upgrades', 'Social/Entertainment', 'Personal Care & Hygiene', 'Savings'] # need category or subcategory as label in array
        sizes = [215, 130, 245, 210] # need totaal for each type of expense for year or month
        colors = ['lightseagreen', 'moccasin', 'salmon', 'palevioletred']
        explode = (0.1, 0, 0, 0)  # explode 1st slice
                     # test path for debug C:\Users\payton\Desktop\testing
        # Plot
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct=lambda pct: func(pct, sizes), shadow=True, startangle=140)
        plt.title("Pie Chart")
        plt.axis('equal')
        plt.rcParams["figure.figsize"] = [30,15]

        if location != "":
            plt.savefig(location + "/" + "piechart.png")
            #success msg when graph has been generated
            popup = Popup(title='Success', content=Label(text='Success, your pie graph has been downloaded to your computer. \n \n To close this popup click anywhere.'),size=(700, 600), size_hint=(None, None))
            popup.open()
        else:
            matplotlib.pyplot.ion()
            plt.show()
            matplotlib.pyplot.ioff()

    elif graphType == 'Histogram':
        x = [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,49,50,100]
        num_bins = len(x)
        n, bins, patches = plt.hist(x, num_bins, facecolor='teal', alpha=0.5)
        plt.title('Histogram Graph')
        plt.xlabel('Expense Amount')
        plt.rcParams["figure.figsize"] = [30,15]

        if location != "":
            plt.savefig(location + "/" + "Histogram.png")
            #success msg when graph has been generated
            popup = Popup(title='Success', content=Label(text='Success, your histogram has been downloaded to your computer. \n \n To close this popup click anywhere.'),size=(700, 600), size_hint=(None, None))
            popup.open()
        else:
            matplotlib.pyplot.ion()
            plt.show()
            matplotlib.pyplot.ioff()

    elif graphType == 'Line Graph':
        y = [450, 12345, 8645, 34553, 55677, 1233, 466, 764, 8900, 4342,1233, 89 ]
        x = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        plt.plot(x, y, color='cornflowerblue')
        plt.xlabel('Month') #or day or week???
        plt.ylabel('Expense')
        plt.title('Line Graph')
        plt.rcParams["figure.figsize"] = [30,15]

        if location != "":
            plt.savefig(location + "/" + "lineGraph.png")
            #success msg when graph has been generated
            popup = Popup(title='Success', content=Label(text='Success, your line graph has been downloaded to your computer. \n \n To close this popup click anywhere.'),size=(700, 600), size_hint=(None, None))
            popup.open()
        else:
            matplotlib.pyplot.ion()
            plt.show()
            matplotlib.pyplot.ioff()

    elif graphType == 'Bar Graph':
        category = ('Improvements/Upgrades', 'Social/Entertainment', 'Personal Care & Hygiene', 'Savings')
        y_pos = np.arange(len(category))

        x = [300,908,2000,123]

        plt.bar(y_pos, x, align='center', alpha=0.5, color = 'rosybrown')
        plt.xticks(y_pos, category)
        plt.ylabel('Expense Amount')
        plt.title('Bar Chart')
        plt.rcParams["figure.figsize"] = [30,15]

        if location != "":
            plt.savefig(location + "/" + "barGraph.png")
            #success msg when graph has been generated
            popup = Popup(title='Success', content=Label(text='Success, your bar graph has been downloaded to your computer. \n \n To close this popup click anywhere.'),size=(700, 600), size_hint=(None, None))
            popup.open()
        else:
            matplotlib.pyplot.ion()
            plt.show()
            matplotlib.pyplot.ioff()
            # Declare screens
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
                    # set user id
                    # set password
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

    def logoutUser(self):
        #clear global variables
        sm.current = 'login'

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
    def __init__(self, **kwargs):
         super(Graphs, self).__init__(**kwargs)
         # set values for drop down list
         self.ids.timeList.values = ['Month', 'Year']
         self.ids.graphList.values = ['Pie Chart', 'Histogram', 'Line Graph', 'Bar Graph']
    def downloadGraph(self):
        # get location input
         location = self.ids.saveLocation.text
         # get month input
         timeInput = self.ids.timeList.text
         #get graph input
         graphType = self.ids.graphList.text

         # check that all fields are filled out
         if timeInput != 'Month or Year' and graphType != 'Type of Graph' and location != '':
             #check the path exists
             if os.path.exists(location):
                loc = location.replace("\\",'/')
                generateGraphs(loc, timeInput, graphType)
             else:
                 #error msg when location does not exist
                popup = Popup(title='Error', content=Label(text='Error, location is not valid, please try again. \n \n To close this popup click anywhere.'),size=(700, 600), size_hint=(None, None))
                popup.open()
         else:
             #error msg when all fields have not been filled out
            popup = Popup(title='Error', content=Label(text='Error, all fields must be filled out. \n \n To close this popup click anywhere.'),size=(700, 600), size_hint=(None, None))
            popup.open()
    def viewGraph(self):
         # get month input
         timeInput = self.ids.timeList.text
         #get graph input
         graphType = self.ids.graphList.text

         # check that all fields are filled out
         if timeInput != 'Month or Year' and graphType != 'Type of Graph':
                generateGraphs("", timeInput, graphType)
         else:
             #error msg when all fields have not been filled out
            popup = Popup(title='Error', content=Label(text='Error, all fields must be filled out. \n \n To close this popup click anywhere.'),size=(700, 600), size_hint=(None, None))
            popup.open()
    pass

class deleteExpense(Screen):
     def __init__(self, **kwargs):
         super(deleteExpense, self).__init__(**kwargs)
         #call function to get list of strings of expense line items
         self.ids.expenseList.values= ['1000: Personal Care & Hygiene - Cosmetic $150', '1001: Personal Care & Hygiene - Cosmetic $100', '1002: Personal Care & Hygiene: Cosmetic $3000']

     def deleteExpense(self):
         expense = self.ids.expenseList.text

         if expense != 'Select an expense to delete':
            deleteSuccessful = True # call function to delete expense. return true if successful

            temp = expense.split(':')

            transactionId = temp[0]

            if(deleteSuccessful):
            # msg when enter expense is deleted successful
                popup = Popup(title='Success', content=Label(text='Success, expense has been deleted. \n \n To close this popup click anywhere.'),size=(700, 600), size_hint=(None, None))
                popup.open()
            else:
                 #error msg when delete expense is not successful
                popup = Popup(title='Error', content=Label(text='Error, delete expense was not successful, please try again. \n \n To close this popup click anywhere.'),size=(700, 600), size_hint=(None, None))
                popup.open()
         else:
              #error msg when delete expense has bot been selected
            popup = Popup(title='Error', content=Label(text='Error, please select an expense to delete. \n \n To close this popup click anywhere.'),size=(700, 600), size_hint=(None, None))
            popup.open()
     pass

class enterExpenses(Screen):
     def __init__(self, **kwargs):
         super(enterExpenses, self).__init__(**kwargs)
         self.ids.categoryDropdown.values = ['Improvements/Upgrades', 'Social/Entertainment', 'Personal Care & Hygiene', 'Savings']

     def updateSub(self):
         category = self.ids.categoryDropdown.text

         # populate subcategory when user chooses a category
         if category == 'Improvements/Upgrades':
             self.ids.subCategoryDropdown.values = ['Home','Automotive','Electronic','Other']
         elif category == 'Social/Entertainment':
             self.ids.subCategoryDropdown.values = ['Dining Out','Special Events','Games', 'Gifts','Subscriptions','Other']
         elif category == 'Personal Care & Hygiene':
             self.ids.subCategoryDropdown.values = ['Cosmetics', 'Clothes', 'Toiletries', 'Memberships', 'Other']
         elif category ==  'Savings':
             self.ids.subCategoryDropdown.values = ['Emergency Fund', 'Asset Deposits', 'Vacations', 'Appliances', 'Other']

     def addExpense(self):

         #get value for category
         category = self.ids.categoryDropdown.text

         #get value for sub-category
         subcategory = self.ids.subCategoryDropdown.text

         expenseAmt = self.ids.expenseAmt.text

         date = self.ids.dateInput.text

         #printing for error checking
         #print(category)
         #print(subcategory)
         #print(expenseAmt)

         # use regex to check if date is in the right format
         if(re.search("[\d]{1,2}/[\d]{1,2}/[\d]{4}",date)):
             if(category == 'Category' or subcategory == 'Sub-Category' or expenseAmt == ''):
              #error msg when field is empty
                    popup = Popup(title='Error', content=Label(text='Error, all fields must be filled out, please enter again. \n \n To close this popup click anywhere.'),size=(700, 600), size_hint=(None, None))
                    popup.open()
             else:
                    if(expenseAmt.isdigit()):
                            expenseSuccessful = True #function call to enter in an expense
                            if(expenseSuccessful):
                                # msg when enter expense is  successful
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
         else:
             #error msg when date it not properly formatted
             popup = Popup(title='Error', content=Label(text='Error, date must be formatted as mm/dd/yyyy, please enter again. \n \n To close this popup click anywhere.'),size=(700, 600), size_hint=(None, None))
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
sm.add_widget(deleteExpense(name='delete'))


class TestApp(App):

    def build(self):
        self.title = 'FootPrints'
        return sm

if __name__ == '__main__':
   TestApp().run()
