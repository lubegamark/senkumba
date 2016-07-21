from django.contrib import admin
from django.contrib.auth.models import User


def user_new_str(self):
    return self.username if self.get_full_name() == "" else self.get_full_name()


# Replace the __str__ method in the User class with our new implementation
User.__str__ = user_new_str

admin.site.site_header = 'SENKUMBA'
admin.site.site_title = 'SENKUMBA'
admin.site.index_title = 'SENKUMBA'