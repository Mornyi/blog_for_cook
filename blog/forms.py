from django import forms
from django.utils.html import escape
from .models import Comment  # Импорт модели, а не формы


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={
                'placeholder': 'Ваш комментарий...',
                'rows': 4,
                'class': 'form-control',
            }),
        }

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if not message:
            raise forms.ValidationError("Комментарий не может быть пустым.")
        escaped_message = escape(message.strip())
        return escaped_message
