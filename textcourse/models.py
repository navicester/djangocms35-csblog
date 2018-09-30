from __future__ import unicode_literals

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from markdown_deux import markdown
from django.utils.safestring import mark_safe

# Create your models here.

class CourseQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

class CourseManager(models.Manager):
    def get_queryset(self):
        return CourseQuerySet(self.model, using=self._db)

    def all(self, *args, **kwargs):
        return self.get_queryset().active()


class Course(models.Model):
    title = models.CharField(_('title'), max_length=150, blank=False, null=False)
    abstract = models.TextField(_('abstract'), max_length=500, blank=True, null=True)
    image = models.ImageField(_('image'), upload_to="upload/serial/", blank=True, null=True)
    order = models.IntegerField(_("order"), blank=True, null=True, default=-1)
    active = models.BooleanField(_("active"), default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    objects = CourseManager()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("textcourse:course_detail", kwargs={"pk":self.pk})

    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Course")
        ordering = ['order', '-updated']


class Article(models.Model):
    course = models.ForeignKey(Course, blank=False, null=False)
    title = models.CharField(max_length=120)
    content = models.TextField()
    order = models.IntegerField(_("order"), blank=True, null=True, default=-1)
    active = models.BooleanField(_("active"), default=True)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)
    timestap = models.DateTimeField(auto_now=True, auto_now_add=False)

    def get_index(self):
        node = self
        index = self.order
        if node and node.parent:
            index = "{}.{}".format(self.parent.get_index(), index)
        return index

    def  __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_markdown(self):
        content = self.content
        markdown_content = markdown(content,'recipe')
        return mark_safe(markdown_content)

    @property
    def index(self):
        return self.get_index()

    class Meta:
        abstract = True


class ArticleManager(models.Manager):
    def get_queryset(self):
        return models.query.QuerySet(self.model, using=self._db)

    def root(self, *args, **kwargs):
        return super(ArticleManager,self).filter(parent=None).filter(active=True)

    def all(self, *args, **kwargs):
        return self.get_queryset().filter(active=True)

class MPTTArticle(MPTTModel, Article):

    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by=['order']

    class Meta:
        ordering=['tree_id','lft']

    def get_absolute_url(self):
        course_pk = None
        if self.course and self.course.pk:
            course_pk = self.course.pk
        return reverse("textcourse:article_detail", kwargs={"pk1": course_pk, "pk": self.pk})    

    def  __unicode__(self):
        return "{} - {}".format(self.get_index(), self.title)

    def  __str__(self):
        return "{} - {}".format(self.get_index(), self.title)

    objects = ArticleManager()