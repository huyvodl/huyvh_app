from django import forms
from .models import Post
from django.contrib.admin import widgets
class PostForm(forms.ModelForm):
	#published_date = JqSplitDateTimeField(widget=JqSplitDateTimeWidget(attrs={'date_class':'datepicker','time_class':'timepicker'})	
	class Meta:
       	 model = Post
         fields = ('title', 'text','imgfile','published_date')
	# def __init__(self, *args, **kwargs):
	# 	super(PostForm, self).__init__(*args, **kwargs)
	# 	self.fields['published_date'].widget.attrs['class'] = 'datepicker'