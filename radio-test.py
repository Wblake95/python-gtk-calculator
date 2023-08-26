import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Calculator(Gtk.Window):
    def __init__(self):
        super().__init__(title="Calculator")
        self.set_border_width(10)

        # Header bar and exit button
        headerBar = Gtk.HeaderBar()
        headerBar.set_show_close_button(True)
        headerBar.props.title = "Calculator"
        self.set_titlebar(headerBar)

        # All the buttons
        # Numbers
        button1 = Gtk.Button(label="1")
        button1.connect("clicked", self.clickedButton1)
        button2 = Gtk.Button(label="2")
        button2.connect("clicked", self.clickedButton2)
        button3 = Gtk.Button(label="3")
        button3.connect("clicked", self.clickedButton3)
        button4 = Gtk.Button(label="4")
        button4.connect("clicked", self.clickedButton4)
        button5 = Gtk.Button(label="5")
        button5.connect("clicked", self.clickedButton5)
        button6 = Gtk.Button(label="6")
        button6.connect("clicked", self.clickedButton6)
        button7 = Gtk.Button(label="7")
        button7.connect("clicked", self.clickedButton7)
        button8 = Gtk.Button(label="8")
        button8.connect("clicked", self.clickedButton8)
        button9 = Gtk.Button(label="9")
        button9.connect("clicked", self.clickedButton9)

        # Zero and sign
        button0 = Gtk.Button(label="0")
        button0.connect("clicked", self.clickedButton0)
        buttonSign = Gtk.Button(label="-/+")
        # self.buttonSign.connect("clicked", self.clickedSign)

        # Operator buttons
        radioMultiply = Gtk.RadioButton.new_with_label_from_widget(None, label="x")
        radioMultiply.connect("toggled", self.button_toggled, "1")
        radioDivide = Gtk.RadioButton.new_with_label_from_widget(radioMultiply, label="/")
        radioDivide.connect("toggled", self.button_toggled, "2")
        radioAdd = Gtk.RadioButton.new_with_label_from_widget(radioMultiply, label="+")
        radioAdd.connect("toggled", self.button_toggled, "3")
        radioSubtract = Gtk.RadioButton.new_with_label_from_widget(radioMultiply, label="-")
        radioSubtract.connect("toggled", self.button_toggled, "4")

        # Enter and clear buttons
        buttonEnter = Gtk.Button(label="=")
        buttonEnter.connect("clicked", self.clickedEnter)
        buttonClear = Gtk.Button(label="c")
        buttonClear.connect("clicked", self.clickedClear)

        # Entry field
        entry = Gtk.Entry()
        entry.set_text("")
        entry1 = Gtk.Entry()
        entry1.set_text("")

        # Organizing the application buttons and entry field
        grid = Gtk.Grid()
        grid.add(button7)
        grid.attach_next_to(entry, button1,Gtk.PositionType.TOP,4,4)
        grid.attach_next_to(entry1, button1,Gtk.PositionType.TOP,4,4)
        grid.attach(button8,1,0,1,1)
        grid.attach(button9,2,0,1,1)
        grid.attach(button4,0,1,1,1)
        grid.attach(button5,1,1,1,1)
        grid.attach(button6,2,1,1,1)
        grid.attach(button1,0,2,1,1)
        grid.attach(button2,1,2,1,1)
        grid.attach(button3,2,2,1,1)

        grid.attach(buttonSign,0,3,1,1)
        grid.attach(button0,1,3,1,1)
        grid.attach(buttonFloat,2,3,1,1)

        grid.attach(radioMultiply,3,0,1,1)
        grid.attach(radioDivide,3,1,1,1)
        grid.attach(radioAdd,3,2,1,1)
        grid.attach(radioSubtract,3,3,1,1)
        grid.attach(buttonEnter,2,4,2,1)
        grid.attach(buttonClear,0,4,2,1)

        self.add(grid)

    # logic of buttons
    def clickedButton1(self, entry):
        text = self.entry.get_text()
        text += "1"
        self.entry.set_text(text)
    def clickedButton2 (self, entry):
        text = self.entry.get_text()
        text += "2"
        self.entry.set_text(text)
    def clickedButton3(self, entry):
        text = self.entry.get_text()
        text += "3"
        self.entry.set_text(text)
    def clickedButton4(self, entry):
        text = self.entry.get_text()
        text += "4"
        self.entry.set_text(text)
    def clickedButton5(self, entry):
        text = self.entry.get_text()
        text += "5"
        self.entry.set_text(text)
    def clickedButton6(self, entry):
        text = self.entry.get_text()
        text += "6"
        self.entry.set_text(text)
    def clickedButton7(self, entry):
        text = self.entry.get_text()
        text += "7"
        self.entry.set_text(text)
    def clickedButton8(self, entry):
        text = self.entry.get_text()
        text += "8"
        self.entry.set_text(text)
    def clickedButton9(self, entry):
        text = self.entry.get_text()
        text += "9"
        self.entry.set_text(text)
    def clickedButton0(self, entry):
        text = self.entry.get_text()
        text += "0"
        self.entry.set_text(text)

    def signCheck(self, text):
        check = ["x","/","+","-"]
        checkSign = self.entry.get_text()
        if checkSign[-1] in check:
            return False
        else:
            return True

    num1, num2 = 0,0
    operator = ""
    def button_toggled(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
    # def clickedMultiply(self, entry):
    #     if buttonMultiply.get_active(): self.operator = "m"
    # def clickedDivide(self, entry):
    #     if buttonDivide.get_active(): self.operator = "d"
    # def clickedAdd(self, entry):
    #     if buttonAdd.get_active(): self.operator = "a"
    # def clickedSubtract(self, entry):
    #     if buttonSubtract.get_active(): self.operator = "s"

    def clickedEnter(self, entry):
        match self.operator:
            case "m": self.entry.set_text(self.a[0]*self.a[1])
            case "d": self.entry.set_text(self.a[0]/self.a[1])
            case "a": self.entry.set_text(self.a[0]+self.a[1])
            case "s": self.entry.set_text(self.a[0]-self.a[1])
    def clickedClear(self, entry):
        self.entry.set_text("")
    # def clickedSign():

win = Calculator()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
