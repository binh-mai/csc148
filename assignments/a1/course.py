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
    _question_n_answer: a dictionary that record student's answer to question

    === Representation Invariants ===
    name is not the empty string
    """
    id: int
    name: str
    _question_n_answer: dict

    def __init__(self, id_: int, name: str) -> None:
        """Initialize a student with name <name> and id <id>"""
        self.id = id_
        self.name = name
        self._question_n_answer = {}

    def __str__(self) -> str:
        """Return the name of this student """
        return self.name

# TODO: different here
    def has_answer(self, question: Question) -> bool:
        """Return True iff this student has an answer for a question with the
        same id as <question> and that answer is a valid answer for <question>.
        """
        if len(self._question_n_answer) == 0:
            return False

        questions_id = []
        for question in self._question_n_answer:
            questions_id.append(question.id)

        if question.id in questions_id \
                and question.validate_answer(self._question_n_answer[question]):
            return True
        return False

    def set_answer(self, question: Question, answer: Answer) -> None:
        """Record this student's answer <answer> to the question <question>.

        If this student already has an answer recorded for the question, then
        replace it with <answer>.
        """
        if question.validate_answer(answer):
            self._question_n_answer[question] = answer

    def get_answer(self, question: Question) -> Optional[Answer]:
        """Return this student's answer to the question <question>.
        Return None if this student does not have an answer to <question>
        """
        if self.has_answer(question):
            return self._question_n_answer[question]
        return None


class Course:
    """A University Course

    === Public Attributes ===
    name: the name of the course
    students: a list of students enrolled in the course

    === Private Attributes ===

    === Representation Invariants ===
    - No two students in this course have the same id
    - name is not the empty string
    """
    name: str
    students: list[Student]

    def __init__(self, name: str) -> None:
        """Initialize a course with the name of <name>.
        """
        self.name = name
        self.students = []

    def enroll_students(self, students: list[Student]) -> None:
        """Enroll all students in <students> in this course.

        If adding any student would violate a representation invariant,
        do not add any of the students in <students> to the course.
        """
        for stu in students:
            if stu.name == '':
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

    def all_answered(self, survey: Survey) -> bool:
        """Return True iff all the students enrolled in this course have a
        valid answer for every question in <survey>.
        """
        for student in self.students:
            for question in survey.get_questions():
                if not student.has_answer(question):
                    return False
        return True

    def get_students(self) -> tuple[Student]:
        """Return a tuple of all students enrolled in this course.

        The students in this tuple should be in order according to their id
        from the lowest id to the highest id.

        Hint: the sort_students function might be useful
        """
        return tuple(sort_students(self.students, 'id'))


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={'extra-imports': ['typing', 'survey'],
                                'disable': ['E9992']})