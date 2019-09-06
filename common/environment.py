# 根据不同的测试环境，获取不同的域名
# return dict
def get_hosts(env):
    if env == 'dev':
        tiger_api_host = 'https://backend-dev.codemao.cn'
        platform_tiger_api_host = 'http://dev-internal.platform.codemao.cn'
        internal_account_api_host = 'https://dev-internal-account-api.codemao.cn'
        transaction_admin_api_host = 'https://dev-api-admin-transaction.codemao.cn'
    elif env == 'test':
        tiger_api_host = 'https://test-api.codemao.cn'
        platform_tiger_api_host = 'http://test-internal.platform.codemao.cn'
        internal_account_api_host = 'https://test-internal-account-api.codemao.cn'
        transaction_admin_api_host = 'https://test-api-admin-transaction.codemao.cn'
    elif env == 'staging':
        tiger_api_host = 'https://backend-test.codemao.cn'
        platform_tiger_api_host = 'http://staging-internal.platform.codemao.cn'
        internal_account_api_host = 'https://staging-internal-account-api.codemao.cn'
        transaction_admin_api_host = 'https://staging-api-admin-transaction.codemao.cn'
    elif env == 'production':
        tiger_api_host = 'https://api.codemao.cn'
        platform_tiger_api_host = 'http://internal.platform.codemao.cn'
        internal_account_api_host = 'https://internal-account-api.codemao.cn'
        transaction_admin_api_host = 'https://api-admin-transaction.codemao.cn'
    return dict(tiger_api_host=tiger_api_host, platform_tiger_api_host=platform_tiger_api_host, 
        internal_account_api_host=internal_account_api_host, transaction_admin_api_host=transaction_admin_api_host)

# 判断是否是dev或者test环境
def is_dev_or_test_env(env):
    return True if env not in ('staging', 'production') else False

# 判断是否是dev 环境
def is_dev_env(env):
    return True if env == 'dev' else False
