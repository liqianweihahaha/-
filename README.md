#### 框架说明
- 脚手架： hrun --startproject demo
- api： 接口的定义，避免重复定义
- suite: 模块定义
- testcases： 测试用例/测试场景文件
- debugtalk.py: 函数定义
- yaml: 第一级结构收紧必须是4个空格
- Available response attributes: status_code, cookies, elapsed, headers, content, text, json, encoding, ok, reason, url.
- skip，skipIf, skipUnless
- setup_hooks, teardown_hooks

#### 运行
- hrun testcases --html-report-name reports/result.html

#### 测试数据准备
1. 用户作品：已发布、未发布、临时删除、永久删除
2. 将登录token放在debugtalk.py中避免多个test多次请求登录方法
3. 开始测hi是作品和测试作品后，将作品属性重置
4. 执行完某个测试用例后，teardown_hooks将测试数据重置为开始状态


#### 经验总结
- ${p1(${p2})}函数嵌套会解析失败
- variables定义多个变量时，前一个定义的变量并不能被同级后一个变量立马引用到
```
variables:
    - content: aaa
    - work_content: print($content)
```
- python语法报错或者TypeError(例如读取配置文件的字段不存在)或者测试文件的KeyError(例如引用不存在的变量)导致生成html报告失败时，错误提示无法定位出错的地方，例如：`from builtins import *`报错，改成 `from builtins import str,eval`
- 对于逻辑关系比较紧密的用例，可以写在一个文件中，例如：创建作品和删除作品（避免测试过后用户作品数过多）
- `less_than: [content.0.id, content.1.id]`，目标对象content.1.id会被识别为字符串，所以要先extract再比较
- api接口定义中最好填写完整的url，避免测试文件中的base_url和api接口中的域名不一致（例如批量创建用户后，验证用户登录）
- `&timestamp`，url: /api?a=aa&timestamp=21902910，&timestamp会被解析错误，改成：/api?timestamp=21902910&a=aa，可以正常解析到
