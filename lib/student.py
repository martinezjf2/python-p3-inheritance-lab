#!/usr/bin/env python

from lib.user import User

class Student(User):
    
    knowledge = []
    
    def learn(self, string):
        self.knowledge.append(string)
    pass
