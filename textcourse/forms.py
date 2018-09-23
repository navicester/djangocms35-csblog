
from django import forms
from .models import MPTTArticle

class ArticleForm(forms.ModelForm): 

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)

        course = None
        instance = getattr(self, 'instance', None)
        # print instance

        if instance and hasattr(instance, 'course'):
            course = instance.course

        if course:
            try:
                CHOICE_LIST = []
                for ins in MPTTArticle.objects.filter(course=course): #course.article_set.all():
                    if not (ins, ins) in CHOICE_LIST:
                        CHOICE_LIST.append((ins, ins))
                # CHOICE_LIST.sort()
                CHOICE_LIST.insert(0, ('', '----'))
  
                self.fields['parent'].choices = CHOICE_LIST

                # OR
                # self.fields['surface'].choices.insert(0,('', _('Please choose a surface')))

                # https://stackoverflow.com/questions/16464119/django-insert-choice-is-neglected-in-form-init                
            except:
                pass

    class Meta: 
        model = MPTTArticle 
        exclude = []