#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from graphics import *

adder= ""
eq = ""
_list = []
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






while True:
    
    
    click = win.getMouse()
   
    if click.getY()>500:  
              
       continue

    elif click.getX()<450 and 100<click.getY()<400 or click.getX()<300 and click.getY()<100:
        
        val = value_turner(click)
        adder += val
        inputText.setText(adder)
       
        
    elif 150<click.getX()<300 and 400<click.getY()<500:
        
        adder += " +/- "
        inputText.setText(adder)

    elif 300<click.getX()<450 and 400<click.getY()<500:
        
        adder += " % "
        inputText.setText(adder)

    elif 450<click.getX()<600 and 400<click.getY()<500:
        
        adder += " / "
        inputText.setText(adder)        

    elif 450<click.getX()<600 and 300<click.getY()<400:
        
        adder += " * "
        inputText.setText(adder)

    elif 450<click.getX()<600 and 200<click.getY()<300:
        
        adder += " - "
        inputText.setText(adder)

    elif 450<click.getX()<600 and 100<click.getY()<200:
        
        adder += " + "
        inputText.setText(adder)

    elif 300<click.getX()<450 and click.getY()<100:
        
        adder += " ** "
        inputText.setText(adder)

    elif click.getX()<150 and 400<click.getY()<500:
        
        adder = ""
        inputText.setText("0")

    elif 450<click.getX()<600 and click.getY()<100:
        
        if "+/-" in adder:
            adder = adder.replace("+/-", "*(-1)")
        
        elif "**" in adder:
            adder = adder.replace("**", "**2")
                
            
        result = eval(adder)
        check = isinstance(result, int)
        adder = str(result)
        if check==True:
            result = int(result)
            inputText.setText(result)
        else:
            inputText.setText(result)


win.getMouse()
win.close()