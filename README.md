#### 项目说明

- transaction分支维护：统一交易系统、收银台等相关的自动化

#### 测试数据准备

- config目录用于配置测试数据
- user：普通账号配置
- internal_user：内部账号配置
- db：数据库配置

#### .env配置文件

- environment表示测试环境：dev、test、staging、production
- test_phone_number表示测试的手机号，主要用于测试手机号+验证码相关。建议使用自己的手机号

#### 依赖包

- python版本：3.0+
- 安装所有依赖包: `pip install -r requirements.txt`

#### 运行脚本

1. `.env`文件中指定测试环境和配置测试手机号
2. 运行如下命令

```sh
# 运行某目录下的所有测试用例
hrun testcases/account-api --dot-env-path=dev.env

# 运行某个测试用例文件
hrun testcases/account-api/v1/login.yaml --dot-env-path=dev.env

# 指定html报告的路径和名称
hrun testcases/account-api --html-report-name reports/result.html --dot-env-path=dev.env

# 自定义报告模板。默认使用：~\httprunner\templates\report_template.html
hrun testcases/account-api/v1/login.yaml --report-template=templates/report_fail_only.html --dot-env-path=dev.env
hrun testcases/account-api/v1/login.yaml --report-template=templates/extent_reports.html --dot-env-path=dev.env # 引入extent reports
```