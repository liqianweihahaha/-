#### 测试数据准备
1. 用户信息准备：用户名，手机号，邮箱
1. 用户作品：IDE、BOX2.0、WOOD、NEMO（最好存在多个存档记录的）
2. 将登录token放在debugtalk.py中避免多个test多次请求登录方法
3. 开始测hi是作品和测试作品后，将作品属性重置
4. 执行完某个测试用例后，teardown_hooks将测试数据重置为开始状态

#### 依赖包
```
python 3.0+
httprunner==1.5.13, 1.5.14, 1.5.15
```

#### 运行脚本
- 默认测试报告的路径：reports/xx.html
```sh
# 运行某目录下的所有测试用例
hrun testcases/platform-user-tiger

# 运行某个测试用例文件
hrun testcases/platform-user-tiger/get_user_info.yaml

# 指定html报告的路径和名称
hrun testcases/platform-user-tiger --html-report-name reports/result.html
```

#### 注意点
- 退出登录后会导致其他用例的登录token不可用，所以退出登录已登录token需要单独获取
- 账号3.0修改密码，导致source_user_login_token失效，所以使用测试账号2（target_user）测试