#### 框架说明
- 脚手架： hrun --startproject demo
- api： 接口的定义，避免重复定义
- suite: 模块定义
- testcases： 测试用例/测试场景文件
- debugtalk.py: 函数定义
- yaml: 第一级结构收紧必须是4个空格

#### 运行
- hrun testcases --html-report-name reports/result.html

#### 测试数据准备
1. 用户作品：已发布、未发布、临时删除、永久删除
2. 将登录token放在debugtalk.py中避免多个test多次请求登录方法
3. 开始测hi是作品和测试作品后，将作品属性重置
