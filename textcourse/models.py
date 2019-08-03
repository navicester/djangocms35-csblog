from __future__ import unicode_literals

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from markdown_deux import markdown
from django.utils.safestring import mark_safe
# from django.conf import settings
from filer.fields.image import FilerImageField

BLANK_CHOICE_DASH = [("", "---------")]

# Create your models here.

class CourseQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

class CourseManager(models.Manager):
    def get_queryset(self):
        return CourseQuerySet(self.model, using=self._db)

    def active(self, *args, **kwargs):
        is_superuser = kwargs.get('is_superuser', None)
        if not is_superuser:
            return self.get_queryset().active()
        return self.get_queryset()


class Course(models.Model):
    title = models.CharField(_('title'), max_length=150, blank=False, null=False)
    abstract = models.TextField(_('abstract'), max_length=500, blank=True, null=True)
    # image = models.ImageField(_('image'), upload_to="upload/serial/", blank=True, null=True)
    cover = FilerImageField(null=True, blank=True,
                           related_name="course_cover")
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
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)

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
        import re
        re_str = "(?<![\[\(\/\w])((http(s)?:\/{2})((www|\w+)\.)?[\w\/\.\%\:]+)(?![\]\)\w\/\.])"
        content = re.sub(re_str, lambda elem: "[{0}]({0})".format(elem.group(0)), content)
        markdown_content = markdown(content,'recipe')
        return mark_safe(markdown_content)

    def get_absolute_url(self, *args, **kwargs):
        return reverse("textcourse:course_detail", kwargs={"pk":self.pk, "pk1":self.course.pk})

    @property
    def index(self):
        return self.get_index()

    @property
    def is_root(self):
        return False if self.parent else True

    class Meta:
        abstract = True


class ArticleManager(models.Manager):
    def get_queryset(self):
        return models.query.QuerySet(self.model, using=self._db)

    def root(self, *args, **kwargs):
        try:
            return self.active(*args, **kwargs).filter(parent=None)
        except:
            return None

    def active(self, *args, **kwargs):
        is_superuser = kwargs.get('is_superuser', None)
        if not is_superuser:        
            return self.get_queryset().filter(active=True)
        return self.get_queryset()

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

    def get_absolute_url_list(self):
        course_pk = None
        if hasattr(self, 'course') and self.course and self.course.pk:
            course_pk = self.course.pk
            return reverse("textcourse:course_detail", kwargs={"pk": course_pk})
        else:
            return reverse("textcourse:course_list", kwargs={})

    def get_absolute_url_update(self):
        course_pk = None
        if self.course and self.course.pk:
            course_pk = self.course.pk
        return reverse("textcourse:article_update", kwargs={"pk1": course_pk, "pk": self.pk})  

    def get_absolute_url_delete(self):
        course_pk = None
        if self.course and self.course.pk:
            course_pk = self.course.pk
        return reverse("textcourse:article_delete", kwargs={"pk1": course_pk, "pk": self.pk}) 

    def  __unicode__(self):
        return "{} - {}".format(self.get_index(), self.title)

    def  __str__(self):
        return "{} - {}".format(self.get_index(), self.title)

    def get_next_by_order(self, *args, **kwargs):
        field = self.__class__._meta.get_field('order')        
        try:
            return self._get_next_or_previous_by_FIELD(field, is_next=True, parent=None, course=self.course)
        except MPTTArticle.DoesNotExist:
            return None

    def get_previous_by_order(self, *args, **kwargs):
        field = self.__class__._meta.get_field('order')
        try:
            return self._get_next_or_previous_by_FIELD(field, is_next=False, parent=None, course=self.course)
        except MPTTArticle.DoesNotExist:
            return None

    @property
    def previous(self): 
        try:
            if self.is_root_node():
                node = self.get_previous_by_order()
                if node:
                    if node.get_children():
                        return node.get_children().last()
                    else:
                        return node
            else:
                if self.get_previous_sibling():
                    if self.get_previous_sibling().get_children():
                        return self.get_previous_sibling().get_children().last()
                    else:
                        return self.get_previous_sibling()
                elif self.parent:
                    return self.parent
                else:
                    pass
        except:
            pass

        return None

    @property
    def next(self):        
        try:
            if self.is_root_node():

                if self.get_children():
                    return self.get_children().first()
                else:
                    return self.get_next_by_order()      
            else:
                if self.get_children():
                    return self.get_children().first()
                elif not self.get_next_sibling():
                    if self.parent.is_root_node():
                        return self.parent.get_next_by_order()
                    else:
                        return self.parent.get_next_sibling()
                else:
                    return self.get_next_sibling()
        except:
            pass

        return None    

    objects = ArticleManager()

def get_article_choice(course):
    CHOICE_LIST = []
    for ins in MPTTArticle.objects.filter(course=course): #course.article_set.all():
        if not (ins, ins) in CHOICE_LIST:
            CHOICE_LIST.append((ins.id, ins))
    # CHOICE_LIST.sort()
    CHOICE_LIST.insert(0, ('', '----'))  
    return CHOICE_LIST    