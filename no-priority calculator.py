from graphics import *
from math import pow

adder= ""
operands = ""
exp = ""
base = ""
win = GraphWin("Calculator",600,600)
win.setCoords(0.0, 0.0, 600.0, 600.0)

inputText = Entry(Point(300,550), 20)
inputText.setText("0")
inputText.draw(win)


def rectangleMaker():
    
    for x in range(0,601,150):
        for y in range(100,501,100):
                    
            rect= Rectangle(Point(x,y), Point(600,500))
            rect.draw(win)

    rect1 = Rectangle(Point(0,100), Point(300,0))
    rect1.draw(win)
    rect2 = Rectangle(Point(300,100), Point(450,0))
    rect2.draw(win)
    rect3 = Rectangle(Point(450,100), Point(600,0))
    rect3.draw(win)
    rect4 = Rectangle(Point(0,500), Point(600,600))   
    rect4.draw(win)
  
    
def text_printer():
    t=0
    text = ["1","4","7","AC","2","5","8","+/-","3","6","9","%","+","-","x","/"]
    Text(Point(375,50), "**").draw(win)
    Text(Point(525,50), "=").draw(win)
    Text(Point(150,50), "0").draw(win)
   
    while t<16:
        for x in range(75,601,150):
            for y in range(150,501,100):
                
                Text(Point(x,y), text[t]).draw(win)
                
                t+=1
                   

rectangleMaker()
text_printer()


def value_turner(click):
    
    
    if click.getX()<300 and click.getY()<100:
        
        val = "0"
        return val
    
    elif click.getX()<150 and 100<click.getY()<200:
        
        val = "1"
        return val        
        
    elif 150<click.getX()<300 and 100<click.getY()<200:
        
        val = "2"
        return val  
    
    elif 300<click.getX()<450 and 100<click.getY()<200:
        
        val = "3"
        return val

    elif click.getX()<150 and 200<click.getY()<300:
        
        val = "4"
        return val

    elif 150<click.getX()<300 and 200<click.getY()<300:
        
        val = "5"
        return val

    elif 300<click.getX()<450 and 200<click.getY()<300:
        
        val = "6"
        return val

    elif click.getX()<150 and 300<click.getY()<400:
        
        val = "7"
        return val

    elif 150<click.getX()<300 and 300<click.getY()<400:
        
        val = "8"
        return val

    elif 300<click.getX()<450 and 300<click.getY()<400:
        
        val = "9"
        return val



def eq_solver(adder,base,exp):
  
    try:
        result = eval(adder)
        check = bool(float(result)==int(result))
        adder = str(result)
        if check==True:
            result = int(result)
            inputText.setText(result)
        else:
            inputText.setText(result)
    except:
        v1=eval(base)
        v2=eval(exp)
        result2 = pow(v1,v2)
        adder = str(result2)
        check = bool(float(result2)==int(result2))
        if check==True:
            result2 = int(result2)
            inputText.setText(result2)

        else:
            inputText.setText(result2)           
        exp = ""
        base = ""
    
    return adder




while True:
    
    
    click = win.getMouse()
   
    if click.getY()>500:  
              
       continue

    elif click.getX()<450 and 100<click.getY()<400 or click.getX()<300 and click.getY()<100: # operands

        val = value_turner(click)
        adder += val
        operands += val
        inputText.setText(operands)
        
        if "a" in adder:
            exp += operands
        
    elif 150<click.getX()<300 and 400<click.getY()<500: # +/-
    
        try:
            adder += "*(-1)"
            eq_solver(adder,base,exp)
            operands = ""
        except:
            adder = ""
            inputText.setText("0")
            
    elif 300<click.getX()<450 and 400<click.getY()<500: # %   
        
        try:            
            adder = eq_solver(adder,base,exp)
            adder += " % "
            
        except:
            adder = ""
            inputText.setText("0")
        
        operands = ""

    elif 450<click.getX()<600 and 400<click.getY()<500: # /   
        
        try:       
            adder = eq_solver(adder,base,exp)
            adder += " / "
     
        except:
            adder = ""
            inputText.setText("0")
            
        operands = ""

    elif 450<click.getX()<600 and 300<click.getY()<400: # x
        
        try:            
            adder = eq_solver(adder,base,exp)
            adder += " * "

        except:    
            adder = ""
            inputText.setText("0")
            
        operands = ""

    elif 450<click.getX()<600 and 200<click.getY()<300: # -

        try:            
            adder = eq_solver(adder,base,exp)
            adder += " - "
            
        except:
            adder = ""
            inputText.setText("0")
            
        operands = ""
        
    elif 450<click.getX()<600 and 100<click.getY()<200: # +
        
        try:            
            adder = eq_solver(adder,base,exp)
            adder += " + "
     
        except:
            adder = ""
            inputText.setText("0")
            
        operands = ""
        
    elif 300<click.getX()<450 and click.getY()<100: # **
        
        try:            
            adder = eq_solver(adder,base,exp)
            adder += " a "
            list1 = list(adder.split(" "))
            base += list1[0]
            
        except:
            adder = ""
            inputText.setText("0")
            
        operands = ""

    elif click.getX()<150 and 400<click.getY()<500: # AC
        
        adder = ""
        operands = ""
        exp = ""
        base = ""
        inputText.setText("0")
            
    elif 450<click.getX()<600 and click.getY()<100: # =
         
        try:
            result = eval(adder)
            check = bool(float(result)==int(result))
            adder = str(result)
            operands = ""
            if check==True:
                result = int(result)
                inputText.setText(result)
            else:               
                inputText.setText(result)
            
        except:
            v1=eval(base)
            v2=eval(exp)
            result2 = pow(v1,v2)
            adder = str(result2)
            check = bool(float(result2)==int(result2))
            if check==True:
                result2 = int(result2)
                inputText.setText(result2)

            else:               
                inputText.setText(result2)
            exp = ""
            base = ""

win.getMouse()
win.close()