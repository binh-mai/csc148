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
"""
import json
import os
import pickle
import sys
from time import time
from typing import Any
from time import sleep
import multiprocessing

import numpy as np
import pandas as pd
import plotly.express as px

import course
import criterion
import grouper
import survey


def _load_criterion(data: dict[str, Any]) -> criterion.Criterion:
    """ Return a criterion created using the information in <data> """
    args = data.get('args', [])
    criterion_ = getattr(criterion, data['class'])(*args)
    return criterion_


def load_survey(data: dict[str, Any]) -> survey.Survey:
    """ Return a survey created using the information in <data>"""
    questions = {}
    criteria = {}
    weights = {}
    for q_data in data['questions']:
        args = q_data['question'].get('args', [])
        question = getattr(survey, q_data['question']['class'])(*args)
        questions[question.id] = question
        weight = q_data.get('weight')
        crit_data = q_data.get('criterion')
        if crit_data is not None:
            criteria[question.id] = _load_criterion(crit_data)
        if weight is not None:
            weights[question.id] = weight

    survey_ = survey.Survey(list(questions.values()))
    for id_, criterion_ in criteria.items():
        survey_.set_criterion(criterion_, questions[id_])
    for id_, weight in weights.items():
        survey_.set_weight(weight=weight, question=questions[id_])
    return survey_


def load_course(data: dict[str, Any]) -> course.Course:
    """ Return a course created using the information in <data>"""
    course_name = data['name']
    course_ = course.Course(course_name)
    students = [course.Student(s_data['id'], s_data['name'])
                for s_data in data['students']]
    course_.enroll_students(students)
    return course_


def load_data(json_filename: str) -> dict[str, Any]:
    """ Return data extracted from <json_filename> which is a json file"""
    with open(json_filename) as f:
        data = json.load(f)
    return data


def answer_questions(survey_: survey.Survey, course_: course.Course,
                     data: dict[str, Any]) -> None:
    """ Answer the questions in <survey_> by assigning answers to the
    student in <course_> according to the data in <data>
    """
    students = {s.id: s for s in course_.get_students()}
    questions = {q.id: q for q in survey_.get_questions()}
    for s_data in data['students']:
        student = students[s_data['id']]
        for a_data in s_data['answers']:
            question = questions[a_data['question_id']]
            answer = survey.Answer(a_data['answer'])
            student.set_answer(question, answer)


def all_equal(lst: list[Any]):
    """Return True if all elements in <lst> are equal, False otherwise"""
    return lst[1:] == lst[:-1]


def run_timer() -> None:
    start = time()
    sys.stdout.write(f'\rRunning Time: {0.000}s')
    while True:
        sys.stdout.write(f'\rRunning Time: {time() - start:.3f}s')
        sleep(.1)
        sys.stdout.flush()


def create_group_comparison_plot(groupers_: list[grouper.Grouper],
                                 course_: course.Course,
                                 survey_: survey.Survey,
                                 include_groups: bool = True,
                                 include_mean: bool = True,
                                 include_std: bool = True,
                                 include_min_over_max: bool = True,
                                 ) -> None:
    """ Plots a bar chart of all the group scores generated by each group in
    ascending order of group number.
    @param groupers_: list of groupers to compare
    @param course_: the course to use for scoring groups
    @param survey_: the survey to use for scoring groups
    @param include_groups: Add bar groups for each group (default True),
    Note that this may lead to non visually appealing results with many groups
    @param include_mean: Add bar group for mean group score of each grouper
    (default True)
    @param include_std: Add bar group for standard deviation of group score of
    each grouper (default True)
    @param include_min_over_max: Add bar group for minimum group score divided
    by the maximum group score of each grouper (default True)
    """
    msg1 = 'At least one of include_groups, include_mean, include_std or ' + \
           'include_min_over_max must be True'
    msg2 = 'All groupers must have the same group size'
    assert any([include_groups, include_mean,
                include_std, include_min_over_max]), msg1
    assert all_equal([x.group_size for x in groupers_]), msg2
    group_names = [str(g).split()[0].split('.')[1] for g in groupers_]
    groupings = []
    for g, name in zip(groupers_, group_names):
        print('-' * 60)
        print(f'Running {name}')
        t = time()
        proc = None
        try:
            proc = multiprocessing.Process(target=run_timer)
            proc.start()
        except pickle.PicklingError:
            pass

        grouping = g.make_grouping(course=course_, survey=survey_)

        if isinstance(proc, multiprocessing.Process):
            proc.terminate()

        print(f'\n{name} took {time() - t:.5f} seconds')
        groupings.append(grouping)

    scores = [[survey_.score_students(g.get_members())
               for g in grouping.get_groups()]
              for grouping in groupings]
    total_scores = [sum(s) for s in scores]
    ordering = sorted(range(len(total_scores)), key=lambda k: total_scores[k])
    total_scores = [total_scores[i] for i in ordering]
    group_names = [group_names[i] for i in ordering]
    scores = [scores[i] for i in ordering]
    mean_scores = [s / len(scores[0]) for s in total_scores]

    data = []
    if include_groups:
        for algo_idx, algo in enumerate(group_names):
            for group_idx, score in enumerate(scores[algo_idx]):
                data.append(dict(Algorithm=algo,
                                 Metric=f'Group {group_idx + 1}',
                                 Score=score))

    for algo_idx, algo in enumerate(group_names):
        if include_mean:
            data.append(
                dict(Algorithm=algo, Metric='Mean',
                     Score=mean_scores[algo_idx]))
        if include_std:
            data.append(
                dict(Algorithm=algo, Metric='Deviation',
                     Score=np.std(scores[algo_idx])))
        if include_min_over_max:
            data.append(
                dict(Algorithm=algo, Metric='Min/Max',
                     Score=min(scores[algo_idx]) / max(scores[algo_idx])))

    title = ' | '.join([f'{name}: {score:.2f}'
                        for name, score in zip(group_names, mean_scores)][::-1])
    fig = px.bar(pd.DataFrame(data), x='Metric', y='Score', color='Algorithm',
                 barmode='group', title=f'<b>Mean Group Scores</b><br>{title}')

    fig.write_html('group_scores.html')
    print('#' * 60)
    print('Group score dashboard written to', 'file:////' +
          os.path.realpath('group_scores.html'))


if __name__ == '__main__':
    example = 'example'  # change this to one of the four options below
    group_size = 3  # change this to your desired group size

    # the SimulatedAnnealingGrouper may take a long time in the larger examples
    if example == 'example':
        # uses a very short survey
        course_file = 'data/example_course.json'
        survey_file = 'data/example_survey.json'
    elif example == 'general':
        # uses a mix of all three criteria to create a grouping
        course_file = 'data/generated_course.json'
        survey_file = 'data/longer_survey.json'
    elif example == 'lonely':
        # uses only the lonely member criterion
        # The SimulatedAnnealingGrouper will likely take quite awhile on this
        # (45 seconds or more is expected)
        course_file = 'data/generated_course_lonely.json'
        survey_file = 'data/longer_survey_lonely.json'
    elif example == 'heterogeneous':
        # uses only the heterogeneous member criterion
        course_file = 'data/generated_course_hetero.json'
        survey_file = 'data/longer_survey_hetero.json'
    else:
        raise ValueError(f'Unknown example {example}')

    course_data = load_data(course_file)
    survey_data = load_data(survey_file)

    new_survey = load_survey(survey_data)
    new_course = load_course(course_data)
    answer_questions(new_survey, new_course, course_data)

    groupers = [
        grouper.AlphaGrouper(group_size),
        grouper.GreedyGrouper(group_size),
        # try changing the number of iterations and the initial temperature
        # to see how it effects the results
        grouper.SimulatedAnnealingGrouper(group_size, iterations=1000,
                                          initial_temperature=.1)]
    create_group_comparison_plot(groupers,
                                 course_=new_course,
                                 survey_=new_survey)