#Toy Mooc#

##功能##

- [x] <del>账号注册、登陆与注销</del>
- [x] <del>注册验证与登陆验证</del>
- [x] <del>查看所有课程</del>
- [x] <del>选课，退课</del>


##截图##
![ ](/shoot.png)

##使用##
测试时可以使用`sqlite3`来生成相应的数据库，并使用`south`进行迁移：
```
python manage.py schemamigration login --initial
python manage.py syncdb
python manage.py migrate login
```

##实现##

* 前端：`bootstrap`
* 脚本：`JavaScript`
* ajax支持：`jQuery`
* 后台：`Django`
* 数据库：`sqlite3`
* 数据库迁移：`south`

