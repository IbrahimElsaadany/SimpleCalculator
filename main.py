from re import sub
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
class Calculator(Widget) :
    action = ObjectProperty(None)
    def typing(self,n) :
        if not self.last or not n.isdigit() and n!='.' :
            self.action.text+=n
            self.last=''
        else :
            self.action.text=n
            self.last=''
    def delete(self) :
        if not self.last :
            self.action.text=self.action.text[:-1]
        else :
            self.action.text=''
    def calc(self) :
        try :
            if '//' in self.action.text or '**' in self.action.text :
                raise SyntaxError
            result = eval(sub(r'(?<=[-+*/])*0+(?=[1-9])+','',self.action.text))
            print('d')
            self.action.text = str(int(result)) if result==int(result)  else str(round(result,15))
            self.last='='
        except :
            self.action.text=''
class Calc(App) :
    def build(self) :
        return Calculator()
if __name__=='__main__':
    Calc().run()