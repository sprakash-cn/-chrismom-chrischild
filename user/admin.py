# from django.conf.urls import include, url
from django.contrib import admin

# urlpatterns = [
#     url(r"^", include("user.urls")),
#     url(r"^admin/", admin.site.urls),
# ]

from . models import UserProfile,Comment, Reply

admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Reply)