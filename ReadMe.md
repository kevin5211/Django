������Ŀ��
����Ŀ��Ŀ¼�£���ʼ�� python manage.py startapp booktest

��models�ж���ģ��

���� python manage.py runserver

����Ǩ�ƣ�����settings.py��INSTALLED_APPSע����Ŀ����ִ��

```python
python manage.py makemigrations
```
ִ��Ǩ�ƣ�
```python
python manage.py migrate
```

�������ݿ⣺python manage.py shell ����shell���в���

```python
from booktest.models import *
from datetime import *
b = BookInfo()
b.btitle = 'abc'
b.bpub_date = datetime(year=1990,month=1,day=12)
b.save()
BookInfo.objects.all()
```
��������Ա��python manage.py createsuperuser

��ͼ������·��urls����  