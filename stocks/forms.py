from tkinter import Widget
from django import forms

class FeedBack(forms.Form):
    name = forms.charField(label = ' First name ' ,min_length=10, max_lenght=10, widget=forms.TextInput(attrs={'class': 'form-control mb-3' , 'placeholder': 'First name', 'id':'first_name'}))
    email = forms.EmailField(label = ' Email ', widget=forms.EmailInput(attrs={'class': 'form-control mb-3' , 'placeholder': 'Email', 'id':'email'}))
    feedback = forms.CharField(label = ' Feedback ', widget=forms.Textarea(attrs={'class': 'form-control mb-3' ,'row':'5', 'placeholder': 'Feedback', 'id':'feedback'}))

    def send_email(self):
        send_feedback_task.delay(
            self.cleaned_data['name'],
            self.cleaned_data['email'],
            self.cleaned_data['feedback']
        )