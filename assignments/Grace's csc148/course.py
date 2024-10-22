"""CSC148 Assignment 1

=== CSC148 Winter 2023 ===
Department of Computer Science,
University of Toronto

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Authors: Misha Schwartz, Mario Badr, Christine Murad, Diane Horton,
Sophia Huynh, Jaisie Sin, Tom Ginsberg, Jonathan Calver, and Jacqueline Smith

All of the files in this directory and all subdirectories are:
Copyright (c) 2023 Misha Schwartz, Mario Badr, Diane Horton, Sophia Huynh,
Jonathan Calver, and Jacqueline Smith

=== Module Description ===
This file contains classes that describe a university course and the students
who are enrolled in these courses.
"""
from __future__ import annotations
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from survey import Answer, Survey, Question


# Provided helper function
def sort_students(lst: list[Student], attribute: str) -> list[Student]:
    """Return a shallow copy of <lst> sorted by <attribute> in non-decreasing
    order.

    Being a shallow copy means that a new list is returned, but it contains
    ids of the same Student objects as in <lst>; no new Student objects are
    created. The conseqence of this is that aliasing exists. Suggestion: draw
    a memory model diagram to ensure that you understand this.

    Preconditions:
        - <attribute> is an attribute name for the Student class

    >>> s1 = Student(1, 'Misha')
    >>> s2 = Student(2, 'Diane')
    >>> s3 = Student(3, 'Mario')
    >>> sort_students([s1, s3, s2], 'id') == [s1, s2, s3]
    True
    >>> sort_students([s1, s2, s3], 'name') == [s2, s3, s1]
    True
    """
    return sorted(lst, key=lambda student: getattr(student, attribute))


class Student:
    """A Student who can be enrolled in a university course.

    === Public Attributes ===
    id: the id of the student
    name: the name of the student

    === Private Attributes ===
    _answers: a dictionary containing the answers which the student puts, key is
            question object, and value is the students answer.

    === Representation Invariants ===
    name is not the empty string
    """
    id: int
    name: str
    _answers: dict

    def __init__(self, id_: int, name: str) -> None:
        """Initialize a student with name <name> and id <id>
        Precondition
        len(name) > 0
        """
        self.name = name
        self.id = id_
        self._answers = {}

    def __str__(self) -> str:
        """Return the name of this student """
        return self.name

    def has_answer(self, question: Question) -> bool:
        """Return True iff this student has an answer for a question with the
        same id as <question> and that answer is a valid answer for <question>.
        """
        if len(self._answers) == 0:
            return False

        exists = False
        for questions in self._answers:
            if questions.id == question.id:
                exists = True

        if exists is False:
            return False

        if question.validate_answer(self._answers[question]):
            return True
        else:
            return False

    def set_answer(self, question: Question, answer: Answer) -> None:
        """Record this student's answer <answer> to the question <question>.

        If this student already has an answer recorded for the question, then
        replace it with <answer>.
        """
        if question.validate_answer(answer):
            self._answers[question] = answer

    def get_answer(self, question: Question) -> Optional[Answer]:
        """Return this student's answer to the question <question>.
        Return None if this student does not have an answer to <question>
        """
        for questions in self._answers:
            if question == questions:
                return self._answers[question]
        return None


class Course:
    """A University Course

    === Public Attributes ===
    name: the name of the course
    students: a list of students enrolled in the course

    === Private Attributes ===
    TODO: Describe any private attributes you create here

    === Representation Invariants ===
    - No two students in this course have the same id
    - name is not the empty string
    """
    name: str
    students: list[Student]

    def __init__(self, name: str) -> None:
        """Initialize a course with the name of <name>.
        Preconditions
        len(name) > 0
        """
        self.name = name
        self.students = []

    def enroll_students(self, students: list[Student]) -> None:
        """Enroll all students in <students> in this course.

        If adding any student would violate a representation invariant,
        do not add any of the students in <students> to the course.
        """
        for stu in students:
            if stu.name.strip() == '':
                students.remove(stu)

        lst_ids = []

        if len(self.students) == 0:
            for stu in students:
                if stu.id not in lst_ids:
                    self.students.append(stu)
                    lst_ids.append(stu.id)
            return None
        else:
            for people in self.students:
                lst_ids.append(people.id)

        for student in students:
            if student.id not in lst_ids:
                self.students.append(student)
                lst_ids.append(student.id)
        return None

        # for stu in students:
        #     if stu.name == "":
        #         students.remove(stu)
        #
        # lst_ids = []
        # if len(self.students) == 0:
        #     for stu in students:
        #         if stu.id not in lst_ids:
        #             self.students.append(stu)
        #             lst_ids.append(stu.id)
        #     return None
        # else:
        #     for people in self.students:
        #         lst_ids.append(people.id)
        # for student in students:
        #     if student.id not in lst_ids:
        #         self.students.append(student)
        #         lst_ids.append(student.id)
        # return None

    def all_answered(self, survey: Survey) -> bool:
        """Return True iff all the students enrolled in this course have a
        valid answer for every question in <survey>.
        """
        # questions_list = survey.get_questions()
        # students_list = self.students
        # for student in students_list:
        #     for questions in questions_list:
        #         if student.get_answer(questions) is None:
        #             return False
        #         elif questions.validate_answer(student.get_answer(questions)) \
        #                 is False:
        #             return False
        # return True
        question_list = survey.get_questions()
        students_list = self.students
        for student in students_list:
            for questions in question_list:
                if student.has_answer(questions) is False:
                    return False
        return True

    def get_students(self) -> tuple[Student]:
        """Return a tuple of all students enrolled in this course.

        The students in this tuple should be in order according to their id
        from the lowest id to the highest id.

        Hint: the sort_students function might be useful
        """
        lst = sort_students(self.students, 'id')
        return tuple(lst)


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={'extra-imports': ['typing', 'survey'],
                                'disable': ['E9992']})
