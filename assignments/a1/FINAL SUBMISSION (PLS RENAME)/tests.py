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
from grouper import Group, Grouper, Grouping

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
        assert s1._answers == {q1: s1_ans_q1, q2: s1_ans_q2,
                               q3: s1_ans_q3, q4: s1_ans_q4}

        s1.set_answer(q1, s1_ans_q1_new)
        s1.set_answer(q2, s1_ans_q2_new)
        s1.set_answer(q3, s1_ans_q3_new)
        s1.set_answer(q4, s1_ans_q4_new)

        # case 2: add new answer to existing question
        assert s1._answers == {q1: s1_ans_q1_new, q2: s1_ans_q2_new,
                               q3: s1_ans_q3_new, q4: s1_ans_q4_new}

        s2.set_answer(q1, s2_ans_q1)
        s2.set_answer(q2, s2_ans_q2)
        s2.set_answer(q3, s2_ans_q3)
        s2.set_answer(q4, s2_ans_q4)

        # case 3: students give invalid answer to the questions
        assert s2._answers == {}

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
        s3 = Student(3, '')
        s4 = Student(4, '')
        s7 = Student(7, '')
        s5, s6 = Student(5, 'Krishi'), Student(6, 'Grace')

        students1 = []
        students2 = [s1, s3, s4, s5, s7]
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
        s1, s2 = Student(1, 'Misha'), Student(2, 'Diane')
        s3, s4 = Student(3, 'Krishi'), Student(4, 'Grace')
        students1 = []
        students2 = [s1, s2]
        # all with valid answers
        students3 = [s1, s2, s3, s4]
        # s3 and s4 have partially invalid answers

        q1 = MultipleChoiceQuestion(1, 'what?', ['a', 'b', 'c'])
        q2 = YesNoQuestion(2, 'how?')
        q3 = NumericQuestion(3, 'when?', -10, 25)
        q4 = CheckboxQuestion(4, 'why?', ['a', 'b', 'c', 'd', 'e'])
        q5 = MultipleChoiceQuestion(5, 'what?', ['a', 'b', 'c'])

        survey1 = Survey([q1, q2, q3, q4])
        survey2 = Survey([q1, q2, q3, q4, q5])
        survey3 = Survey([])

        course1 = Course('CSC148')
        course1.enroll_students(students1)
        # case 1: course has no student, Course.students = []
        assert not course1.all_answered(survey1)

        course1.enroll_students(students2)
        # case 2: course has students but students don't have
        # answer question in survey
        assert not course1.all_answered(survey1)

        # case 3: survey is empty, survey._question = {}
        assert not course1.all_answered(survey3)

        s1_ans_q1, s1_ans_q2 = Answer('a'), Answer(True)
        s1_ans_q3, s1_ans_q4 = Answer(20), Answer(['c', 'a', 'e'])

        s2_ans_q1, s2_ans_q2 = Answer('b'), Answer(False)
        s2_ans_q3, s2_ans_q4 = Answer(-10), Answer(['e', 'a'])

        s1.set_answer(q1, s1_ans_q1)
        s1.set_answer(q2, s1_ans_q2)
        s1.set_answer(q3, s1_ans_q3)
        s1.set_answer(q4, s1_ans_q4)

        s2.set_answer(q1, s2_ans_q1)
        s2.set_answer(q2, s2_ans_q2)
        s2.set_answer(q3, s2_ans_q3)
        s2.set_answer(q4, s2_ans_q4)

        course2 = Course('CSC165')
        course2.enroll_students(students2)
        # case 4: all students have valid answers to questions in survey
        assert course2.all_answered(survey1)

        # case 6: survey has 1 extra question that students don't have answer to
        assert not course2.all_answered(survey2)

        s3_ans_q1, s3_ans_q2 = Answer('a'), Answer('True')
        s3_ans_q3, s3_ans_q4 = Answer(25), Answer(['c', 'a', 'z'])

        s4_ans_q1, s4_ans_q2 = Answer('z'), Answer(False)
        s4_ans_q3, s4_ans_q4 = Answer(100), Answer(['e', 'a'])

        s3.set_answer(q1, s3_ans_q1)
        s3.set_answer(q2, s3_ans_q2)
        s3.set_answer(q3, s3_ans_q3)
        s3.set_answer(q4, s3_ans_q4)

        s4.set_answer(q1, s4_ans_q1)
        s4.set_answer(q2, s4_ans_q2)
        s4.set_answer(q3, s4_ans_q3)
        s4.set_answer(q4, s4_ans_q4)

        course2.enroll_students(students3)
        assert not course2.all_answered(survey1)

    def test_get_students(self) -> None:
        s1, s2 = Student(3, 'Misha'), Student(1, 'Diane')
        s3, s4 = Student(2, 'Mario'), Student(1, 'Hina')
        s5, s6 = Student(5, 'Misha'), Student(1, '')

        students1 = [s1, s2, s3, s4, s5, s6]

        course1 = Course('CSC148')
        course2 = Course('CSC108')

        course1.enroll_students(students1)
        course2.enroll_students([])

        # case 1: students with different ids in wrong order
        assert course1.get_students() == (s2, s3, s1, s5)

        # case 2: no student in course, return ()
        assert course2.get_students() == ()


###############################################################################
# survey: Question
###############################################################################

class TestMultipleChoiceQuestion:
    def test_validate_answer(self) -> None:
        q1 = MultipleChoiceQuestion(1, 'what?', ['a', 'b', 'c'])

        ans1_valid1 = Answer('b')
        ans1_valid2 = Answer('c')
        ans1_valid3 = Answer('a')

        ans1_int = Answer(1)
        ans1_lst = Answer(['a'])
        ans1_bool = Answer(True)
        ans1_str = Answer('A')

        # case 1: answer is valid
        assert q1.validate_answer(ans1_valid1)
        assert q1.validate_answer(ans1_valid2)
        assert q1.validate_answer(ans1_valid3)

        # case 2: answer is invalid
        assert not q1.validate_answer(ans1_int)
        assert not q1.validate_answer(ans1_lst)
        assert not q1.validate_answer(ans1_bool)
        assert not q1.validate_answer(ans1_str)

    def test_get_similarity(self) -> None:
        q1 = MultipleChoiceQuestion(1, 'what?', ['a', 'b', 'c'])

        ans1 = Answer('b')
        ans2 = Answer('b')
        ans3 = Answer('c')

        # case 1: answer1 == answer2 ->return 1.0
        assert q1.get_similarity(ans1, ans2) == 1.0

        # case 2: answer1 != answer2 -> return 0.0
        assert q1.get_similarity(ans1, ans3) == 0.0


class TestNumericQuestion:
    def test_validate_answer(self) -> None:
        q1 = NumericQuestion(3, 'when?', -10, 25)

        ans1_valid1 = Answer(-10)
        ans1_valid2 = Answer(0)
        ans1_valid3 = Answer(25)

        ans1_int = Answer(100)
        ans1_lst = Answer(['0'])
        ans1_bool = Answer(False)
        ans1_str = Answer('0')

        # case 1: answer is valid
        assert q1.validate_answer(ans1_valid1)
        assert q1.validate_answer(ans1_valid2)
        assert q1.validate_answer(ans1_valid3)

        # case 2: answer is invalid
        assert not q1.validate_answer(ans1_int)
        assert not q1.validate_answer(ans1_lst)
        assert not q1.validate_answer(ans1_bool)
        assert not q1.validate_answer(ans1_str)

    def test_get_similarity(self) -> None:
        q1 = NumericQuestion(3, 'when?', -20, 20)

        ans1 = Answer(-20)
        ans2 = Answer(-20)
        ans3 = Answer(20)
        ans4 = Answer(15)
        ans5 = Answer(-10)

        # case 1: answer1 == answer2 -> 1.0
        assert q1.get_similarity(ans1, ans2) == 1.0

        # case 2: answer1 == self._min and answer2 == se;f._max -> 0.0
        assert q1.get_similarity(ans1, ans3) == 0.0

        # case 3: answer1 and answer2 in between min and max
        assert q1.get_similarity(ans4, ans5) == 0.375


class TestYesNoQuestion:
    def test_validate_answer(self) -> None:
        q1 = YesNoQuestion(2, 'how?')

        ans1_valid1 = Answer(True)
        ans1_valid2 = Answer(False)

        ans1_int = Answer(100)
        ans1_lst = Answer(['True'])
        ans1_str = Answer('False')

        # case 1: answer is valid
        assert q1.validate_answer(ans1_valid1)
        assert q1.validate_answer(ans1_valid2)

        # case 2: answer is invalid
        assert not q1.validate_answer(ans1_int)
        assert not q1.validate_answer(ans1_lst)
        assert not q1.validate_answer(ans1_str)

    def test_get_similarity(self) -> None:
        q1 = YesNoQuestion(2, 'how?')

        ans1 = Answer(True)
        ans2 = Answer(True)
        ans3 = Answer(False)
        ans4 = Answer(False)

        # case 1: answer1 == answer2 ->return 1.0
        assert q1.get_similarity(ans1, ans2) == 1.0
        assert q1.get_similarity(ans3, ans4) == 1.0

        # case 2: answer1 != answer2 -> return 0.0
        assert q1.get_similarity(ans1, ans3) == 0.0
        assert q1.get_similarity(ans2, ans4) == 0.0


class TestCheckboxQuestion:
    def test_validate_answer(self) -> None:
        q1 = CheckboxQuestion(5, 'many?', ['a', 'b', 'c', 'd', 'e', 'f'])

        ans1_valid1 = Answer(['a', 'b', 'c', 'd', 'e', 'f'])
        ans1_valid2 = Answer(['d'])
        ans1_valid3 = Answer(['f', 'b', 'd'])

        ans1_int = Answer(1)
        ans1_bool = Answer(True)
        ans1_str = Answer('a')
        ans1_lst = Answer(['a', 'z'])

        # case 1: answer is valid
        assert q1.validate_answer(ans1_valid1)
        assert q1.validate_answer(ans1_valid2)
        assert q1.validate_answer(ans1_valid3)

        # case 2: answer is invalid
        assert not q1.validate_answer(ans1_int)
        assert not q1.validate_answer(ans1_bool)
        assert not q1.validate_answer(ans1_str)
        assert not q1.validate_answer(ans1_lst)

    def test_get_similarity(self) -> None:
        q1 = CheckboxQuestion(5, 'many?', ['a', 'b', 'c', 'd', 'e', 'f'])

        ans1 = Answer(['a', 'b', 'c'])
        ans2 = Answer(['c', 'a', 'b'])
        ans3 = Answer(['d', 'f', 'e'])
        ans4 = Answer(['c', 'e', 'f'])
        ans5 = Answer(['a', 'c', 'd', 'e'])

        # case 1: answer1 == answer2 ->return 1.0
        assert q1.get_similarity(ans1, ans2) == 1.0

        # case 2: answer1 != answer2 -> return 0.0
        assert q1.get_similarity(ans1, ans3) == 0.0

        # case 3: answer1 and answer2 has some common answers
        assert q1.get_similarity(ans4, ans5) == 0.4

###############################################################################
# survey: Answer
###############################################################################


class TestAnswer:
    def test_is_valid_multichoice(self) -> None:
        q1 = MultipleChoiceQuestion(1, 'what?', ['a', 'b', 'c'])

        ans1_valid1 = Answer('b')
        ans1_valid2 = Answer('c')
        ans1_valid3 = Answer('a')

        ans1_int = Answer(1)
        ans1_lst = Answer(['a'])
        ans1_bool = Answer(True)
        ans1_str = Answer('A')

        # case 1: answer is valid
        assert ans1_valid1.is_valid(q1)
        assert ans1_valid2.is_valid(q1)
        assert ans1_valid3.is_valid(q1)

        # case 2: answer is invalid
        assert not ans1_int.is_valid(q1)
        assert not ans1_lst.is_valid(q1)
        assert not ans1_bool.is_valid(q1)
        assert not ans1_str.is_valid(q1)

    def test_is_valid_numeric(self) -> None:
        q1 = NumericQuestion(3, 'when?', -10, 25)

        ans1_valid1 = Answer(-10)
        ans1_valid2 = Answer(0)
        ans1_valid3 = Answer(25)

        ans1_int = Answer(100)
        ans1_lst = Answer(['0'])
        ans1_bool = Answer(False)
        ans1_str = Answer('0')

        # case 1: answer is valid
        assert ans1_valid1.is_valid(q1)
        assert ans1_valid2.is_valid(q1)
        assert ans1_valid3.is_valid(q1)

        # case 2: answer is invalid
        assert not ans1_int.is_valid(q1)
        assert not ans1_lst.is_valid(q1)
        assert not ans1_bool.is_valid(q1)
        assert not ans1_str.is_valid(q1)

    def test_is_valid_yesno(self) -> None:
        q1 = YesNoQuestion(2, 'how?')

        ans1_valid1 = Answer(True)
        ans1_valid2 = Answer(False)

        ans1_int = Answer(100)
        ans1_lst = Answer(['True'])
        ans1_str = Answer('False')

        # case 1: answer is valid
        assert ans1_valid1.is_valid(q1)
        assert ans1_valid2.is_valid(q1)

        # case 2: answer is invalid
        assert not ans1_int.is_valid(q1)
        assert not ans1_lst.is_valid(q1)
        assert not ans1_str.is_valid(q1)

    def test_is_valid_checkbox(self) -> None:
        q1 = CheckboxQuestion(5, 'many?', ['a', 'b', 'c', 'd', 'e', 'f'])

        ans1_valid1 = Answer(['a', 'b', 'c', 'd', 'e', 'f'])
        ans1_valid2 = Answer(['d'])
        ans1_valid3 = Answer(['f', 'b', 'd'])

        ans1_int = Answer(1)
        ans1_bool = Answer(True)
        ans1_str = Answer('a')
        ans1_lst = Answer(['a', 'z'])

        # case 1: answer is valid
        assert ans1_valid1.is_valid(q1)
        assert ans1_valid2.is_valid(q1)
        assert ans1_valid3.is_valid(q1)

        # case 2: answer is invalid
        assert not ans1_int.is_valid(q1)
        assert not ans1_lst.is_valid(q1)
        assert not ans1_bool.is_valid(q1)
        assert not ans1_str.is_valid(q1)


###############################################################################
# survey: Survey
###############################################################################

class TestSurvey:
    def test_get_questions(self) -> None:
        q1 = MultipleChoiceQuestion(1, 'what?', ['a', 'b', 'c'])
        q2 = YesNoQuestion(2, 'how?')
        q3 = NumericQuestion(3, 'when?', -10, 25)
        q4 = CheckboxQuestion(4, 'why?', ['a', 'b', 'c', 'd', 'e'])

        survey1 = Survey([])
        survey2 = Survey([q1, q2])
        survey3 = Survey([q1, q2, q3, q4])

        # case 1: survey has no question -> return []
        assert survey1.get_questions() == []

        # case 2: survey has different types of questions
        assert survey2.get_questions() == [q1, q2]
        assert survey3.get_questions() == [q1, q2, q3, q4]

    # case 1: empty survey._criteria
    # case 2: question in survey._criteria
    # case 3: question not in survey._criteria
    # def test__set_criterion(self) -> None:
    #     q1 = MultipleChoiceQuestion(1, 'what?', ['a', 'b', 'c'])
    #     q1_id = q1.id
    #     q2 = YesNoQuestion(2, 'how?')
    #     q2_id = q2.id
    #     q3 = NumericQuestion(3, 'when?', -10, 25)
    #     q3_id = q3.id
    #     q4 = CheckboxQuestion(4, 'why?', ['a', 'b', 'c', 'd', 'e'])
    #     q4_id = q4.id
    #
    #     homo = HomogeneousCriterion()
    #
    #     survey1 = Survey([])
    #     survey2 = Survey([q1, q2])
    #
    #     # case 1: empty survey._criteria
    #     survey1.set_criterion(HomogeneousCriterion, q1)
    #     assert survey1._criteria == {}
    #
    #     survey1.set_criterion(HeterogeneousCriterion, q1)
    #     assert survey1._criteria == {}
    #
    #     survey1.set_criterion(LonelyMemberCriterion, q1)
    #     assert survey1._criteria == {}
    #
    #     # case 2: question in survey._criteria
    #     assert survey2._criteria == {q1_id: homo,
    #                                  q2_id: homo}
    #     survey2.set_criterion(HomogeneousCriterion, q1)
    #     survey2.set_criterion(LonelyMemberCriterion, q2)
    #     assert survey2._criteria == {q1_id: HomogeneousCriterion,
    #                                  q2_id: LonelyMemberCriterion}
    #
    #     # case 3: question not in survey._criteria
    #     assert survey2._criteria == {q1_id: HomogeneousCriterion,
    #                                  q2_id: HomogeneousCriterion}
    #     survey2.set_criterion(HomogeneousCriterion, q3)
    #     survey2.set_criterion(LonelyMemberCriterion, q4)
    #     assert survey2._criteria == {q1_id: HomogeneousCriterion,
    #                                  q2_id: HomogeneousCriterion}

    # TODO: can't create Criterion object

    # def test__get_criterion(self) -> None:
    #         q1 = MultipleChoiceQuestion(1, 'what?', ['a', 'b', 'c'])
    #         q1_id = q1.id
    #         q2 = YesNoQuestion(2, 'how?')
    #         q2_id = q2.id
    #         q3 = NumericQuestion(3, 'when?', -10, 25)
    #         q3_id = q3.id
    #         q4 = CheckboxQuestion(4, 'why?', ['a', 'b', 'c', 'd', 'e'])
    #         q4_id = q4.id
    #
    #         survey = Survey([q1, q2, q3, q4])
    #
    #         assert survey._get_criterion(q1) == HomogeneousCriterion

    # TODO: can't create Criterion object

    def test_set_weight(self) -> None:
        q1 = MultipleChoiceQuestion(1, 'what?', ['a', 'b', 'c'])
        q1_id = q1.id
        q2 = YesNoQuestion(2, 'how?')
        q2_id = q2.id
        q3 = NumericQuestion(3, 'when?', -10, 25)
        q4 = CheckboxQuestion(4, 'why?', ['a', 'b', 'c', 'd', 'e'])

        survey1 = Survey([])
        survey2 = Survey([q1, q2])

        # case 1: empty survey._criteria
        assert survey1._weights == {}
        assert not survey1.set_weight(2, q1)

        # case 2: question in survey._criteria
        assert survey2._weights == {q1_id: 1, q2_id: 1}

        assert survey2.set_weight(2, q1)
        assert survey2.set_weight(3, q2)

        assert survey2._weights == {q1_id: 2, q2_id: 3}

        # case 3: question not in survey._criteria
        assert survey2._weights == {q1_id: 1, q2_id: 1}

        assert not survey2.set_weight(2, q3)
        assert not survey2.set_weight(3, q4)

        assert survey2._weights == {q1_id: 2, q2_id: 3}

    def test__get_weight(self) -> None:
        q1 = MultipleChoiceQuestion(1, 'what?', ['a', 'b', 'c'])
        q2 = YesNoQuestion(2, 'how?')
        q3 = NumericQuestion(3, 'when?', -10, 25)
        q4 = CheckboxQuestion(4, 'why?', ['a', 'b', 'c', 'd', 'e'])

        survey = Survey([q1, q2, q3, q4])

        assert survey._get_weight(q1) == 1
        assert survey._get_weight(q2) == 1
        assert survey._get_weight(q3) == 1
        assert survey._get_weight(q4) == 1

        survey.set_weight(2, q1)
        survey.set_weight(3, q2)
        survey.set_weight(0, q3)
        survey.set_weight(5, q4)

        assert survey._get_weight(q1) == 2
        assert survey._get_weight(q2) == 3
        assert survey._get_weight(q3) == 0
        assert survey._get_weight(q4) == 5

    def test_score_students(self) -> None:
        s1 = Student(1, 'Misha')
        s2 = Student(2, 'Diane')

        q1 = MultipleChoiceQuestion(1, 'what?', ['a', 'b', 'c'])
        q2 = YesNoQuestion(2, 'how?')
        q3 = NumericQuestion(3, 'when?', -10, 25)
        q4 = CheckboxQuestion(4, 'why?', ['a', 'b', 'c', 'd', 'e'])

        survey = Survey([q1, q2, q3, q4])

        s1_ans_q1 = Answer('a')
        s1_ans_q2 = Answer(True)
        s1_ans_q3 = Answer(20)
        s1_ans_q4 = Answer(['c', 'a', 'e'])

        s1.set_answer(q1, s1_ans_q1)
        s1.set_answer(q2, s1_ans_q2)
        s1.set_answer(q3, s1_ans_q3)
        s1.set_answer(q4, s1_ans_q4)

        s2_ans_q1 = Answer('b')
        s2_ans_q2 = Answer(False)
        s2_ans_q3 = Answer(25)
        s2_ans_q4 = Answer(['c', 'e'])

        s2.set_answer(q1, s2_ans_q1)
        s2.set_answer(q2, s2_ans_q2)
        s2.set_answer(q3, s2_ans_q3)
        s2.set_answer(q4, s2_ans_q4)

        assert survey.score_students([s1, s2]) == 32/84

    def test_score_grouping(self) -> None:
        s1, s2 = Student(1, 'Misha'), Student(2, 'Diane')
        s3, s4 = Student(3, 'Krishi'), Student(4, 'Grace')

        q1 = MultipleChoiceQuestion(1, 'what?', ['a', 'b', 'c'])
        q2 = YesNoQuestion(2, 'how?')
        q3 = NumericQuestion(3, 'when?', -10, 25)
        q4 = CheckboxQuestion(4, 'why?', ['a', 'b', 'c', 'd', 'e'])

        survey = Survey([q1, q2, q3, q4])

        s1_ans_q1 = Answer('a')
        s1_ans_q2 = Answer(True)
        s1_ans_q3 = Answer(20)
        s1_ans_q4 = Answer(['c', 'a', 'e'])

        s1.set_answer(q1, s1_ans_q1)
        s1.set_answer(q2, s1_ans_q2)
        s1.set_answer(q3, s1_ans_q3)
        s1.set_answer(q4, s1_ans_q4)

        s2_ans_q1 = Answer('b')
        s2_ans_q2 = Answer(False)
        s2_ans_q3 = Answer(25)
        s2_ans_q4 = Answer(['c', 'e'])

        s2.set_answer(q1, s2_ans_q1)
        s2.set_answer(q2, s2_ans_q2)
        s2.set_answer(q3, s2_ans_q3)
        s2.set_answer(q4, s2_ans_q4)

        s3_ans_q1 = Answer('b')
        s3_ans_q2 = Answer(True)
        s3_ans_q3 = Answer(3)
        s3_ans_q4 = Answer(['c', 'd', 'b'])

        s3.set_answer(q1, s3_ans_q1)
        s3.set_answer(q2, s3_ans_q2)
        s3.set_answer(q3, s3_ans_q3)
        s3.set_answer(q4, s3_ans_q4)

        s4_ans_q1 = Answer('c')
        s4_ans_q2 = Answer(False)
        s4_ans_q3 = Answer(3)
        s4_ans_q4 = Answer(['c', 'e', 'a'])

        s4.set_answer(q1, s4_ans_q1)
        s4.set_answer(q2, s4_ans_q2)
        s4.set_answer(q3, s4_ans_q3)
        s4.set_answer(q4, s4_ans_q4)

        g1 = Group([])
        g2 = Group([s1, s2, s3, s4])
        g3 = Group([s1, s2])

        grouping1 = Grouping()
        grouping2 = Grouping()
        grouping3 = Grouping()

        grouping1.add_group(g1)
        grouping2.add_group(g2)
        grouping3.add_group(g3)

        assert survey.score_grouping(grouping1) == 0.0
        assert survey.score_grouping(grouping2) == 0.40049603174603177
        assert survey.score_grouping(grouping3) == 0.38095238095238093

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
# grouper: Group
###############################################################################


class TestGroup:
    def test___len__(self) -> None:
        s1, s2 = Student(1, 'Misha'), Student(2, 'Diane')
        s3, s4 = Student(3, 'Krishi'), Student(4, 'Grace')

        g1 = Group([s1])
        g2 = Group([s1, s2, s3, s4])
        g3 = Group([s1, s2, s3, s4, s2, s4])

        assert g1.__len__() == 1
        assert g2.__len__() == 4
        assert g3.__len__() == 4

    def test___contains__(self) -> None:
        s1, s2 = Student(1, 'Misha'), Student(2, 'Diane')
        s3, s4 = Student(3, 'Krishi'), Student(4, 'Grace')
        s5, s6 = Student(5, 'Binh'), Student(5, 'Hina')

        g1 = Group([s1, s2, s3, s4])

        assert g1.__contains__(s1)
        assert g1.__contains__(s2)
        assert g1.__contains__(s3)
        assert g1.__contains__(s4)
        assert not g1.__contains__(s5)
        assert not g1.__contains__(s6)

    def test_get_members(self) -> None:
        s1, s2 = Student(1, 'Misha'), Student(2, 'Diane')
        s3, s4 = Student(3, 'Krishi'), Student(4, 'Grace')

        g1 = Group([s1])
        g2 = Group([s1, s2, s3, s4])
        g3 = Group([s1, s2, s3, s4, s2, s4])

        # case 1: no duplicate of Student object
        assert g1.get_members() == [s1]
        assert g2.get_members() == [s1, s2, s3, s4]

        # case 2: same Student object added twice
        assert g3.get_members() == [s1, s2, s3, s4]


###############################################################################
# grouper: Grouping
###############################################################################

class TestGrouping:
    def test_add_group(self) -> None:
        s1, s2 = Student(1, 'Misha'), Student(2, 'Diane')
        s3, s4 = Student(3, 'Krishi'), Student(4, 'Grace')

        g1 = Group([])
        g2 = Group([s1, s2, s3, s4])
        g3 = Group([s1, s2])

        grouping = Grouping()

        # case 1: group contains 0 members -> False
        assert not grouping.add_group(g1)
        assert grouping._groups == []

        # case 2: no violation of representation invariants -> True
        assert grouping.add_group(g2)
        assert grouping._groups == [g2]

        # case 3: student appears in more than 1 group -> False
        assert not grouping.add_group(g3)
        assert grouping._groups == [g2]


###############################################################################
# grouper: AlphaGrouper
###############################################################################

class AlphaGrouper:
    # case 1: group contains 0 members -> False
    # case 2: student appears in more than 1 group -> False
    # case 3: no violation of representation invariants -> True
    def test_make_grouping(self) -> None:

        pass

###############################################################################
# grouper: GreedyGrouper
###############################################################################

class GreedyGrouper:
    # case 1: group contains 0 members -> False
    # case 2: student appears in more than 1 group -> False
    # case 3: no violation of representation invariants -> True
    def test_make_grouping(self) -> None:
        pass
