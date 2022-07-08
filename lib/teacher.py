#!/usr/bin/env python

from lib.user import User

import random

class Teacher(User):

    KNOWLEDGE = [
        "a String is a data type in Python",
        "programming is hard, but it's worth it",
        "javascript async web request",
        "Python function call definition",
        "object oriented dog cat class instance",
        "programming computers hacking learning terminal",
        "pipenv shell",
        "pytest -x flag to fail fast",
    ]    

    def teach(self):
        # Resource: https://www.w3schools.com/python/module_random.asp
       return random.choice(Teacher.KNOWLEDGE)
    