I need a CEETIS ATS function that can ask a user an arbitrary number of questions and print out a nice box or printout. Currently, we use report_manual_reading() which prints the result surrounded by a nice outline. However, when we have multiple report values to enter, it gets very messy and uses lots of space. I think we need to create a nice ASCII table with a header, the questions/report fields, the min, the max, and the entered value. Something like:

+---------------------------------------------------------------+
| Reading                       | Min     | Max    | Measured   |
+-------------------------------+---------+--------+------------+
| C-C Insertion Loss at 850nm   | 0.01 dB | 2.0 dB | 1.56 dB    |
| C-C Insertion Loss at 1300nm  | 0.01 dB | 2.0 dB | 1.6754 dB  |
| D-D Insertion Loss at 850nm   | 0.01 dB | 2.0 dB | -1.7545 dB |
+-------------------------------+---------+--------+------------+