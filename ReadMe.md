启动项目：
在项目根目录下，初始化 python manage.py startapp booktest

在models中定义模型

运行 python manage.py runserver

生成迁移：先在settings.py中INSTALLED_APPS注册项目。再执行

```python
python manage.py makemigrations
```
执行迁移：
```python
python manage.py migrate
```

测试数据库：python manage.py shell 进入shell进行测试

```python
from booktest.models import *
from datetime import *
b = BookInfo()
b.btitle = 'abc'
b.bpub_date = datetime(year=1990,month=1,day=12)
b.save()
BookInfo.objects.all()
```
创建管理员：python manage.py createsuperuser

视图：配置路由urls配置  