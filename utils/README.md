# 文件内容介绍
文件目录如下
```
.
├── README.md
├── crypt.py
├── db_handling.py
├── init_db.sql
├── mail_handling.py
└── request_handling.py

0 directories, 6 files
```

`crypt.py` 包含了加密所需要的function，包括加密token，解密token，验证email所需要的token等。

`db_handling.py` 包含了执行database语句的function，并把结果修改成dict的形式返回。

`mail_handling.py`发送邮件所需要的function，`send` 这个function

`request_handling.py` 处理请求和得到请求参数，header和文件的操作的function。
