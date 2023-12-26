import os
import json


def read_config():
    global config
    with open("config.json", "r", encoding="UTF-8") as f:
        config = json.load(f)


def read_data():
    # find the name of the only .txt file under the directory
    files = os.listdir()
    for file in files:
        if file.endswith(".txt"):
            data_file = file
            break
    # read data from the file
    with open(data_file, "r", encoding="UTF-8") as f:
        data = f.read()
    # find the keys from the first line of the file
    keys = data.split("\n")[0].split("\t")
    # find the values from the rest of the file
    lines = data.split("\n")[1:]
    # pop the last empty line
    lines.pop()
    result = {}
    for line in lines:
        values = line.split("\t")
        for i in range(len(keys)):
            if keys[i] not in result:
                result[keys[i]] = []
            result[keys[i]].append(values[i])
    return result


def get_needed_courses(data):
    result = []
    bullshit = config["bullshit"]
    for i, type in enumerate(data["课程类别"]):
        if type in bullshit:
            continue
        else:
            credits = float(data["学分"][i])
            if config["upgradeA+"] and data["成绩"][i] == "A+":
                gpa = 4.3
            else:
                gpa = float(data["绩点"][i])
            result.append({"credits": credits, "gpa": gpa})
    return result


def calc_gpa(data):
    total_credits = 0
    total_summation = 0
    for course in data:
        total_credits += course["credits"]
        total_summation += course["credits"] * course["gpa"]
    return total_summation / total_credits


if __name__ == "__main__":
    read_config()
    data = read_data()
    needed_courses = get_needed_courses(data)
    gpa = calc_gpa(needed_courses)
    print("GPA: {:.2f}".format(gpa))
