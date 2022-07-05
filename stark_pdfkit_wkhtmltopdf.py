# +----------------------------------------------------------------------
# | Author:Stark
# +----------------------------------------------------------------------
# | Date:2022/7/5
# +----------------------------------------------------------------------
# | Desc: html生成pdf
# |       依赖库 pip3 install pdfkit 需要安装wkhtmltopdf
# +----------------------------------------------------------------------

import pdfkit


def pdf(url, file):
    path = r'/usr/local/bin/wkhtmltopdf'
    config = pdfkit.configuration(wkhtmltopdf=path)

    # 页眉URl 页脚URl
    options = {
        '--header-html': 'http://demo.com/api/test/header',
        '--footer-html': 'http://demo.com/api/test/footer'
    }

    # url 正文url ，其他参数在options设置
    pdfkit.from_url(url, file, configuration=config, options=options)
    print('完成')


pdf(r'http://demo.com/api/test/test','/demo/out_77.pdf')
