"""
There are a number of grades you can get in a test: A, B, C, D, F.
The percentages are as follows:

A: 90-100%

B: 80-90%

C: 70-80%

D: 60-70%

F: <60%

Determine the grade that a student will get based on the student's score and the maximum score.
Note that the upper limit is not included in the range,
except for the A grade. For example,
a student with 60% will get D, with 70% or 79.9% — C,
but the top score 100% is just A.
The input format:
Two lines: the first with a student's score and the second with the maximum.
The output format:
The grade of the student.
"""

numero = int(input())
numero2 = int(input())
notas = ["A", "B", "C", "D", "F"]

if 0.9 <= numero / numero2 <= 1:
    print(notas[0])
elif 0.8 <= numero / numero2 < 0.9:
    print(notas[1])
elif 0.7 <= numero / numero2 < 0.8:
    print(notas[2])
elif 0.6 <= numero / numero2 < 0.7:
    print(notas[3])
else:
    print(notas[4])
