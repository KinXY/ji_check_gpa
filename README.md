# JI_GPA_CHECK
Check your real GPA in UM-SJTU Joint Institute

## Usage
- Go to `学生成绩查询` on [i.sjtu.edu.cn](https://i.sjtu.edu.cn/)
- Press the `导出` button and export the data as .txt file
- Put the .txt file under this directory
- Run `python main.py`

## Config
- By default, the project calculates the GPA that excludes `RED COURSES`, `PE COURSES` and `HUMANITIES COURSES`. You can modify the type of courses to be excluded in the `bullshit` field of `config.json`. Ttype of courses shown in `课程类别` field on [i.sjtu.edu.cn](https://i.sjtu.edu.cn/) should ve applied, e.g. `公共课程类`.
- By default, the project take the GPA of `A+` as `4.3`, unlike the official setting of JI. You can change the `upgradeA+` field of `config.json` to false to disable this feature.