student = {"Student1": {"Name": "ding", "Sex": "Female", "Age": 18, "Score": [78, 82]},
           "Student2": {"Name": "Wang", "Sex": "Male", "Age": 21, "Score": [78, 82]}}
print(student["Student1"])  # 一次性输出全部
print(student["Student1"]["Name"])  # 只输出student1的名字
print(student["Student2"])  # 一次性输出全部
print(student["Student2"]["Score"])  # 只输出student2的得分
print(student["Student2"]["Score"][1])  # 只输出student2的得分2
