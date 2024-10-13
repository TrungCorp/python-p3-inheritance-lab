#!/usr/bin/env python

from user import User

import random

class Teacher(User):

    def teach(self):
        for lesson in self.knowledge:
            lesson_obj_num = random.randrange(0,len(self.knowledge))
            return self.knowledge[lesson_obj_num]