import json
import tkinter as tk

from pynput import keyboard


class PasswordKeeper:
    def __init__(self, source, username, password):
        self.__passes = {}
        self.length = len(self.__passes)
        self.source = source
        self.username = username
        self.password = password

    @property
    def passes(self):
        return self.__passes

    def add_source(self):
        self.__passes[self.source] = {None: None}

    def add_username(self):
        self.__passes[self.source] = {self.username: None}

    def add_password(self):
        self.__passes[self.source] = {self.username: self.password}



password_keeper = PasswordKeeper(input("Enter source app or website: "),
                                 input("Enter username or e-mail address: "),
                                 input("Enter password: "))


def addition():
    password_keeper.add_source()
    password_keeper.add_username()
    password_keeper.add_password()


addition()


with open('passes.json', 'a+') as file:
    json.dump(password_keeper.passes, file, indent=4, separators=(',', ': '))
    file.write('\n')
