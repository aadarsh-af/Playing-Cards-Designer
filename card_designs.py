from turtle import *

# write("\n\nHello! Welcome to one of Aadarsh's many Logical Programs!")
# write("This program illustrates the designs we've seen in card games many times")
# write("What's your favorite design?")
# write("""1: Spades
# 2: Clubs
# 3: Diamonds
# 4: Hearts

# Enter your favorite desgin's index: """)
title("Card Designs - by Aadarsh")
fav = textinput('Type a number',
'''Hello! Welcome to one of Aadarsh's many Logical Programs!

This program illustrates the designs we've seen in card games
What's your favorite design?

                                            1: Spades
                                            2: Clubs
                                            3: Diamonds
                                            4: Hearts''')

if fav == "1": #Spades
    pensize(3)
    speed(3)
    up()
    goto(-10,-200)
    write("Coded by - Aadarsh Lalchandani",font=("Courier",15,"bold"),align="right")

    goto(0,0)
    down()

    color("black", "black")
    begin_fill()


    #the base
    left(0)
    forward(93)
    left(131)
    circle(-100,40)

    # first circle
    color("blue")
    shape("triangle")
    right(145)
    circle(40,180)

    #second line
    color("red")
    shape("circle")
    forward(150)

    #third line
    color("green")
    shape("arrow")
    left(110)
    forward(150)

    # fourth circle
    color("blue")
    shape("triangle")
    left(2)
    circle(40,180)

    #return path
    shape("turtle")
    color("black")
    right(152)
    circle(-100,40)
    write("SPADES",font=("Verdana",15,"bold"),align="right")
    end_fill()

    up()
    goto(12,-200)
    done()






elif fav == "2": #Clubs
    pensize(3)
    speed(3)
    up()
    goto(-10,-200)
    write("Coded by - Aadarsh Lalchandani",font=("Courier",15,"bold"),align="right")

    goto(0,0)
    down()

    up()
    goto(200,0)
    down()
    color("black", "black")
    begin_fill()

    #base
    left(0)
    forward(76)

    #second arc
    left(131)
    circle(-100,40)

    #third circle
    color("blue", "black")
    shape("triangle")
    right(150)
    circle(40,270)


    #fourth circle
    color("red", "black")
    shape("circle")
    right(165)
    circle(40,270)


    #fifth circle
    color("green", "black")
    shape("arrow")
    right(165)
    circle(40,270)


    #sixth arc
    shape("turtle")
    color("black", "black")
    right(152)
    circle(-100,40)
    write("CLUBS",font=("Verdana",15,"bold"),align="right")
    end_fill()

    up()
    goto(12,-200)
    done()





elif fav == "3": #Diamonds
    pensize(3)
    speed(3)
    up()
    goto(-10,-200)
    write("Coded by - Aadarsh Lalchandani",font=("Courier",15,"bold"),align="right")

    goto(0,0)
    down()

    left(283)
    begin_fill()
    shape("turtle")
    color("red","red")
    left(150)
    circle(-90,50)
    left(135)
    circle(-90,50)
    left(147)
    circle(-90,50)
    left(130)
    circle(-90,50)

    right(100)  # because it will help the text move out of the shape
    color("white","red")
    forward(20)
    color("red","red")

    write("DIAMONDS",font=("Verdana",15,"bold"),align="right")
    end_fill()
    color("white","white")

    up()
    goto(12,-200)
    done()





elif fav == "4": #Hearts
    pensize(3)
    speed(3)
    up()
    goto(-10,-200)
    write("Coded by - Aadarsh Lalchandani",font=("Courier",15,"bold"),align="right")

    goto(0,0)
    down()

    color("red", "red")
    begin_fill()

    #first line
    left(50)
    shape("turtle")
    forward(100)


    #second circle
    circle(40, 180)
    left(260)


    #third circle
    circle(40, 180)
    forward(100)


    #fourth line
    right(120)  # because it will help the text move out of the shape
    color("white","red")
    forward(20)
    color("red","white")
    write("HEARTS",font=("Verdana",15,"bold"),align="right")

    color("red","red")
    end_fill()

    up()
    goto(12,-200)
    done()










else:
    pensize(3)
    speed(3)
    up()
    goto(20,-50)
    write("Coded by - Aadarsh Lalchandani",font=("Courier",10,"bold"),align="right")


    #*********************************************CLUBS*****************************************
    up()
    goto(200,0)
    down()
    color("black", "black")
    begin_fill()

    #base
    left(0)
    forward(76)

    #second arc
    left(131)
    circle(-100,40)

    #third circle
    color("blue", "black")
    shape("triangle")
    right(150)
    circle(40,270)


    #fourth circle
    color("red", "black")
    shape("circle")
    right(165)
    circle(40,270)


    #fifth circle
    color("green", "black")
    shape("arrow")
    right(165)
    circle(40,270)


    #sixth arc
    shape("turtle")
    color("black", "black")
    right(152)
    circle(-100,40)
    write("CLUBS",font=("Verdana",15,"bold"),align="right")
    end_fill()

    #************************************HEARTS*****************************************
    up()
    goto(238,-200)
    down()
    color("red", "red")
    begin_fill()

    #first line
    left(182)
    forward(100)


    #second circle
    circle(40, 180)
    left(260)


    #third circle
    circle(40, 180)
    forward(100)


    #fourth line
    right(120)  # because it will help the text move out of the shape
    color("white","red")
    forward(20)
    color("red","white")
    write("HEARTS",font=("Verdana",15,"bold"),align="right")

    color("red","red")
    end_fill()


    #*************************************************SPADES*************************************************
    up()
    goto(-200,0)
    down()


    color("black", "black")
    begin_fill()


    #the base
    left(169)
    forward(93)
    left(131)
    circle(-100,40)

    # first circle
    color("blue")
    shape("triangle")
    right(145)
    circle(40,180)

    #second line
    color("red")
    shape("circle")
    forward(150)

    #third line
    color("green")
    shape("arrow")
    left(110)
    forward(150)

    # fourth circle
    color("blue")
    shape("triangle")
    left(2)
    circle(40,180)

    #return path
    shape("turtle")
    color("black")
    right(152)
    circle(-100,40)
    write("SPADES",font=("Verdana",15,"bold"),align="right")
    end_fill()

    #******************************************DIAMONDS*****************************************
    up()
    goto(-150,-200)
    down()

    left(57)
    begin_fill()
    color("red","red")
    left(150)
    circle(-90,50)
    left(135)
    circle(-90,50)
    left(147)
    circle(-90,50)
    left(130)
    circle(-90,50)

    right(100)  # because it will help the text move out of the shape
    color("white","red")
    forward(20)
    color("red","red")

    write("DIAMONDS",font=("Verdana",15,"bold"),align="right")
    end_fill()
    color("white","white")


    done()