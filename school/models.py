from django.db import models

from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class App(models.Model):
    slug = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=64, unique=True)
    info = models.TextField()
    summary = models.CharField(max_length=64, unique=True)
    category = models.CharField(max_length=8, unique=False)

    def __str__(self):
        return self.name


class AppRelease(models.Model):
    app = models.ForeignKey(App)
    os_requirement = models.CharField(max_length=16, unique=True)
    released_at = models.DateTimeField()
    release_info = models.TextField()
    download_count = models.IntegerField()


class AppCategory(models.Model):
    slug = models.CharField(max_length=8, unique=True)
    name = models.CharField(max_length=8, unique=True)


class AppDeveloper(models.Model):
    name = models.CharField(max_length=64, unique=True)


class AppTag(models.Model):
    name = models.CharField(max_length=8, unique=True)
