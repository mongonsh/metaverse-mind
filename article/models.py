# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from mongoengine import Document, StringField, DateTimeField, IntField
import datetime
import pytz


class Actions(Document):
    action_name_mn = StringField(max_length=100, blank=True, null=True)
    action_name_jp = StringField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actions'


class ArticleStatus(Document):
    name_jp = StringField(max_length=100, blank=True, null=True)
    name_mn = StringField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article_status'


class Articles(Document):
    title_mn = StringField(blank=True, null=True)
    title_jp = StringField(blank=True, null=True)
    content_jp = StringField(blank=True, null=True)
    content_mn = StringField(blank=True, null=True)
    writer_id = IntField(blank=True, null=True)
    published_date = models.DateField(blank=True, null=True)
    state = StringField(max_length=50, blank=True, null=True)
    views_count = IntField(blank=True, null=True)
    media_id = IntField(blank=True, null=True)
    category_id = StringField(blank=True, null=True)
    updated_at = DateTimeField(default=lambda: datetime.datetime.now(pytz.timezone('Asia/Tokyo')))
    delete_flag = IntField(blank=True, null=True)
    impression_id = IntField(blank=True, null=True)
    media_url = StringField(max_length=250, blank=True, null=True)
    thumbnail_url = StringField(max_length=250, blank=True, null=True)
    short_desc = StringField(blank=True, null=True)
    status = IntField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'articles'


class Categories(Document):
    name = StringField(max_length=100, blank=True, null=True)
    name_jp = StringField(max_length=100, blank=True, null=True)
    path_name = StringField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class Impression(Document):
    article_id = IntField(blank=True, null=True)
    views_count = IntField(blank=True, null=True)
    share_count = IntField(blank=True, null=True)
    like_count = IntField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'impression'


class Mediauser(Document):
    username = StringField(max_length=100, blank=True, null=True)
    email = StringField(max_length=200, blank=True, null=True)
    password = StringField(max_length=200, blank=True, null=True)
    role = StringField(max_length=100, blank=True, null=True)
    created_at = DateTimeField(default=lambda: datetime.datetime.now(pytz.timezone('Asia/Tokyo')))
    social_id = IntField(blank=True, null=True)
    profile_url = StringField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mediauser'


class Social(Document):
    user_id = IntField(blank=True, null=True)
    linkedin = StringField(max_length=200, blank=True, null=True)
    facebook = StringField(max_length=256, blank=True, null=True)
    twitter = StringField(max_length=256, blank=True, null=True)
    website = StringField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'social'

class Image(Document):
    media_id = StringField(max_length=500)
    media_url = StringField(max_length=500)
