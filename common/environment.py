# 根据不同的测试环境，不同的域名
def get_hosts(env):
    if env == 'dev':
        tiger_api_host = 'https://backend-dev.codemao.cn'
        platform_tiger_api_host = 'http://dev-external.platform.codemao.cn'
    elif env == 'test':
        tiger_api_host = "https://test-api.codemao.cn"
        platform_tiger_api_host = 'http://test-internal.platform.codemao.cn'
    elif env == 'staging':
        tiger_api_host = 'https://backend-test.codemao.cn'
        platform_tiger_api_host = 'http://staging-internal.platform.codemao.cn'
    elif env == 'production':
        tiger_api_host = 'https://api.codemao.cn'
        platform_tiger_api_host = 'http://internal.platform.codemao.cn'
    elif env == 'press':
        tiger_api_host = 'https://press-api.codemao.cn'
        platform_tiger_api_host = 'http://press-internal.platform.codemao.cn'
    # 预演环境
    elif env == 'preview':
        tiger_api_host = 'https://preview-api.codemao.cn'
        platform_tiger_api_host = 'http://preview-internal.platform.codemao.cn'
    hosts = {
        'tiger_api_host': tiger_api_host, 
        'platform_tiger_api_host': platform_tiger_api_host
        }
    return hosts