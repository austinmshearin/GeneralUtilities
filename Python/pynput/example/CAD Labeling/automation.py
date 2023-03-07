from pynput import keyboard, mouse
import time
import string
from time import sleep

class automation():
    def __init__(self):
        # Stores combination of keys to start program
        self.COMBINATIONS = [
            {keyboard.Key.num_lock}
        ]
        # Initializes list of letters and controllers
        self.letters = list(string.ascii_uppercase)
        self.keyboard_controller = keyboard.Controller()
        self.mouse_controller = mouse.Controller()
        self.current = set()
        self.flag = False

    def execute(self):
        # row/col are iterating over rows and columns
        row = int(0)
        col = int(1)
        while row < self.num_rows: # iterate rows

            if self.flag == True:
                break
            
            while col < (self.num_cols + 1): # iterate columns
                if (row == 0) and (col==1): # do not do A1 until the end
                    col += 1
                    continue

                if self.flag == True:
                    break
                
                # Change text
                self.keyboard_controller.press(keyboard.Key.esc) # escape key
                self.keyboard_controller.release(keyboard.Key.esc)
                sleep(0.2)
                self.mouse_controller.position = self.right_position # move mouse to right position
                sleep(0.2)
                self.mouse_controller.click(mouse.Button.left) # click mouse
                sleep(0.2)
                self.mouse_controller.position = self.left_position # move mouse to left position
                sleep(0.2)
                self.mouse_controller.click(mouse.Button.left) # click mouse
                sleep(0.2)
                self.keyboard_controller.type("TEXTEDIT") # type textedit
                sleep(0.2)
                self.keyboard_controller.press(keyboard.Key.enter) # enter key
                self.keyboard_controller.release(keyboard.Key.enter)
                sleep(0.2)
                self.keyboard_controller.type(self.letters[row]+str(col)) # type label
                sleep(0.2)
                self.keyboard_controller.press(keyboard.Key.enter) # enter key
                self.keyboard_controller.release(keyboard.Key.enter)
                sleep(0.2)
                self.keyboard_controller.press(keyboard.Key.esc) # escape key
                self.keyboard_controller.release(keyboard.Key.esc)
                sleep(0.2)

                # Copy text
                self.mouse_controller.position = self.right_position # move mouse to right position
                sleep(0.2)
                self.mouse_controller.click(mouse.Button.left) # click mouse
                sleep(0.2)
                self.mouse_controller.position = self.left_position # move mouse to left position
                sleep(0.2)
                self.mouse_controller.click(mouse.Button.left) # click mouse
                sleep(0.2)
                self.keyboard_controller.type("COPY") # type copy
                sleep(0.2)
                self.keyboard_controller.press(keyboard.Key.enter) # enter key
                self.keyboard_controller.release(keyboard.Key.enter)
                sleep(0.2)
                self.mouse_controller.click(mouse.Button.left) # click mouse
                sleep(0.2)
                self.keyboard_controller.type(str((col-1)*self.col_spacing) + ",") # type x-coordinate and comma
                sleep(0.2)
                self.keyboard_controller.type(str(-1*row*self.row_spacing)) # type y-coordinate
                sleep(0.2)
                self.keyboard_controller.press(keyboard.Key.enter) # enter key
                self.keyboard_controller.release(keyboard.Key.enter)
                sleep(0.2)
                col += 1 # next column
            col = int(1) # restart columns
            row += 1 # next row

        if self.flag == False:
            # Fix A1
            self.keyboard_controller.press(keyboard.Key.esc)
            self.keyboard_controller.release(keyboard.Key.esc)
            sleep(0.2)
            self.mouse_controller.position = self.right_position
            sleep(0.2)
            self.mouse_controller.click(mouse.Button.left)
            sleep(0.2)
            self.mouse_controller.position = self.left_position
            sleep(0.2)
            self.mouse_controller.click(mouse.Button.left)
            sleep(0.2)
            self.keyboard_controller.type("TEXTEDIT")
            sleep(0.2)
            self.keyboard_controller.press(keyboard.Key.enter)
            self.keyboard_controller.release(keyboard.Key.enter)
            sleep(0.2)
            self.keyboard_controller.type("A1")
            sleep(0.2)
            self.keyboard_controller.press(keyboard.Key.enter)
            self.keyboard_controller.release(keyboard.Key.enter)
            sleep(0.2)
            self.keyboard_controller.press(keyboard.Key.esc)
            self.keyboard_controller.release(keyboard.Key.esc)
            sleep(0.2)

        keyboard_listener.stop()
        mouse_listener.stop()

    # Checks keyboard to see if correct combination has been input and executes
    def on_press(self,key):
        if key == keyboard.Key.esc:
            self.flag = True
        if any([key in COMBO for COMBO in self.COMBINATIONS]):
            self.current.add(key)
            if any(all(k in self.current for k in COMBO) for COMBO in self.COMBINATIONS):
                self.execute()

    # Removes input after keys on keyboard are released
    def on_release(self,key):
        if any([key in COMBO for COMBO in self.COMBINATIONS]):
            self.current.remove(key)

    # monitors mouse movement, but is not used
    def on_move(self,x,y):
        pass

    # monitors mouse scroll, but is not used
    def on_scroll(self,x,y,dx,dy):
        pass

    # monitors first two mouse clicks after start button to obtain position of first label
    def on_click(self,x,y,button,pressed):
        if pressed: # only collects data from press and not release
            if self.num_points == 0: # first click
                self.right_position = self.mouse_controller.position
                self.num_points += 1
            elif self.num_points == 1: # second click
                self.left_position = self.mouse_controller.position
                self.num_points += 1
            else:
                pass # future clicks are not recorded

    # Starts program
    def start(self, num_rows, num_cols, row_spacing, col_spacing):
        # Collects user input from GUI
        self.num_rows = int(num_rows)
        self.num_cols = int(num_cols)
        self.row_spacing = float(row_spacing)
        self.col_spacing = float(col_spacing)
        # Starts keyboard thread that listens for keyboard input
        keyboard_listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        keyboard_listener.start()
        # Initializes number of mouse clicks
        self.num_points=0
        # Starts mouse thread that listens for mouse input
        mouse_listener = mouse.Listener(on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll)
        mouse_listener.start()
