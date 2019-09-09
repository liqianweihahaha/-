#### 项目说明

- master分支：账号相关APi层和服务层测试
- release-work分支：作品相关接口测试

#### 测试数据准备

- config目录用于配置测试数据
- user：普通账号配置
- internal_user：内部账号配置
- db：数据库配置

#### .env配置文件

- environment表示测试环境：dev、test、staging、production
- test_phone_number表示测试的手机号，主要用于测试手机号+验证码相关。建议使用自己的手机号
- geetest_v2表示极验2.0状态，on表示开启，off表示未开启

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