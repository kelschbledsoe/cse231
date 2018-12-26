scores_file = open("scores.txt") 

data = []
print ("{:21s}{:6s}{:6s}{:6s}{:6s}{:>9s}".format("Name", "Exam1", "Exam2", "Exam3", "Exam4", "Mean"))
exam_1_avg = 0
exam_2_avg = 0
exam_3_avg = 0
exam_4_avg = 0

for line in scores_file: 
    name = line[:20].strip() 
    data_line = [int(x) for x in line [21:].split()]
    exam_1 = data_line [0] 
    exam_1_avg += data_line [0] 
    exam_2 = data_line [1] 
    exam_2_avg += data_line [1]
    exam_3 = data_line [2]
    exam_3_avg += data_line [2]
    exam_4 = data_line [3]
    exam_4_avg += data_line [3]
    total = sum(data_line)
    length = len(data_line)
    average = total/length
    
    student = (name, exam_1, exam_2, exam_3, exam_4, average)
    data.append(student) 

data = sorted(data) 
for tup in data: 
    print ("{:20s}{:6d}{:6d}{:6d}{:6d}{:10.2f}".format(tup[0], tup[1], tup[2], tup[3], tup[4], tup[5])) 
 
    
print("{:20s}{:6.1f}{:6.1f}{:6.1f}{:6.1f}".format("Exam Mean", exam_1_avg/5,\
      exam_2_avg/5, exam_3_avg/5, exam_4_avg/5))