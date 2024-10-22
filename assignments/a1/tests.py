# TODO: Add the test cases that you'll be submitting to this file!
#       Make sure your test cases are all named starting with
#       test_ and that they have unique names.

# You may need to import pytest in order to run your tests.
# You are free to import hypothesis and use hypothesis for testing.
# This file will not be graded for style with PythonTA

import pytest
from course import Student, Course
from survey import Question, MultipleChoiceQuestion, NumericQuestion, \
    YesNoQuestion, CheckboxQuestion, Answer, Survey
from criterion import InvalidAnswerError, Criterion, \
    HomogeneousCriterion, HeterogeneousCriterion, LonelyMemberCriterion
from grouper import Grouper, Grouping

###############################################################################
# course: Student
###############################################################################


class TestStudent:
    def test_set_answer(self) -> None:
        s1 = Student(1, 'Misha')
        s2 = Student(2, 'Diane')

        q1 = MultipleChoiceQuestion(1, 'what?', ['a', 'b', 'c'])
        q2 = YesNoQuestion(2, 'how?')
        q3 = NumericQuestion(3, 'when?', -10, 25)
        q4 = CheckboxQuestion(4, 'why?', ['a', 'b', 'c', 'd', 'e'])

        s1_ans_q1 = Answer('a')
        s1_ans_q2 = Answer(True)
        s1_ans_q3 = Answer(20)
        s1_ans_q4 = Answer(['c', 'a', 'e'])
        # all valid answers for 4 types of questions

        s1_ans_q1_new = Answer('c')
        s1_ans_q2_new = Answer(False)
        s1_ans_q3_new = Answer(-10)
        s1_ans_q4_new = Answer(['b', 'd'])
        # replace answers

        s2_ans_q1 = Answer('z')
        s2_ans_q2 = Answer('True')
        s2_ans_q3 = Answer(100)
        s2_ans_q4 = Answer(['c', 'z', 'e'])
        # all invalid answers for 4 types of questions

        s1.set_answer(q1, s1_ans_q1)
        s1.set_answer(q2, s1_ans_q2)
        s1.set_answer(q3, s1_ans_q3)
        s1.set_answer(q4, s1_ans_q4)

        # case 1: add new answer and question
        assert s1._question_n_answer == {q1: s1_ans_q1, q2: s1_ans_q2,
                                         q3: s1_ans_q3, q4: s1_ans_q4}

        s1.set_answer(q1, s1_ans_q1_new)
        s1.set_answer(q2, s1_ans_q2_new)
        s1.set_answer(q3, s1_ans_q3_new)
        s1.set_answer(q4, s1_ans_q4_new)

        # case 2: add new answer to existing question
        assert s1._question_n_answer == {q1: s1_ans_q1_new, q2: s1_ans_q2_new,
                                         q3: s1_ans_q3_new, q4: s1_ans_q4_new}

        s2.set_answer(q1, s2_ans_q1)
        s2.set_answer(q2, s2_ans_q2)
        s2.set_answer(q3, s2_ans_q3)
        s2.set_answer(q4, s2_ans_q4)

        # case 3: students give invalid answer to the questions
        assert s2._question_n_answer == {}

    def test_has_answer(self) -> None:
        s1 = Student(1, 'Misha')
        s2 = Student(2, 'Diane')

        q1 = MultipleChoiceQuestion(1, 'what?', ['a', 'b', 'c'])
        q2 = YesNoQuestion(2, 'how?')
        q3 = NumericQuestion(3, 'when?', -10, 25)
        q4 = CheckboxQuestion(4, 'why?', ['a', 'b', 'c', 'd', 'e'])
        q5 = MultipleChoiceQuestion(5, 'what?', ['a', 'b', 'c'])

        s1_ans_q1 = Answer('a')
        s1_ans_q2 = Answer(True)
        s1_ans_q3 = Answer(20)
        s1_ans_q4 = Answer(['c', 'a', 'e'])

        s1.set_answer(q1, s1_ans_q1)
        s1.set_answer(q2, s1_ans_q2)
        s1.set_answer(q3, s1_ans_q3)
        s1.set_answer(q4, s1_ans_q4)

        # case 1: student has valid answer to question
        assert s1.has_answer(q1)
        assert s1.has_answer(q2)
        assert s1.has_answer(q3)
        assert s1.has_answer(q4)

        s2_ans_q1 = Answer('z')
        s2_ans_q2 = Answer('True')
        s2_ans_q3 = Answer(100)
        s2_ans_q4 = Answer(['c', 'z', 'e'])

        s2.set_answer(q1, s2_ans_q1)
        s2.set_answer(q2, s2_ans_q2)
        s2.set_answer(q3, s2_ans_q3)
        s2.set_answer(q4, s2_ans_q4)

        # case 2: student has invalid answer to question
        assert not s2.has_answer(q1)
        assert not s2.has_answer(q2)
        assert not s2.has_answer(q3)
        assert not s2.has_answer(q4)

        # case 3: student doesn't have answer to question,
        # not in Student._answers
        assert not s1.has_answer(q5)
        assert not s2.has_answer(q5)

    def test_get_answer(self) -> None:
        s1 = Student(1, 'Misha')

        q1 = MultipleChoiceQuestion(1, 'what?', ['a', 'b', 'c'])
        q2 = YesNoQuestion(2, 'how?')
        q3 = NumericQuestion(3, 'when?', -10, 25)
        q4 = CheckboxQuestion(4, 'why?', ['a', 'b', 'c', 'd', 'e'])
        q5 = MultipleChoiceQuestion(5, 'what?', ['a', 'b', 'c'])
        q6 = NumericQuestion(3, 'when?', 3, 50)

        s1_ans_q1 = Answer('a')
        s1_ans_q2 = Answer(True)
        s1_ans_q3 = Answer(20)
        s1_ans_q4 = Answer(['c', 'a', 'e'])

        s1.set_answer(q1, s1_ans_q1)
        s1.set_answer(q2, s1_ans_q2)
        s1.set_answer(q3, s1_ans_q3)
        s1.set_answer(q4, s1_ans_q4)

        # case 1: student has valid answer to question
        assert s1.get_answer(q1) == s1_ans_q1
        assert s1.get_answer(q2) == s1_ans_q2
        assert s1.get_answer(q3) == s1_ans_q3
        assert s1.get_answer(q4) == s1_ans_q4

        # case 2: student doesn't have answer to question
        if s1.get_answer(q5) is None:
            assert True
        if s1.get_answer(q6) is None:
            assert True


###############################################################################
# course: Course
###############################################################################

class TestCourse:
    def test_enroll_students(self) -> None:
        s1, s2 = Student(1, 'Misha'), Student(1, 'Diane')
        s3, s4 = Student(3, ''), Student(4, '')
        s5, s6 = Student(5, 'Krishi'), Student(6, 'Grace')

        students1 = []
        students2 = [s1, s3, s4, s5]
        students3 = [s1, s5, s6]
        students4 = [s1, s2, s5]
        students5 = [s2, s6]

        # case 1: self.students is empty
        course1 = Course('CSC148')
        course1.enroll_students(students1)
        assert course1.students == []

        # case 2: some students in list have name = ''
        course1.enroll_students(students2)
        assert course1.students == [s1, s5]

        # case 3: all students in list have unique ids
        course2 = Course('CSC165')
        course2.enroll_students(students3)
        assert course1.students == [s1, s5, s6]

        # case 4: some students in list have duplicated ids (in list)
        course3 = Course('CSC108')
        course3.enroll_students(students4)
        assert course1.students == [s1, s5, s6]

        # case 5: some students in list have duplicated ids (in course)
        course3.enroll_students(students5)
        assert course3.students == [s1, s6]


    def test_all_answered(self) -> None:
        # q1 = MultipleChoiceQuestion(1, 'what?', ['a', 'b', 'c'])
        # q2 = YesNoQuestion(2, 'how?')
        # q3 = NumericQuestion(3, 'when?', -10, 25)
        # q4 = CheckboxQuestion(4, 'why?', ['a', 'b', 'c', 'd', 'e'])
        # q5 = MultipleChoiceQuestion(5, 'choose one?', ['x', 'y', 'z'])
        # q6 = YesNoQuestion(6, 'yes or no?')
        # q7 = NumericQuestion(7, 'choose number?', 0, 10)
        # q8 = CheckboxQuestion(8, 'choose many?', ['148', '165', '108', '101'])
        #
        # questions1 = [q1, q2, q3, q4, q5, q6, q7, q8]
        # questions2 = [q2, q4, q6, q8]
        # questions3 = [q1, q3, q5, q7]
        # survey1 = Survey(questions1)
        # survey2 = Survey(questions2)
        # survey3 = Survey(questions3)
        # survey4 = Survey([]) #empty survey, no Q&A
        #
        # s1, s2 = Student(3, 'Misha'), Student(1, 'Diane')
        # s3, s4 = Student(2, 'Mario'), Student(1, 'Hina')
        # s5, s6 = Student(5, 'Misha'), Student(1, '')
        #
        # # TODO: how to add Q&As to students?
        #
        # students1 = [s1, s2, s3, s4, s5, s6]
        # students2 = [s2, s4, s6]
        # students3 = [s1, s3, s5]
        #
        # c1 = Course('CSC108')
        # c2 = Course('CSC148')
        # c3 = Course('CSC165')
        # c4 = Course('empty')
        # c1.enroll_students(students1)
        # c2.enroll_students(students2)
        # c3.enroll_students(students3)
        # c4.enroll_students([]) #empty course, no students
        #
        # assert c1.all_answered(survey1)
        # assert c1.all_answered(survey2)
        # assert c1.all_answered(survey3)
        # assert c1.all_answered(survey4)
        #
        # assert c2.all_answered(survey1)
        # assert c2.all_answered(survey2)
        # assert c2.all_answered(survey3)
        # assert c2.all_answered(survey4)
        #
        # assert c3.all_answered(survey1)
        # assert c3.all_answered(survey2)
        # assert c3.all_answered(survey3)
        # assert c3.all_answered(survey4)
        #
        # assert c4.all_answered(survey1)
        # assert c4.all_answered(survey2)
        # assert c4.all_answered(survey3)
        # assert c4.all_answered(survey4)
        pass
        # TODO: come back after finishing class Survey

    def test_get_students(self) -> None:
        s1, s2 = Student(3, 'Misha'), Student(1, 'Diane')
        s3, s4 = Student(2, 'Mario'), Student(1, 'Hina')
        s5, s6 = Student(5, 'Misha'), Student(1, '')

        students1 = [s1, s2, s3, s4, s5, s6]

        course1 = Course('CSC148')
        course2 = Course('CSC108')

        course1.enroll_students(students1)
        course2.enroll_students([]) # course with no students

        assert course1.get_students() == (s2, s3, s1, s5)
        assert course2.get_students() == ()


###############################################################################
# survey: Question
###############################################################################

###############################################################################
# survey: Answer
###############################################################################

###############################################################################
# survey: Survey
###############################################################################


###############################################################################
# criterion: HomogeneousCriterion
###############################################################################

# case 1: 1 answer to question (return 1.0)
# case 2: not valid answer to questions
# case 3: more than 1 answers, all similar (return 1.0)
# case 4: more than 1 answers, all not similar (return (0.0)
# case 5: more than 1 answers, some similar, some not (return between 0 - 1)
def test_score_answers_homo_multichoice() -> None:
    q1 = MultipleChoiceQuestion(1, 'what?', ['a', 'b', 'c', 'd'])

    a1 = Answer('a')
    a2 = Answer('z')
    a3 = Answer('a')
    a4 = Answer('c')

    ans_list_1 = [a1]
    ans_list_2 = [a1, a2]
    ans_list_3 = [a1, a3]
    ans_list_4 = [a1, a4]
    ans_list_5 = [a1, a4, a3, a4]

    assert HomogeneousCriterion.score_answers(HomogeneousCriterion,
                                              q1, ans_list_1) == 1.0
    # case 1: 1 answer to question (return 1.0)

    assert HomogeneousCriterion.score_answers(HomogeneousCriterion, q1,
                                              ans_list_2) == InvalidAnswerError
    # case 2: not valid answer to questions
    # TODO: NOT WORKING

    assert HomogeneousCriterion.score_answers(HomogeneousCriterion,
                                              q1, ans_list_3) == 1.0
    # case 3: more than 1 answers, all similar (return 1.0)

    assert HomogeneousCriterion.score_answers(HomogeneousCriterion,
                                              q1, ans_list_4) == 0.0
    # case 4: more than 1 answers, all not similar (return (0.0)

    assert HomogeneousCriterion.score_answers(HomogeneousCriterion,
                                              q1, ans_list_5) == 2/6
    # case 5: more than 1 answers, some similar, some not (return between 0 - 1)


def test_score_answers_homo_numeric() -> None:
    q1 = NumericQuestion(2, 'when?', -10, 25)

    a1 = Answer(10)
    a2 = Answer(100)
    a3 = Answer(10)
    a4 = Answer(-5)

    ans_list_1 = [a1]
    ans_list_2 = [a1, a2]
    ans_list_3 = [a1, a3]
    ans_list_4 = [a1, a4]
    ans_list_5 = [a1, a4, a3, a4]

    assert HomogeneousCriterion.score_answers(HomogeneousCriterion,
                                              q1, ans_list_1) == 1.0
    # case 1: 1 answer to question (return 1.0)

    assert HomogeneousCriterion.score_answers(HomogeneousCriterion, q1,
                                              ans_list_2) == InvalidAnswerError
    # case 2: not valid answer to questions
    # TODO: NOT WORKING

    assert HomogeneousCriterion.score_answers(HomogeneousCriterion,
                                              q1, ans_list_3) == 1.0
    # case 3: more than 1 answers, all similar (return 1.0)

    assert HomogeneousCriterion.score_answers(HomogeneousCriterion,
                                              q1, ans_list_4) == 0.0
    # case 4: more than 1 answers, all not similar (return (0.0)

    assert HomogeneousCriterion.score_answers(HomogeneousCriterion,
                                              q1, ans_list_5) == 2/6
    # case 5: more than 1 answers, some similar, some not (return between 0 - 1)


def test_score_answers_homo_yesorno() -> None:
    q1 = YesNoQuestion(2, 'how?')

    a1 = Answer(True)
    a2 = Answer('True')
    a3 = Answer(True)
    a4 = Answer(False)

    ans_list_1 = [a1]
    ans_list_2 = [a1, a2]
    ans_list_3 = [a1, a3]
    ans_list_4 = [a1, a4]
    ans_list_5 = [a1, a4, a3, a4]

    assert HomogeneousCriterion.score_answers(HomogeneousCriterion,
                                              q1, ans_list_1) == 1.0
    # case 1: 1 answer to question (return 1.0)

    assert HomogeneousCriterion.score_answers(HomogeneousCriterion, q1,
                                              ans_list_2) == InvalidAnswerError
    # case 2: not valid answer to questions
    # TODO: NOT WORKING

    assert HomogeneousCriterion.score_answers(HomogeneousCriterion,
                                              q1, ans_list_3) == 1.0
    # case 3: more than 1 answers, all similar (return 1.0)

    assert HomogeneousCriterion.score_answers(HomogeneousCriterion,
                                              q1, ans_list_4) == 0.0
    # case 4: more than 1 answers, all not similar (return (0.0)

    assert HomogeneousCriterion.score_answers(HomogeneousCriterion,
                                              q1, ans_list_5) == 2/6
    # case 5: more than 1 answers, some similar, some not (return between 0 - 1)


def test_score_answers_homo_checkbox() -> None:
    q1 = CheckboxQuestion(4, 'why?', ['a', 'b', 'c', 'd', 'e'])

    a1 = Answer(True)
    a2 = Answer('True')
    a3 = Answer(True)
    a4 = Answer(False)

    ans_list_1 = [a1]
    ans_list_2 = [a1, a2]
    ans_list_3 = [a1, a3]
    ans_list_4 = [a1, a4]
    ans_list_5 = [a1, a4, a3, a4]

    assert HomogeneousCriterion.score_answers(HomogeneousCriterion,
                                              q1, ans_list_1) == 1.0
    # case 1: 1 answer to question (return 1.0)

    assert HomogeneousCriterion.score_answers(HomogeneousCriterion, q1,
                                              ans_list_2) == InvalidAnswerError
    # case 2: not valid answer to questions
    # TODO: NOT WORKING

    assert HomogeneousCriterion.score_answers(HomogeneousCriterion,
                                              q1, ans_list_3) == 1.0
    # case 3: more than 1 answers, all similar (return 1.0)

    assert Criterion.score_answers(HomogeneousCriterion,
                                              q1, ans_list_4) == 0.0
    # case 4: more than 1 answers, all not similar (return (0.0)

    assert HomogeneousCriterion.score_answers(HomogeneousCriterion,
                                              q1, ans_list_5) == 2/6
    # case 5: more than 1 answers, some similar, some not (return between 0 - 1)

###############################################################################
# criterion: HeterogeneousCriterion
###############################################################################


def test_score_answers_hetero() -> None:
    pass

###############################################################################
# criterion: LonelyMemberCriterion
###############################################################################


def test_score_answers_lonely() -> None:
    pass

###############################################################################
# grouper: Grouper
###############################################################################

###############################################################################
# grouper: Grouping
###############################################################################



###############################################################################
# Task 3 Test cases
###############################################################################
# TODO: Add your test cases below


###############################################################################
# Task 4 Test cases
###############################################################################
# TODO: Add your test cases below


###############################################################################
# Task 5 Test cases
###############################################################################
# TODO: Add your test cases below


###############################################################################
# Task 6 Test cases
###############################################################################
# TODO: Add your test cases below


###############################################################################
# Task 7 Test cases
###############################################################################
# TODO: Add your test cases below


###############################################################################
# Task 8 Test cases
###############################################################################
# TODO: Add your test cases below


###############################################################################
# Task 9 Test cases
###############################################################################
# TODO: Add your test cases below


###############################################################################
# Task 10 Test cases
###############################################################################
# TODO: Add your test cases below

