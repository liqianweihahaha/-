# 根据不同的测试环境，获取不同的域名
# return dict
def get_hosts(env):
    if env == 'dev':
        tiger_api_host = 'https://backend-dev.codemao.cn'
        # tiger_api_host = 'https://dev-account-api.codemao.cn'
        platform_tiger_api_host = 'http://dev-internal.platform.codemao.cn'
    elif env == 'test':
        tiger_api_host = 'https://test-api.codemao.cn'
        platform_tiger_api_host = 'http://test-internal.platform.codemao.cn'
    elif env == 'staging':
        tiger_api_host = 'https://backend-test.codemao.cn'
        # tiger_api_host = 'https://staging-account-api.codemao.cn'
        platform_tiger_api_host = 'http://staging-internal.platform.codemao.cn'
    elif env == 'production':
        # tiger_api_host = 'https://api.codemao.cn'
        tiger_api_host = 'https://account-api.codemao.cn'
        platform_tiger_api_host = 'http://internal.platform.codemao.cn'
    # 压测环境
    elif env == 'press':
        tiger_api_host = 'https://press-api.codemao.cn'
        platform_tiger_api_host = 'http://press-internal.platform.codemao.cn'
    # 预演环境
    elif env == 'preview':
        tiger_api_host = 'https://preview-api.codemao.cn'
        platform_tiger_api_host = 'http://preview-internal.platform.codemao.cn'
    return dict(tiger_api_host=tiger_api_host, platform_tiger_api_host=platform_tiger_api_host)

# 判断是否是dev或者test环境
def is_dev_or_test_environment(env):
    stat = True if env not in ('staging', 'production') else False
    return stat

# 判断是否是dev 环境
def is_dev_environment(env):
    stat = True if env == 'dev' else False
    return stat
