# Django-admin-compare

adds an action `compare` to the admin panel on a page with a list of objects.

use somewhere in admin.py:
```
from django_admin_compare.action import compare

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    ordering = ['title']
    actions = [compare]  #add compare in action
```

Use css class `table` `table-compile` for override style.

For example, you can add when you redefine the django template change_list.html.

requires: Django>=3.2 ,<4 but it will probably work on other versions as well
## Page admin change_list
<img src="https://github.com/meat-source/django-admin-compare/blob/master/list_change.jpg" width="450">

## Page admin compare
<img src="https://github.com/meat-source/django-admin-compare/blob/master/list_compare.jpg" width="450">

#### License MIT
