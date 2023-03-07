from pynput import keyboard
import time
import string

class hotkey():
    # The key combination to check
    def __init__(self):
        self.COMBINATIONS = [
            {keyboard.Key.num_lock}
        ]

        self.letters = list(string.ascii_uppercase)
        self.Controller = keyboard.Controller()
        self.current = set()

    def execute(self):
        self.Controller.type(self.letters[self.let_iter]+str(self.col_iter))
        if self.col_iter == self.num_col:
            self.let_iter += 1
            self.col_iter = 0
        self.col_iter += 1
        time.sleep(0.001)
        self.Controller.press(keyboard.Key.enter)
        self.Controller.release(keyboard.Key.enter)

    def on_press(self,key):
        if any([key in COMBO for COMBO in self.COMBINATIONS]):
            self.current.add(key)
            if any(all(k in self.current for k in COMBO) for COMBO in self.COMBINATIONS):
                self.execute()

    def on_release(self,key):
        if any([key in COMBO for COMBO in self.COMBINATIONS]):
            self.current.remove(key)
            
    def start(self,start_label,num_col):
        self.let_iter=int(self.letters.index(start_label[:1]))
        self.col_iter=int(start_label[1:])
        self.num_col=int(num_col)
        listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        listener.start()
        #with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
        #    listener.join()
