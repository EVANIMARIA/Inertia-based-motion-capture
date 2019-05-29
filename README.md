# Inertia-based-motion-capture
# 基于惯性导航的动作捕捉系统与其在交警手势识别上的应用开发
### 项目结构
- 数据采集
  - /serial_code中的serial_code.py
  - 最新数据在/data和/0523中，分别为直行和停止的姿势数据
- 动作分割
- 动作特征提取
  - test3.py, 对data和0523中的数据进行识别， 并将模型保存为.model文件
- 动作识别
  - /serial_code中的th_test2.py为全流程文件， 对实时数据进行处理并调用模型识别
