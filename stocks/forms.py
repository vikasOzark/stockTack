from django import forms
from .tasks import send_feedback_email_task

class FeedBack(forms.Form):
    name = forms.CharField(label = ' First name ' ,min_length=10, max_length=10, widget=forms.TextInput(attrs={'class': 'form-control mb-3' , 'placeholder': 'First name', 'id':'first_name'}))
    email = forms.EmailField(label = ' Email ', widget=forms.EmailInput(attrs={'class': 'form-control mb-3' , 'placeholder': 'Email', 'id':'email'}))
    feedback = forms.CharField(label = ' Feedback ', widget=forms.Textarea(attrs={'class': 'form-control mb-3' ,'row':'5', 'placeholder': 'Feedback', 'id':'feedback'}))

    def send_email(self):
        send_feedback_email_task.delay(
            name=self.cleaned_data['name'],
            email=self.cleaned_data['email'],
            feedback=self.cleaned_data['feedback']
        )