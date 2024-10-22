"""Assignment 0: Sample Tests
=== CSC148, Winter 2023 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains sample tests for Assignment 0.

Warning: This is an extremely incomplete set of tests! Add your own tests
to be confident that your code is correct.

Note: this file is to only help you; you will not submit it when you hand in
the assignment.

This code is provided solely for the personal and private use of students taking
CSC148 at the University of Toronto. Copying for purposes other than this use
is expressly prohibited.  All forms of distribution of this code, whether as
given or with any changes, are expressly prohibited.

Authors: Mario Badr, Jonathan Calver, Tom Ginsberg, Diane Horton,
Sophia Huynh, Christine Murad, Misha Schwartz, Jaisie Sin, and Jacqueline Smith.

All of the files in this directory and all subdirectories are:
Copyright (c) 2022 Mario Badr, Jonathan Calver, Tom Ginsberg, Diane Horton,
Sophia Huynh, Christine Murad, Misha Schwartz, Jaisie Sin, and Jacqueline Smith.
"""
import pytest
from gym import Instructor, Gym, WorkoutClass, datetime


class TestInstructor:
    """Test cases for the Instructor class"""

    def test_name(self) -> None:
        instructor = Instructor(1, 'Diane')
        assert instructor.name == 'Diane'

    def test_get_id(self) -> None:
        instructor = Instructor(1, 'Diane')
        assert instructor.get_id() == 1

    def test_get_certificates_empty(self) -> None:
        instructor = Instructor(1, 'Diane')
        assert instructor.get_certificates() == []

    def test_get_certificates_no_mutation(self) -> None:
        instructor = Instructor(1, 'Diane')
        certificates = instructor.get_certificates()
        assert certificates == []

        certificates.append("Cardio 1")
        assert instructor.get_certificates() == []

    def test_add_certificate_single(self) -> None:
        instructor = Instructor(1, 'Diane')

        cert = 'Cardio 1'
        instructor.add_certificate(cert)

        assert instructor.get_certificates() == ['Cardio 1']

    def test_add_certificate_duplicates(self) -> None:
        instructor = Instructor(1, 'Diane')
        cert = 'Cardio 1'

        instructor.add_certificate(cert)
        instructor.add_certificate(cert)

        assert instructor.get_certificates() == ['Cardio 1']

    def test_add_certificate_multiple(self) -> None:
        instructor = Instructor(1, 'Diane')

        instructor.add_certificate('Cardio 1')
        instructor.add_certificate('Aerobics 2')
        instructor.add_certificate('Dance 1')

        assert instructor.get_certificates() == \
               ['Cardio 1', 'Aerobics 2', 'Dance 1']


class TestGym:
    """Test cases for the Gym class"""

    def test_name_doctest(self) -> None:
        ac = Gym('Athletic Centre')
        assert ac.name == 'Athletic Centre'

    def test_add_instructor_doctest(self) -> None:
        ac = Gym('Athletic Centre')
        diane = Instructor(1, 'Diane')
        assert ac.add_instructor(diane) is True

    def test_add_instructor_same_id_different_name(self) -> None:
        ac = Gym('Athletic Centre')
        jack = Instructor(2, 'Jack')
        assert ac.add_instructor(jack) is True

        jane = Instructor(2, 'Jane')
        assert ac.add_instructor(jane) is False

    def test_add_instructor_same_name_different_id(self) -> None:
        ac = Gym('Athletic Centre')
        diane = Instructor(1, 'Diane')
        assert ac.add_instructor(diane) is True

        diane = Instructor(2, 'Diane')
        assert ac.add_instructor(diane) is True

    def test_add_workout_class_doctest(self) -> None:
        ac = Gym('Athletic Centre')
        kickboxing = WorkoutClass('Kickboxing', ['Strength Training'])
        assert ac.add_workout_class(kickboxing) is True

    def test_add_workout_class_multiple(self) -> None:
        ac = Gym('Athletic Centre')
        kickboxing = WorkoutClass('Kickboxing', ['Strength Training'])
        assert ac.add_workout_class(kickboxing) is True

        kickboxing = WorkoutClass('Dancing', ['Dancing Dancing'])
        assert ac.add_workout_class(kickboxing) is True

        yoga = WorkoutClass('Yoga', ['Flexibility', 'Balancing'])
        assert ac.add_workout_class(yoga) is True

    def test_add_workout_class_same_name_same_certs(self) -> None:
        ac = Gym('Athletic Centre')
        kickboxing = WorkoutClass('Kickboxing', ['Strength Training'])
        assert ac.add_workout_class(kickboxing) is True

        kickboxing = WorkoutClass('Kickboxing', ['Strength Training'])
        assert ac.add_workout_class(kickboxing) is False

    def test_add_workout_class_same_name_different_certs(self) -> None:
        ac = Gym('Athletic Centre')
        dancing = WorkoutClass('Dancing', ['Dancing Dancing'])
        assert ac.add_workout_class(dancing) is True

        dancing = WorkoutClass('Dancing', ['Dancing Dancing', 'Popping'])
        assert ac.add_workout_class(dancing) is False

    def test_add_room_doctest(self) -> None:
        ac = Gym('Athletic Centre')
        assert ac.add_room('Dance Studio', 50) is True

    def test_add_room_already_in(self) -> None:
        ac = Gym('Athletic Centre')
        assert ac.add_room('Dance Studio', 50) is True
        assert ac.add_room('Dance Studio', 20) is False

    def test_schedule_workout_class_doctest(self) -> None:
        ac = Gym('Athletic Centre')
        jacqueline = Instructor(1, 'Jacqueline Smith')

        assert ac.add_instructor(jacqueline) is True

        assert jacqueline.add_certificate('Cardio 1') is True

        diane = Instructor(2, 'Diane Horton')
        assert ac.add_instructor(diane) is True
        assert diane.add_certificate('Cardio 1') is True
        assert ac.add_room('Dance Studio', 18) is True
        assert ac.add_room('lower gym', 50) is True

        boot_camp = WorkoutClass('Boot Camp', ['Cardio 1'])
        assert ac.add_workout_class(boot_camp) is True

        tap = WorkoutClass('Intro Tap', [])
        assert ac.add_workout_class(tap) is True

        sep_9_2022_12_00 = datetime(2022, 9, 9, 12, 0)
        assert ac.schedule_workout_class(sep_9_2022_12_00, 'lower gym',
                                         boot_camp.name,
                                         jacqueline.get_id()) is True
        assert ac.schedule_workout_class(sep_9_2022_12_00, 'Dance Studio',
                                         boot_camp.name, diane.get_id()) is True

    def test_schedule_workout_class_instr_not_available(self) -> None:
        ac = Gym('Athletic Centre')
        jacqueline = Instructor(1, 'Jacqueline Smith')

        assert ac.add_instructor(jacqueline) is True

        assert jacqueline.add_certificate('Cardio 1') is True

        assert ac.add_room('Dance Studio', 18) is True
        assert ac.add_room('lower gym', 50) is True

        boot_camp = WorkoutClass('Boot Camp', ['Cardio 1'])
        assert ac.add_workout_class(boot_camp) is True

        tap = WorkoutClass('Intro Tap', [])
        assert ac.add_workout_class(tap) is True

        sep_9_2022_12_00 = datetime(2022, 9, 9, 12, 0)
        assert ac.schedule_workout_class(sep_9_2022_12_00, 'lower gym',
                                         boot_camp.name,
                                         jacqueline.get_id()) is True

        assert ac.schedule_workout_class(sep_9_2022_12_00, 'Dance Studio',
                                         tap.name,
                                         jacqueline.get_id()) is False

    def test_schedule_workout_class_instr_not_qualified_time_not_in_gym(self) \
            -> None:
        ac = Gym('Athletic Centre')
        jacqueline = Instructor(1, 'Jacqueline Smith')

        assert ac.add_instructor(jacqueline) is True

        assert jacqueline.add_certificate('Cardio 1') is True

        assert ac.add_room('lower gym', 50) is True

        boot_camp = WorkoutClass('Boot Camp', ['Cardio 2'])
        assert ac.add_workout_class(boot_camp) is True

        sep_9_2022_12_00 = datetime(2022, 9, 9, 12, 0)
        assert ac.schedule_workout_class(sep_9_2022_12_00, 'lower gym',
                                         boot_camp.name,
                                         jacqueline.get_id()) is False

    def test_schedule_workout_class_instr_not_qualified_time_in_gym(self) -> None:
        ac = Gym('Athletic Centre')
        jacqueline = Instructor(1, 'Jacqueline Smith')

        assert ac.add_instructor(jacqueline) is True

        assert jacqueline.add_certificate('Cardio 1') is True

        diane = Instructor(2, 'Diane Horton')
        assert ac.add_instructor(diane) is True
        assert ac.add_room('Dance Studio', 18) is True
        assert ac.add_room('lower gym', 50) is True

        boot_camp = WorkoutClass('Boot Camp', ['Cardio 1'])
        assert ac.add_workout_class(boot_camp) is True

        tap = WorkoutClass('Intro Tap', ['Tapping'])
        assert ac.add_workout_class(tap) is True
        sep_9_2022_12_00 = datetime(2022, 9, 9, 12, 0)
        assert ac.schedule_workout_class(sep_9_2022_12_00, 'lower gym',
                                         boot_camp.name,
                                         jacqueline.get_id()) is True
        assert ac.schedule_workout_class(sep_9_2022_12_00, 'Dance Studio',
                                         tap.name, diane.get_id()) is False

    def test_schedule_workout_class_room_unavailable(self) -> None:
        ac = Gym('Athletic Centre')
        jacqueline = Instructor(1, 'Jacqueline Smith')

        assert ac.add_instructor(jacqueline) is True

        assert jacqueline.add_certificate('Cardio 1') is True

        diane = Instructor(2, 'Diane Horton')
        assert ac.add_instructor(diane) is True
        assert ac.add_room('lower gym', 50) is True

        boot_camp = WorkoutClass('Boot Camp', ['Cardio 1'])
        assert ac.add_workout_class(boot_camp) is True

        tap = WorkoutClass('Intro Tap', [])
        assert ac.add_workout_class(tap) is True
        sep_9_2022_12_00 = datetime(2022, 9, 9, 12, 0)
        assert ac.schedule_workout_class(sep_9_2022_12_00, 'lower gym',
                                         boot_camp.name,
                                         jacqueline.get_id()) is True
        assert ac.schedule_workout_class(sep_9_2022_12_00, 'lower gym',
                                         tap.name, diane.get_id()) is False

    def test_register_doctest(self) -> None:
        ac = Gym('Athletic Centre')
        diane = Instructor(1, 'Diane')

        assert diane.add_certificate('Cardio 1') is True
        assert ac.add_instructor(diane) is True

        assert ac.add_room('Dance Studio', 50) is True
        boot_camp = WorkoutClass('Boot Camp', ['Cardio 1'])
        assert ac.add_workout_class(boot_camp) is True

        sep_9_2022_12_00 = datetime(2022, 9, 9, 12, 0)
        assert ac.schedule_workout_class(sep_9_2022_12_00,
                                         'Dance Studio',
                                         boot_camp.name,
                                         diane.get_id()) is True

        assert ac.register(sep_9_2022_12_00, 'Philip', 'Boot Camp') is True
        assert ac.register(sep_9_2022_12_00, 'Philip', 'Boot Camp') is False

    def test_register_room_unavailable(self) -> None:
        ac = Gym('Athletic Centre')
        diane = Instructor(1, 'Diane')

        assert diane.add_certificate('Cardio 1') is True
        assert ac.add_instructor(diane) is True

        assert ac.add_room('Dance Studio', 1) is True
        boot_camp = WorkoutClass('Boot Camp', ['Cardio 1'])
        assert ac.add_workout_class(boot_camp) is True

        sep_9_2022_12_00 = datetime(2022, 9, 9, 12, 0)
        assert ac.schedule_workout_class(sep_9_2022_12_00,
                                         'Dance Studio',
                                         boot_camp.name,
                                         diane.get_id()) is True

        assert ac.register(sep_9_2022_12_00, 'Philip', 'Boot Camp') is True
        assert ac.register(sep_9_2022_12_00, 'Janey', 'Boot Camp') is False

    def test_register_same_class_different_times(self) -> None:
        ac = Gym('Athletic Centre')
        diane = Instructor(1, 'Diane')

        assert diane.add_certificate('Cardio 1') is True
        assert ac.add_instructor(diane) is True

        assert ac.add_room('Dance Studio', 20) is True
        boot_camp = WorkoutClass('Boot Camp', ['Cardio 1'])
        assert ac.add_workout_class(boot_camp) is True

        sep_9_2022_12_00 = datetime(2022, 9, 9, 12, 0)
        sep_9_2022_13_00 = datetime(2022, 9, 9, 13, 0)
        assert ac.schedule_workout_class(sep_9_2022_12_00,
                                         'Dance Studio',
                                         boot_camp.name,
                                         diane.get_id()) is True
        assert ac.schedule_workout_class(sep_9_2022_13_00,
                                         'Dance Studio',
                                         boot_camp.name,
                                         diane.get_id()) is True
        assert ac.register(sep_9_2022_12_00, 'Philip', 'Boot Camp') is True
        assert ac.register(sep_9_2022_13_00, 'Philip', 'Boot Camp') is True

    def test_register_room_available_and_full(self) -> None:
        ac = Gym('Athletic Centre')
        diane = Instructor(1, 'Diane')
        jacqueline = Instructor(2, 'Jacqueline Smith')

        assert jacqueline.add_certificate('Cardio 1') is True
        assert diane.add_certificate('Cardio 1') is True

        assert ac.add_instructor(diane) is True
        assert ac.add_instructor(jacqueline) is True

        assert ac.add_room('Dance Studio', 3) is True
        assert ac.add_room('lower gym', 1) is True
        boot_camp = WorkoutClass('Boot Camp', ['Cardio 1'])
        assert ac.add_workout_class(boot_camp) is True

        sep_9_2022_12_00 = datetime(2022, 9, 9, 12, 0)
        assert ac.schedule_workout_class(sep_9_2022_12_00,
                                         'Dance Studio',
                                         boot_camp.name,
                                         diane.get_id()) is True
        assert ac.schedule_workout_class(sep_9_2022_12_00,
                                         'lower gym',
                                         boot_camp.name,
                                         jacqueline.get_id()) is True
        assert ac.register(sep_9_2022_12_00, 'Philip', 'Boot Camp') is True
        assert ac.register(sep_9_2022_12_00, 'Janey', 'Boot Camp') is True
        assert len(ac._schedule[sep_9_2022_12_00]['Dance Studio'][2]) == 2

        assert ac.register(sep_9_2022_12_00, 'Katie', 'Boot Camp') is True
        assert ac.register(sep_9_2022_12_00, 'Dan', 'Boot Camp') is True
        assert len(ac._schedule[sep_9_2022_12_00]['lower gym'][2]) == 1

        assert ac.register(sep_9_2022_12_00, 'Harry', 'Boot Camp') is False

    def test_instructor_hours_doctest(self) -> None:
        ac = Gym('Athletic Centre')
        diane = Instructor(1, 'Diane')
        david = Instructor(2, 'David')

        assert diane.add_certificate('Cardio 1') is True
        assert ac.add_instructor(diane) is True
        assert ac.add_instructor(david) is True

        assert ac.add_room('Dance Studio', 50) is True
        boot_camp = WorkoutClass('Boot Camp', ['Cardio 1'])
        assert ac.add_workout_class(boot_camp) is True

        t1 = datetime(2019, 9, 9, 12, 0)
        assert ac.schedule_workout_class(t1, 'Dance Studio',
                                         boot_camp.name, 1) is True
        t2 = datetime(2019, 9, 10, 12, 0)

        assert ac.instructor_hours(t1, t2) == {1: 1, 2: 0}
        assert ac.schedule_workout_class(t2, 'Dance Studio',
                                         boot_camp.name, 1) is True
        assert ac.instructor_hours(t1, t2) == {1: 2, 2: 0}

    def test_instructor_no_class_no_instructor_time_not_in_schedule(self) -> None:
        ac = Gym('Athletic Centre')
        t1 = datetime(2019, 9, 9, 12, 0)
        t2 = datetime(2019, 9, 10, 12, 0)
        assert ac.instructor_hours(t1, t2) == {}

    def test_instructor_hours_doctest_additional(self) -> None:
        ac = Gym('Athletic Centre')
        diane = Instructor(1, 'Diane')
        david = Instructor(2, 'David')
        janey = Instructor(3, 'Janey')

        assert diane.add_certificate('Cardio 1') is True
        assert david.add_certificate('Cardio 1') is True
        assert david.add_certificate('Tapping') is True
        assert janey.add_certificate('Tapping') is True

        assert ac.add_instructor(diane) is True
        assert ac.add_instructor(david) is True
        assert ac.add_instructor(janey) is True

        assert ac.add_room('Dance Studio', 50) is True
        assert ac.add_room('lower gym', 20) is True

        boot_camp = WorkoutClass('Boot Camp', ['Cardio 1'])
        assert ac.add_workout_class(boot_camp) is True

        dance = WorkoutClass('Dance', ['Tapping'])
        assert ac.add_workout_class(dance) is True

        t1 = datetime(2019, 9, 9, 12, 0)
        t2 = datetime(2019, 9, 9, 14, 0)
        t3 = datetime(2019, 9, 10, 9, 0)
        t4 = datetime(2019, 9, 13, 8, 0)
        t5 = datetime(2019, 9, 14, 12, 0)

        assert ac.schedule_workout_class(t1, 'Dance Studio',
                                         boot_camp.name, 1) is True

        assert ac.schedule_workout_class(t2, 'lower gym',
                                         boot_camp.name, 2) is True

        assert ac.schedule_workout_class(t3, 'Dance Studio',
                                         dance.name, 2) is True

        assert ac.schedule_workout_class(t4, 'Dance Studio',
                                         boot_camp.name, 1) is True

        assert ac.schedule_workout_class(t5, 'Dance Studio',
                                         boot_camp.name, 1) is True

        assert ac.instructor_hours(t1, t3) == {1: 1, 2: 2, 3: 0}
        assert ac.instructor_hours(t1, t5) == {1: 3, 2: 2, 3: 0}
        assert ac.instructor_hours(t3, t5) == {1: 2, 2: 1, 3: 0}

    def test_payroll_doctest(self) -> None:
        ac = Gym('Athletic Centre')
        diane = Instructor(1, 'Diane')
        david = Instructor(2, 'David')

        assert diane.add_certificate('Cardio 1') is True
        assert ac.add_instructor(david) is True
        assert ac.add_instructor(diane) is True

        assert ac.add_room('Dance Studio', 50) is True
        boot_camp = WorkoutClass('Boot Camp', ['Cardio 1'])
        assert ac.add_workout_class(boot_camp) is True

        t1 = datetime(2019, 9, 9, 12, 0)
        t2 = datetime(2019, 9, 10, 12, 0)

        assert ac.schedule_workout_class(t1, 'Dance Studio',
                                         boot_camp.name, 1) is True
        assert ac.payroll(t1, t2, 25.0) == \
               [(1, 'Diane', 1, 26.5), (2, 'David', 0, 0.0)]

    def test_payroll_no_instructor_time_not_in_schedule(self) -> None:
        ac = Gym('Athletic Centre')
        t1 = datetime(2019, 9, 9, 12, 0)
        t2 = datetime(2019, 9, 10, 12, 0)
        assert ac.payroll(t1, t2, 20) == []

    def test_payroll_additional(self) -> None:
        ac = Gym('Athletic Centre')
        diane = Instructor(1, 'Diane')
        david = Instructor(2, 'David')
        janey = Instructor(3, 'Janey')
        harry = Instructor(4, 'Harry')

        assert diane.add_certificate('Cardio 1') is True
        assert david.add_certificate('Cardio 1') is True
        assert david.add_certificate('Tapping') is True
        assert janey.add_certificate('Tapping') is True
        assert janey.add_certificate('Flexibility') is True
        assert janey.add_certificate('Balancing') is True

        assert ac.add_instructor(diane) is True
        assert ac.add_instructor(david) is True
        assert ac.add_instructor(janey) is True
        assert ac.add_instructor(harry) is True

        assert ac.add_room('Dance Studio', 50) is True
        assert ac.add_room('lower gym', 20) is True

        boot_camp = WorkoutClass('Boot Camp', ['Cardio 1'])
        assert ac.add_workout_class(boot_camp) is True

        dance = WorkoutClass('Dance', ['Tapping'])
        assert ac.add_workout_class(dance) is True

        yoga = WorkoutClass('Yoga', ['Flexibility', 'Balancing'])
        assert ac.add_workout_class(yoga) is True

        t1 = datetime(2019, 9, 9, 12, 0)
        t2 = datetime(2019, 9, 9, 14, 0)
        t3 = datetime(2019, 9, 10, 9, 0)
        t4 = datetime(2019, 9, 13, 8, 0)
        t5 = datetime(2019, 9, 14, 12, 0)

        assert ac.schedule_workout_class(t1, 'Dance Studio',
                                         boot_camp.name, 1) is True

        assert ac.schedule_workout_class(t2, 'lower gym',
                                         boot_camp.name, 2) is True

        assert ac.schedule_workout_class(t3, 'Dance Studio',
                                         dance.name, 2) is True

        assert ac.schedule_workout_class(t3, 'lower gym',
                                         dance.name, 3) is True

        assert ac.schedule_workout_class(t4, 'Dance Studio',
                                         boot_camp.name, 1) is True

        assert ac.schedule_workout_class(t4, 'lower gym',
                                         yoga.name, 3) is True

        assert ac.schedule_workout_class(t5, 'Dance Studio',
                                         boot_camp.name, 1) is True

        assert ac.payroll(t1, t4, 20) == [(1, 'Diane', 2, 43.0), (2, 'David', 2, 46.0),
                                          (3, 'Janey', 2, 49.0), (4, 'Harry', 0, 0.0)]
        assert ac.payroll(t4, t5, 25) == [(1, 'Diane', 2, 53.0), (2, 'David', 0, 0.0),
                                          (3, 'Janey', 1, 29.5), (4, 'Harry', 0, 0.0)]
        assert ac.payroll(t2, t4, 15) == [(1, 'Diane', 1, 16.5), (2, 'David', 2, 36.0),
                                          (3, 'Janey', 2, 39.0), (4, 'Harry', 0, 0.0)]

    def test_is_instructor_name_unique_doctest(self) -> None:
        ac = Gym('Athletic Centre')

        first_hire = Instructor(1, 'Diane')
        assert ac.add_instructor(first_hire) is True
        assert ac._is_instructor_name_unique(first_hire) is True

        second_hire = Instructor(2, 'Diane')
        assert ac.add_instructor(second_hire) is True

        assert ac._is_instructor_name_unique(first_hire) is False
        assert ac._is_instructor_name_unique(second_hire) is False

        third_hire = Instructor(3, 'Tom')
        assert ac._is_instructor_name_unique(third_hire) is True

    def test_is_instructor_name_unique_diff_name_same_id(self) -> None:
        ac = Gym('Athletic Centre')

        first_hire = Instructor(1, 'Diane')
        assert ac.add_instructor(first_hire) is True
        assert ac._is_instructor_name_unique(first_hire) is True

        second_hire = Instructor(1, 'David')
        assert ac.add_instructor(second_hire) is False
        assert ac._is_instructor_name_unique(first_hire) is True

    def test_offerings_at_doctest(self) -> None:
        ac = Gym('Athletic Centre')

        diane1 = Instructor(1, 'Diane')
        assert diane1.add_certificate('Cardio 1') is True

        diane2 = Instructor(2, 'Diane')
        david = Instructor(3, 'David')
        assert david.add_certificate('Strength Training') is True

        assert ac.add_instructor(diane1) is True
        assert ac.add_instructor(diane2) is True
        assert ac.add_instructor(david) is True

        assert ac.add_room('Dance Studio', 50) is True
        assert ac.add_room('Room A', 20) is True

        boot_camp = WorkoutClass('Boot Camp', ['Cardio 1'])
        assert ac.add_workout_class(boot_camp) is True
        kickboxing = WorkoutClass('KickBoxing', ['Strength Training'])
        assert ac.add_workout_class(kickboxing) is True

        t1 = datetime(2022, 9, 9, 12, 0)
        assert ac.schedule_workout_class(t1, 'Dance Studio',
                                         boot_camp.name, 1) is True
        assert ac.schedule_workout_class(t1, 'Room A',
                                         kickboxing.name, 3) is True

        assert ac.offerings_at(t1) == [
            {'Date': 'Friday, 2022-09-09', 'Time': '12:00',
             'Class': 'Boot Camp', 'Room': 'Dance Studio',
             'Registered': 0, 'Available': 50, 'Instructor': 'Diane (1)'},
            {'Date': 'Friday, 2022-09-09', 'Time': '12:00',
             'Class': 'KickBoxing', 'Room': 'Room A', 'Registered': 0,
             'Available': 20, 'Instructor': 'David'}
        ]

    def test_offerings_at_time_point_not_in_schedule(self) -> None:
        ac = Gym('Athletic Centre')
        diane1 = Instructor(1, 'Diane')
        assert ac.add_instructor(diane1) is True
        assert diane1.add_certificate('Cardio 1') is True

        assert ac.add_room('Dance Studio', 50) is True
        boot_camp = WorkoutClass('Boot Camp', ['Cardio 1'])
        assert ac.add_workout_class(boot_camp) is True

        t1 = datetime(2022, 9, 9, 12, 0)
        t2 = datetime(2022, 9, 9, 14, 0)
        assert ac.schedule_workout_class(t1, 'Dance Studio', boot_camp.name, diane1.get_id()) \
               is True

        assert ac.offerings_at(t2) == []

    def test_offerings_at_additional(self) -> None:
        ac = Gym('Athletic Centre')

        diane1 = Instructor(1, 'Diane')
        diane2 = Instructor(2, 'Diane')
        david = Instructor(3, 'David')

        assert diane1.add_certificate('Cardio 1') is True
        assert david.add_certificate('Strength Training') is True

        assert ac.add_instructor(diane1) is True
        assert ac.add_instructor(diane2) is True
        assert ac.add_instructor(david) is True

        assert ac.add_room('lower gym', 10) is True
        assert ac.add_room('Room A', 1) is True
        assert ac.add_room('Dance Studio', 2) is True

        boot_camp = WorkoutClass('Boot Camp', ['Cardio 1'])
        assert ac.add_workout_class(boot_camp) is True
        kickboxing = WorkoutClass('KickBoxing', ['Strength Training'])
        assert ac.add_workout_class(kickboxing) is True

        t1 = datetime(2022, 9, 9, 12, 0)
        t2 = datetime(2022, 9, 10, 12, 0)

        assert ac.schedule_workout_class(t1, 'Room A',
                                         boot_camp.name, 1) is True
        assert ac.schedule_workout_class(t1, 'lower gym',
                                         kickboxing.name, 3) is True
        assert ac.schedule_workout_class(t2, 'Dance Studio',
                                         boot_camp.name, 1) is True
        assert ac.schedule_workout_class(t2, 'Room A',
                                         kickboxing.name, 3) is True

        assert ac.register(t1, 'Philip', 'Boot Camp') is True
        assert ac.register(t1, 'Jane', 'KickBoxing') is True
        assert ac.register(t2, 'Philip', 'Boot Camp') is True

        assert ac.offerings_at(t1) == [
            {'Date': 'Friday, 2022-09-09', 'Time': '12:00',
             'Class': 'Boot Camp', 'Room': 'Room A',
             'Registered': 1, 'Available': 0, 'Instructor': 'Diane (1)'},
            {'Date': 'Friday, 2022-09-09', 'Time': '12:00',
             'Class': 'KickBoxing', 'Room': 'lower gym', 'Registered': 1,
             'Available': 9, 'Instructor': 'David'},
        ]

        assert ac.offerings_at(t2) == [
            {'Date': 'Saturday, 2022-09-10', 'Time': '12:00',
             'Class': 'Boot Camp', 'Room': 'Dance Studio', 'Registered': 1,
             'Available': 1, 'Instructor': 'Diane (1)'},
            {'Date': 'Saturday, 2022-09-10', 'Time': '12:00',
             'Class': 'KickBoxing', 'Room': 'Room A',
             'Registered': 0, 'Available': 1, 'Instructor': 'David'}
        ]

    def test_to_schedule_list_doctest(self) -> None:
        ac = Gym('Athletic Centre')

        diane1 = Instructor(1, 'Diane')
        diane2 = Instructor(2, 'Diane')
        david = Instructor(3, 'David')

        assert diane1.add_certificate('Cardio 1') is True
        assert david.add_certificate('Strength Training') is True

        assert ac.add_instructor(diane1) is True
        assert ac.add_instructor(diane2) is True
        assert ac.add_instructor(david) is True

        assert ac.add_room('Studio 1', 20) is True

        boot_camp = WorkoutClass('Boot Camp', ['Cardio 1'])
        assert ac.add_workout_class(boot_camp) is True
        kickboxing = WorkoutClass('KickBoxing', ['Strength Training'])
        assert ac.add_workout_class(kickboxing) is True

        t1 = datetime(2022, 9, 9, 12, 0)
        t2 = datetime(2022, 9, 8, 13, 0)

        assert ac.schedule_workout_class(t1, 'Studio 1', boot_camp.name, 1) is True
        assert ac.schedule_workout_class(t2, 'Studio 1', kickboxing.name, 3) is True

        assert ac.to_schedule_list() == [
            {'Date': 'Thursday, 2022-09-08', 'Time': '13:00',
             'Class': 'KickBoxing', 'Room': 'Studio 1',
             'Registered': 0, 'Available': 20, 'Instructor': 'David'},
            {'Date': 'Friday, 2022-09-09', 'Time': '12:00',
             'Class': 'Boot Camp', 'Room': 'Studio 1', 'Registered': 0,
             'Available': 20, 'Instructor': 'Diane (1)'}
        ]

    def test_to_schedule_list_additional_week_not_specified(self) -> None:
        ac = Gym('Athletic Centre')

        diane1 = Instructor(1, 'Diane')
        diane2 = Instructor(2, 'Diane')
        david = Instructor(3, 'David')

        assert diane1.add_certificate('Cardio 1') is True
        assert david.add_certificate('Strength Training') is True
        assert david.add_certificate('Cardio 1') is True

        assert ac.add_instructor(diane1) is True
        assert ac.add_instructor(diane2) is True
        assert ac.add_instructor(david) is True

        assert ac.add_room('Studio 1', 20) is True
        assert ac.add_room('Dance Studio', 20) is True

        boot_camp = WorkoutClass('Boot Camp', ['Cardio 1'])
        assert ac.add_workout_class(boot_camp) is True
        kickboxing = WorkoutClass('KickBoxing', ['Strength Training'])
        assert ac.add_workout_class(kickboxing) is True

        t1 = datetime(2022, 9, 9, 12, 0)
        t2 = datetime(2022, 9, 8, 13, 0)

        assert ac.schedule_workout_class(t1, 'Studio 1', boot_camp.name, 1) is True
        assert ac.schedule_workout_class(t1, 'Dance Studio', boot_camp.name, 3) is True
        assert ac.schedule_workout_class(t2, 'Dance Studio', kickboxing.name, 3) is True

        assert ac.to_schedule_list() == [
            {'Date': 'Thursday, 2022-09-08', 'Time': '13:00',
             'Class': 'KickBoxing', 'Room': 'Dance Studio',
             'Registered': 0, 'Available': 20, 'Instructor': 'David'},
            {'Date': 'Friday, 2022-09-09', 'Time': '12:00',
             'Class': 'Boot Camp', 'Room': 'Dance Studio',
             'Registered': 0, 'Available': 20, 'Instructor': 'David'},
            {'Date': 'Friday, 2022-09-09', 'Time': '12:00',
             'Class': 'Boot Camp', 'Room': 'Studio 1',
             'Registered': 0, 'Available': 20, 'Instructor': 'Diane (1)'}
        ]

    def test_to_schedule_list_additional_week_specified(self) -> None:
        ac = Gym('Athletic Centre')

        diane1 = Instructor(1, 'Diane')
        diane2 = Instructor(2, 'Diane')
        david = Instructor(3, 'David')

        assert diane1.add_certificate('Cardio 1') is True
        assert david.add_certificate('Strength Training') is True
        assert david.add_certificate('Cardio 1') is True

        assert ac.add_instructor(diane1) is True
        assert ac.add_instructor(diane2) is True
        assert ac.add_instructor(david) is True

        assert ac.add_room('Studio 1', 20) is True
        assert ac.add_room('Dance Studio', 20) is True

        boot_camp = WorkoutClass('Boot Camp', ['Cardio 1'])
        assert ac.add_workout_class(boot_camp) is True
        kickboxing = WorkoutClass('KickBoxing', ['Strength Training'])
        assert ac.add_workout_class(kickboxing) is True

        t0 = datetime(2022, 9, 6, 10, 0)
        t1 = datetime(2022, 9, 9, 12, 0)
        t2 = datetime(2022, 9, 8, 13, 0)
        t3 = datetime(2022, 9, 15, 13, 0)

        assert ac.schedule_workout_class(t0, 'Studio 1', boot_camp.name, 3) is True
        assert ac.schedule_workout_class(t1, 'Studio 1', boot_camp.name, 1) is True
        assert ac.schedule_workout_class(t1, 'Dance Studio', boot_camp.name, 3) is True
        assert ac.schedule_workout_class(t2, 'Studio 1', kickboxing.name, 3) is True
        assert ac.schedule_workout_class(t3, 'Studio 1', kickboxing.name, 3) is True
        assert ac.schedule_workout_class(t3, 'Dance Studio', boot_camp.name, 1) is True

        assert ac.to_schedule_list(t2) == [
            {'Date': 'Tuesday, 2022-09-06', 'Time': '10:00',
             'Class': 'Boot Camp', 'Room': 'Studio 1',
             'Registered': 0, 'Available': 20, 'Instructor': 'David'},
            {'Date': 'Thursday, 2022-09-08', 'Time': '13:00',
             'Class': 'KickBoxing', 'Room': 'Studio 1',
             'Registered': 0, 'Available': 20, 'Instructor': 'David'},
            {'Date': 'Friday, 2022-09-09', 'Time': '12:00',
             'Class': 'Boot Camp', 'Room': 'Dance Studio',
             'Registered': 0, 'Available': 20, 'Instructor': 'David'},
            {'Date': 'Friday, 2022-09-09', 'Time': '12:00',
             'Class': 'Boot Camp', 'Room': 'Studio 1',
             'Registered': 0, 'Available': 20, 'Instructor': 'Diane (1)'}
        ]


if __name__ == '__main__':
    pytest.main(['gym_sample_tests.py'])
