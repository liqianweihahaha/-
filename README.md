#### 测试数据准备

1. 用户信息准备：创建2个用户
2. 用户作品：IDE、BOX2.0、WOOD、NEMO（最好存在多个存档记录的）
3. 将登录token放在debugtalk.py中避免多个test多次请求登录方法
4. 执行完某个测试用例后，teardown_hooks将测试数据重置为开始状态

#### 依赖包

```
python 3.0+
httprunner==2.0+
```
- httprunner 1.5.x版本，可切换到分支hrun1.0，然后运行

#### 运行脚本

1. `.env`文件中指定测试环境和配置测试手机号
2. 运行如下命令

```sh
# 运行某目录下的所有测试用例
hrun testcases/account-api

# 运行某个测试用例文件
hrun testcases/account-api/v1/login.yaml

# 指定html报告的路径和名称
hrun testcases/account-api --html-report-name reports/result.html

# 指定报告模板：例如只输出执行失败的testcase
# 默认使用：~\httprunner\templates\report_template.html
hrun testcases/account-api/v1/login.yaml --report-template=templates/report_fail_only.html
```