import numpy as np
from scipy.integrate import quad

def f(x):
    return np.exp(-x**2/5)

integral, error = quad(f, 0, 6)
F_6 = integral + 6

# for time in self._schedule:
#     time_list.append(time)
#
# else:
#     if time2 in time_list:
#         time_list = time_list[time_list.index(time1):
#                               time_list.index(time2) + 1]
#     else:
#         time_list = time_list[time_list.index(time1):]

# cert_num_dict = {}
# for instr_id in self.instructor_hours(time1, time2):
#     cert_num_dict[instr_id] = 0
#
# # for time in self._schedule:
# #     if time in time_list:
# #         for room in self._schedule[time]:
# #             instr_id = self._schedule[time][room][0].get_id()
# #             cert_num = len(self._schedule[time][room][1]
# #                            .get_required_certificates())
# #             cert_num_dict[instr_id] += cert_num

# class_ = self._schedule[time][room]
# for instr_id in self._instructors:
#     if instr_id not in total_hour:
#         total_hour[instr_id] = 0
#     instr = self._instructors[instr_id]
#     if instr in class_:
#         total_hour[instr_id] += 1

# for time in time_list:
#     classes = self._schedule[time]
#     for room in classes:
#         class_ = classes[room]
#         for instr_id in self._instructors:
#             if instr_id not in total_hour:
#                 total_hour[instr_id] = 0
#             instr = self._instructors[instr_id]
#             if instr in class_:
#                 total_hour[instr_id] += 1

# elif time2 in self._schedule:
#     for time in self._schedule:
#         if time1 <= time <= time2:
#             time_list.append(time)
#
# else:
#     for time in self._schedule:
#         if time1 <= time:
#             time_list.append(time)

# for time in self._schedule:
#     time_list.append(time)

# for instr_id in all_instr_hour:
#     total_cert = 0
#     for time in time_list:
#         classes = self._schedule[time]
#         for room in classes:
#             class_ = classes[room]
#             if self._instructors[instr_id] in class_:
#                 workout_cert = class_[1].get_required_certificates()
#                 total_cert += len(workout_cert)
#     instr_hour = self.instructor_hours(time1, time2)[instr_id]
#     pay = instr_hour * base_rate + BONUS_RATE * total_cert
#     instr_name = self._instructors[instr_id].name
#     instr_pay = (instr_id, instr_name, instr_hour, float(pay))
#     payroll.append(instr_pay)


# else:
#     t1 = time_list.index(time1)
#     if time2 in time_list:
#         t2 = time_list.index(time2) + 1
#         time_list = time_list[t1:t2]
#     else:
#         time_list = time_list[t1:]
