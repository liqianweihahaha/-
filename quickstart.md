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

#### 经验总结
- `- eq: [content.id, ${str($source_user_id)}]`会报错，解决：`- eq: [content.id, '${str($source_user_id)}']`
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
- 修改数据后判断数据是否更新成功，目前是通过请求某api的返回值确认，而不是数据库操作
- 设置用户名的操作者，设置一次之后用户就无法设置了，怎么设置username为null，使测试账号可以重复使用？？？dev、test可以代码连接数据库吗？
- 直接运行整个文件夹路径，文件执行顺序是随机的
- api定义中怎么添加可选参数？？