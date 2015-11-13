####get git update information,use mail to notice

####use config.py file to config your project
>this is a config.py file<br>

```python
mailto_list = ["416883813@qq.com"] #my mailaddress
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "username"  # 用户名
mail_pass = "userpassword"  # 口令
mail_postfix = "163.com"  # 发件箱的后缀

config_6605 = {
    'Project_name': 'Addison A6604/A6605',
    'server_address': 'git@192.168.128.206:/MT8735_BD2_M',
    'git_path': '/home/lzg/6605/codebase/6605/MT8735_BD2_M',
    'remote_respo': 'origin',
    'mailto_list': ['liuzhigang@huaqin.com',
                    '416883813@qq.com'
                    ]
}

config_test = {
    'Project_name': 'Test',
    'server_address': '/home/lzg/work/gittest/./remote',
    'git_path': '/home/lzg/work/gittest/native',
    'remote_respo': 'origin',
    'mailto_list': ['416883813@qq.com',
                    # '416883813@qq.com'
                    ]
}

```