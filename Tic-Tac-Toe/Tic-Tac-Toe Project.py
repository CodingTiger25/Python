#-------------------------------------------------------------------------------
# Name:        Project 1 / Tic-Tac- Toe
# Purpose: Plays a game of Tic-Tac-Toe
#
# Author:      Tony Padmore
#
# Created:     04/30/2014
# # Comment : I am happy I was able to get the matrix part going. There is most likely a cleaner
# # But I will expand on this project at another time.
# # Hardest part was using a list in list
#-------------------------------------------------------------------------------

# Creates the the position for the game
def main():
    from graphics import GraphWin, Circle, Line, Point, Text, Rectangle, Entry
    win = GraphWin('Tic-Tac-Toe',600,600)
    win.setBackground('yellow')
    win.setCoords(-2,-2,9,11)
    board = [[1,2,3], [4,5,6], [7,8,9]]

    # Creates the Gameboard
    def Table():
        title = Text(Point(3.5,10.5),'Tic - Tac - Toe')
        title.draw(win)
        box_1 = Rectangle(Point(0,0),Point(3,3))
        box_1.setFill('white')
        box_1.move(-1,0)
        box_1.draw(win)

        box_2 = box_1.clone()
        box_2.move(3,0)

        box_2.draw(win)

        box_3 = box_1.clone()
        box_3.move(6,0)
        box_3.draw(win)

        box_4 = box_1.clone()
        box_4.move(0,3)
        box_4.draw(win)

        box_5 = box_1.clone()
        box_5.move(0,6)
        box_5.draw(win)

        box_6 = box_1.clone()
        box_6.move(3,3)
        box_6.draw(win)

        box_7 = box_1.clone()
        box_7.move(3,6)
        box_7.draw(win)

        box_8 = box_1.clone()
        box_8.move(6,3)
        box_8.draw(win)

        box_9 = box_1.clone()
        box_9.move(6,6)
        box_9.draw(win)

    # Makes X's inside box
    def X_make(p2):
        upper = p2.getX()
        lower = p2.getY()
        # Lower left Box
        if(p2.getX() < 2 and p2.getY() < 3):
            X_mark = Line(Point(-.5,2.5),Point(1.5,.5))
            X_mark2 = Line(Point(-.5,.5),Point(1.5,2.5))
            X_mark.setOutline('blue')
            X_mark.setWidth(3)
            X_mark2.setOutline('blue')
            X_mark2.setWidth(3)
            X_mark.draw(win)
            X_mark2.draw(win)
            board[2][0] = 'X'
        # Left column middle box
        elif (p2.getX() < 2 and p2.getY() < 6):
            X_mark = Line(Point(-0.8,5.5),Point(1.5,3.5))
            X_mark2 = Line(Point(-.8,3.5),Point(1.5,5.5))
            X_mark.setOutline('blue')
            X_mark.setWidth(3)
            X_mark2.setOutline('blue')
            X_mark2.setWidth(3)
            X_mark.draw(win)
            X_mark2.draw(win)
            board[1][0] = 'X'
        # Top left box
        elif (p2.getX() < 2 and p2.getY() < 9):
            X_mark = Line(Point(-.8,8.5),Point(1.5,6.5))
            X_mark2 = Line(Point(-.8,6.5),Point(1.5,8.5))
            X_mark.setOutline('blue')
            X_mark.setWidth(3)
            X_mark2.setOutline('blue')
            X_mark2.setWidth(3)
            X_mark.draw(win)
            X_mark2.draw(win)
            board[0][0] = 'X'
        # Bottom row middle box
        elif (p2.getX() < 5 and p2.getY() < 3):
            X_mark = Line(Point(2.5,2.5),Point(4.5,.5))
            X_mark2 = Line(Point(4.5,2.5),Point(2.5,.5))
            X_mark.setOutline('blue')
            X_mark.setWidth(3)
            X_mark2.setOutline('blue')
            X_mark2.setWidth(3)
            X_mark.draw(win)
            X_mark2.draw(win)
            board[2][1] = 'X'
        # Middle row middle box
        elif (p2.getX() < 5 and p2.getY() < 6):
            X_mark = Line(Point(2.5,5.5),Point(4.5,3.5))
            X_mark2 = Line(Point(2.5,3.5),Point(4.5,5.5))
            X_mark.setOutline('blue')
            X_mark.setWidth(3)
            X_mark2.setOutline('blue')
            X_mark2.setWidth(3)
            X_mark.draw(win)
            X_mark2.draw(win)
            board[1][1] = 'X'
        # Top row middle box
        elif (p2.getX() < 5 and p2.getY() < 9):
            X_mark = Line(Point(2.5,8.5),Point(4.5,6.5))
            X_mark2 = Line(Point(4.5,8.5),Point(2.5,6.5))
            X_mark.setOutline('blue')
            X_mark.setWidth(3)
            X_mark2.setOutline('blue')
            X_mark2.setWidth(3)
            X_mark.draw(win)
            X_mark2.draw(win)
            board[0][1] = 'X'
        # Bottom row rightmost box
        elif (p2.getX() < 8 and p2.getY() < 3):
            X_mark = Line(Point(5.5,.5),Point(7.5,2.5))
            X_mark2 = Line(Point(5.5,2.5),Point(7.5,.5))
            X_mark.setOutline('blue')
            X_mark.setWidth(3)
            X_mark2.setOutline('blue')
            X_mark2.setWidth(3)
            X_mark.draw(win)
            X_mark2.draw(win)
            board[2][2] = 'X'
        # Right column middle box
        elif (p2.getX() < 8 and p2.getY() < 6):
            X_mark = Line(Point(5.5,3.5),Point(7.5,5.5))
            X_mark2 = Line(Point(5.5,5.5),Point(7.5,3.5))
            X_mark.setOutline('blue')
            X_mark.setWidth(3)
            X_mark2.setOutline('blue')
            X_mark2.setWidth(3)
            X_mark.draw(win)
            X_mark2.draw(win)
            board[1][2] = 'X'
        # right column top box
        elif (p2.getX() < 8 and p2.getY() < 9):
            X_mark = Line(Point(5.5,8.5),Point(7.5,6.5))
            X_mark2 = Line(Point(5.5,6.5),Point(7.5,8.5))
            X_mark.setOutline('blue')
            X_mark.setWidth(3)
            X_mark2.setOutline('blue')
            X_mark2.setWidth(3)
            X_mark.draw(win)
            X_mark2.draw(win)
            board[0][2] = 'X'

    # Makes Circles inside box
    def O_make(p1):
        # Left column bottom Box
        if (p1.getX() < 2 and p1.getY() < 3):
            Circ = Circle(Point(.5,1.5),1)
            board[2][0] = 'O'
            Circ.setFill('red')
            Circ.draw(win)
        # left column second Box
        elif (p1.getX() < 2 and p1.getY() < 6):
            Circ = Circle(Point(.5,4.5),1)
            board[1][0] = 'O'
            Circ.setFill('red')
            Circ.draw(win)
        # Left column top box
        elif (p1.getX() < 2 and p1.getY() < 9):
            Circ = Circle(Point(.5,7.5),1)
            board[0][0] = 'O'
            Circ.setFill('red')
            Circ.draw(win)
        # Middle column bottom box
        elif (p1.getX() < 5 and p1.getY() < 3):
            Circ = Circle(Point(3.5,1.5),1)
            Circ.setFill('red')
            Circ.draw(win)
            board[2][1] = 'O'
        # middle column middle box
        elif (p1.getX() < 5 and p1.getY() < 6):
            Circ = Circle(Point(3.5,4.5),1)
            Circ.setFill('red')
            Circ.draw(win)
            board[1][1] = 'O'
        # middle column top box
        elif (p1.getX() < 5 and p1.getY() < 9):
            Circ = Circle(Point(3.5,7.5),1)
            Circ.setFill('red')
            Circ.draw(win)
            board[0][1] = 'O'
        # right column bottom box
        elif (p1.getX() < 8 and p1.getY() < 3):
            Circ = Circle(Point(6.5,1.5),1)
            Circ.setFill('red')
            Circ.draw(win)
            board[2][2] = 'O'
        # right column middle box
        elif (p1.getX() < 8 and p1.getY() < 6):
            Circ = Circle(Point(6.5,4.5),1)
            Circ.setFill('red')
            Circ.draw(win)
            board[1][2] = 'O'
        # right column top box
        elif (p1.getX() < 8 and p1.getY() < 9):
            Circ = Circle(Point(6.5,7.5),1)
            Circ.setFill('red')
            Circ.draw(win)
            board[0][2] = 'O'

    # Total score
    def winner(o,x):
       return o == 1 or x == 1

    # quit button
    def leave():
        quit_button = Rectangle(Point(-1,-2),Point(1,-1))
        quit_text = Text(Point(-.5,-1.5),'Quit')
        quit_button.setFill('white')
        quit_button.draw(win)
        quit_text.draw(win)

    # Plays the program
    def action():
        O_player = 0
        X_player = 0
        # This will count how many times the mouse has been clicked on the window
        Mouse_click = 0

        vert_line1 = Line(Point(.5,0),Point(.5,9))
        vert_line1.setWidth(3)
        vert_line2 = Line(Point(3.5,0),Point(3.5,9))
        vert_line2.setWidth(3)
        vert_line3 = Line(Point(6.5,0), Point(6.5,9))
        vert_line3.setWidth(3)

        hori_line1 = Line(Point(-1,1.5),Point(8,1.5))
        hori_line1.setWidth(3)
        hori_line2 = Line(Point(-1,4.5), Point(8,4.5))
        hori_line2.setWidth(3)
        hori_line3 = Line(Point(-1,7.5), Point(8,7.5))
        hori_line3.setWidth(3)

        diag_line1 = Line(Point(-1,0),Point(8,9))
        diag_line1.setWidth(3)
        diag_line2 = Line(Point(-1,9),Point(8,0))
        diag_line2.setWidth(3)

        while not winner(O_player,X_player):
            leave()
            p1_turn = Text(Point(5,-.5),'Player 1\'s turn')
            p1_turn.draw(win)
            p1 = win.getMouse()
            Mouse_click += 1
            O_make(p1)

            # Checks for O's Vertically
            if board[2][0] == 'O':
                if board[1][0] == 'O':
                    if board[0][0] == 'O':
                        vert_line1.draw(win)
                        O_player += 1
                        win_message = Text(Point(3.5,9.5),'Player 1 wins!!!')
                        win_message.draw(win)
                        quit_message = Text(Point(5,-1.5),'Click the quit button to leave.')
                        quit_message.draw(win)
                        win.getMouse()
                        win.close()
                        break

            elif board[0][1] == 'O':
                if board[1][1] == 'O':
                    if board[2][1] == 'O':
                        vert_line2.draw(win)
                        O_player += 1
                        win_message = Text(Point(3.5,9.5),'Player 1 wins!!!')
                        win_message.draw(win)
                        quit_message = Text(Point(5,-1.5),'Click the quit button to leave.')
                        quit_message.draw(win)
                        win.getMouse()
                        win.close()
                        break

            elif board[0][2] == 'O':
                if board[1][2] == 'O':
                    if board[2][2] == 'O':
                        vert_line3.draw(win)
                        O_player += 1
                        win_message = Text(Point(3.5,9.5),'Player 1 wins!!!')
                        win_message.draw(win)
                        quit_message = Text(Point(5,-1.5),'Click the quit button to leave.')
                        quit_message.draw(win)
                        win.getMouse()
                        win.close()
                        break

            # Checks for O's horizontally
            if board[2][0] == 'O':
                if board[2][1] == 'O':
                    if board[2][2] == 'O':
                        hori_line1.draw(win)
                        O_player += 1
                        win_message = Text(Point(3.5,9.5),'Player 1 wins!!!')
                        win_message.draw(win)
                        quit_message = Text(Point(5,-1.5),'Click the quit button to leave.')
                        quit_message.draw(win)
                        win.getMouse()
                        win.close()
                        break
            elif board[1][0] == 'O':
                if board[1][1] == 'O':
                    if board[1][2] == 'O':
                        hori_line2.draw(win)
                        O_player += 1
                        win_message = Text(Point(3.5,9.5),'Player 1 wins!!!')
                        win_message.draw(win)
                        quit_message = Text(Point(5,-1.5),'Click the quit button to leave.')
                        quit_message.draw(win)
                        win.getMouse()
                        win.close()
                        break
            elif board[0][0] == 'O':
                if board[0][1] == 'O':
                    if board[0][2] == 'O':
                        hori_line3.draw(win)
                        O_player += 1
                        win_message = Text(Point(3.5,9.5),'Player 1 wins!!!')
                        win_message.draw(win)
                        quit_message = Text(Point(5,-1.5),'Click the quit button to leave.')
                        quit_message.draw(win)
                        win.getMouse()
                        win.close()
                        break

            # Checks for O's diagonally
            if board[2][0] == 'O':
                if board[1][1] == 'O':
                    if board[0][2] == 'O':
                        diag_line1.draw(win)
                        O_player += 1
                        win_message = Text(Point(3.5,9.5),'Player 1 wins!!!')
                        win_message.draw(win)
                        quit_message = Text(Point(5,-1.5),'Click the quit button to leave.')
                        quit_message.draw(win)
                        win.getMouse()
                        win.close()
                        break
            elif board[0][0] == 'O':
                if board[1][1] == 'O':
                    if board[2][2] == 'O':
                        diag_line2.draw(win)
                        O_player += 1
                        win_message = Text(Point(3.5,9.5),'Player 1 wins!!!')
                        win_message.draw(win)
                        quit_message = Text(Point(5,-1.5),'Click the quit button to leave.')
                        quit_message.draw(win)
                        win.getMouse()
                        win.close()
                        break
            # Checking to see if nobody won, which leads to a tie
            if Mouse_click == 9:
                Tie_Message = Text(Point(3.5,9.5),'It\'s a Tie!!!')
                Tie_Message.draw(win)
                quit_message = Text(Point(5,-1.5),'Click the quit button to leave.')
                quit_message.draw(win)
                win.getMouse()
                win.close()
                break


            p1_turn.undraw()
            p2_turn = Text(Point(7,-.5),'Player 2\'s turn')
            p2_turn.draw(win)

            p2 = win.getMouse()
            Mouse_click += 1
            X_make(p2)
            p2_turn.undraw()
            # Checks X's veritcally
            if board[2][0] == 'X':
                if board[1][1] == 'X':
                    if board[0][0] == 'X':
                        vert_line1.draw(win)
                        X_player += 1
                        win_message = Text(Point(3.5,9.5),'Player 2 wins!!!')
                        win_message.draw(win)
                        quit_message = Text(Point(5,-1.5),'Click the quit button to leave.')
                        quit_message.draw(win)
                        win.getMouse()
                        win.close()
                        break
            elif board[2][1] == 'X':
                if board[1][1] == 'X':
                    if board[0][1] == 'X':
                        vert_line2.draw(win)
                        win_message = Text(Point(3.5,9.5),'Player 2 wins!!!')
                        win_message.draw(win)
                        quit_message = Text(Point(5,-1.5),'Click the quit button to leave.')
                        quit_message.draw(win)
                        win.getMouse()
                        win.close()
                        break
            elif board[2][2] == 'X':
                if board[1][2] == 'X':
                    if board[0][2] == 'X':
                        vert_line3.draw(win)
                        X_player += 1
                        win_message = Text(Point(3.5,9.5),'Player 2 wins!!!')
                        win_message.draw(win)
                        quit_message = Text(Point(5,-1.5),'Click the quit button to leave.')
                        quit_message.draw(win)
                        win.getMouse()
                        win.close()
                        break
            # Checks X's Horizontally
            if board[2][0] == 'X':
                if board[2][1] == 'X':
                    if board[2][2] == 'X':
                        hori_line1.draw(win)
                        X_player += 1
                        win_message = Text(Point(3.5,9.5),'Player 2 wins!!!')
                        win_message.draw(win)
                        quit_message = Text(Point(5,-1.5),'Click the quit button to leave.')
                        quit_message.draw(win)
                        win.getMouse()
                        win.close()
                        break
            elif board[1][0] == 'X':
                if board[1][1] == 'X':
                    if board[1][2] == 'X':
                        hori_line2.draw(win)
                        X_player += 1
                        win_message = Text(Point(3.5,9.5),'Player 2 wins!!!')
                        win_message.draw(win)
                        quit_message = Text(Point(5,-1.5),'Click the quit button to leave.')
                        quit_message.draw(win)
                        win.getMouse()
                        win.close()
                        break
            elif board[0][0] == 'X':
                if board[0][1] == 'X':
                    if board[0][2] == 'X':
                        hori_line3.draw(win)
                        X_player += 1
                        win_message = Text(Point(3.5,9.5),'Player 2 wins!!!')
                        win_message.draw(win)
                        quit_message = Text(Point(5,-1.5),'Click the quit button to leave.')
                        quit_message.draw(win)
                        win.getMouse()
                        win.close()
                        break
            if board[2][0] == 'X':
                if board[1][1] == 'X':
                    if board[0][2] == 'X':
                        diag_line1.draw(win)
                        X_player += 1
                        win_message = Text(Point(3.5,9.5),'Player 2 wins!!!')
                        win_message.draw(win)
                        quit_message = Text(Point(5,-1.5),'Click the quit button to leave.')
                        quit_message.draw(win)
                        win.getMouse()
                        win.close()
                        break
            elif board[0][0] == 'X':
                if board[1][1] == 'X':
                    if board[2][2] == 'X':
                        diag_line2.draw(win)
                        X_player += 1
                        win_message = Text(Point(3.5,9.5),'Player 2 wins!!!')
                        win_message.draw(win)
                        quit_message = Text(Point(5,-1.5),'Click the quit button to leave.')
                        quit_message.draw(win)
                        win.getMouse()
                        win.close()
                        break

    Table()
    action()
main()
