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
- output打印的变量，可以在不同测试用例之间访问

#### hrun1.0 到 2.0

| 不同点 | hrun 1.5.15 | hrun 2.0 |
|----|----|----|
|base_url|可以在config中的request下定义|只能在config下直接定义或者api中直接定义(不能在request下)|
|request|可以在testcase的config中统一配置request的method、url等|只能在test中定义request|
|parameters|可以在testcase中指定|只能在testsuites中指定|
|api定义|通过api和def关键字定义|和test定义一样|
|api调用|通过api关键字和函数名调用，传递函数参数|通过api指定文件路径，variables传递参数|
|test定义|-|必须指定name|
|debugtalk.py|可以直接引用其中定义的变量|不能直接引用其中定义的变量|
|testcase文件内容为空||执行报错|

#### 框架源码学习
- html报告生成：report.py中的render_html_report函数，使用的是jinja2的模板文件templates/report_template.html

#### 经验总结
- `- eq: [content.id, ${str(${source_user_id()})}]`会报错，解决：`- eq: [content.id, '${str(${source_user_id()})}']`
- variables定义多个变量时，前一个定义的变量并不能被同级后一个变量立马引用到，例如下面的写法会报错
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
- 修改数据后判断数据是否更新成功，目前是通过请求某api的返回值确认，而不是数据库操作
- 设置用户名的操作者，设置一次之后用户就无法设置了，怎么设置username为null，使测试账号可以重复使用？？？dev、test可以代码连接数据库吗？
- 直接运行整个文件夹路径，文件执行顺序是随机的
- api定义中不支持默认参数，不支持可选参数
- api定义，request中指定 base_url 不会被识别到，所以要直接在 url 中指定完整路径
- api文件中的yaml文件内容为空会报错
- api文件中的name会覆盖testcases文件test用例中的name
- testcases中yaml文件内容为空，会导致生成报告失败
- 加载顺序：.env文件---》加载testcase中定义的变量(执行其中可执行部分)---》运行testcase
- 读取可能有延迟的接口（例如MQ同步数据），需要添加sleep数据（ ${sleep_N_secs(1)} ）
- 同一个testcase的不同test之间，Cookies是继承的。（例如：第一个test用户登录成功，第二个test中如果不指定headers那么会使用默认的headers即带上Cookie）

#### 错误写法总结

##### 错误写法1
- 预期效果：先执行发送登录验证码接口，再获取验证码，执行验证码登录接口。

```
- test:
    name: 发送登录验证码-手机号未注册
    skipUnless: ${is_dev_or_test()}
    setup_hooks:
        - ${clear_phone_number($unregister_phone_number)}
    api: api/account/v3_for_web/send_login_silence_captcha.yaml
    variables:
        - phone_number: $unregister_phone_number
    validate:
        - eq: [status_code, 204]

- test:
    name: 验证码登录：手机号未注册-验证码正确
    skipUnless: ${is_dev_or_test()}
    api: api/account/v3_for_web/login_silence_by_captcha.yaml
    variables:
        - phone_number: $unregister_phone_number
        - captcha: ${get_captcha_account_v3(login_with_register, $unregister_phone_number)}  # 在执行所有testcase(包括setup_hooks)之前，variables中调用debugtalk.py中的函数会被先执行，调用几次就执行几次
    validate:
        - eq: [status_code, 200]
        - eq: [content.is_first_login, true]
```
- 实际效果：先执行了获取验证码，然后再执行发送验证码，导致获取的验证码为空（原因：test的variables中调用debugtalk.py的函数会在所有用例执行之前先执行）
- 解决方法：执行获取验证码的方法放在request中，而不是variables中，因此只要不复用api即可。

#### Hook
- 测试用例的准备和清理工作没有使用setup_hooks/teardown_hoos，而是直接调用DB层的接口（因为DB层涉及的CRUD操作的接口已经有了）
- 缺点：用例之间耦合性大，依赖于底层的DB操作接口的正确性
- 优点：减少直接操作数据库（并且正式库还没法直接修改表）
- 涉及到手机号注册相关，不会通过解绑接口清空手机号，因为业务限制太多，所以直接操作数据库

#### 注意点
- 退出登录后会导致其他用例中的source_user_login_token失效，所以退出登录用例中的已登录token需要单独获取
- 账号3.0修改密码，导致source_user_login_token失效，所以使用测试账号2（target_user）测试



