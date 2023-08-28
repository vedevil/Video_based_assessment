from django.db import models

class QuestionPack(models.Model):
    org_id = models.CharField(max_length=50)  # Organization ID
    access_id = models.IntegerField(primary_key=True)
    access_status = models.BooleanField(default=True)  # True or False
    s_no = models.IntegerField(default=1)  # Serial Number
    unique_id = models.CharField(max_length=10, unique=True, null=True, blank=True)
    title = models.CharField(max_length=100)
    summary = models.TextField()
    max_attempts = models.PositiveIntegerField()
    min_response_duration = models.PositiveIntegerField()
    max_response_duration = models.PositiveIntegerField()
    submit_screen_title = models.CharField(max_length=100)
    submit_screen_message = models.TextField()
    show_question_numbers = models.BooleanField()
    feedback_url = models.URLField()
    feedback_message = models.TextField()
    feedback_button_text = models.CharField(max_length=50)
    expiration_timestamp = models.BigIntegerField()
    end_timestamp = models.BigIntegerField()
    ended_message = models.TextField()
    require_linkedin = models.BooleanField()
    linkedin_username = models.CharField(max_length=100, blank=True, null=True)
    qp_url = models.URLField(default="NA")
    ques_values = models.TextField(default="NA")
    qp_result = models.CharField(max_length=100,default='NA')
    qp_mssg = models.TextField(default="NA")

    def __str__(self):
        return self.title
    
class Question(models.Model):
    org_id = models.CharField(max_length=50)
    access_id = models.ForeignKey(QuestionPack, on_delete=models.CASCADE)  # Access ID
    ques_id = models.IntegerField()
    ques_text = models.TextField()
    ques_type = models.CharField(max_length=50)
    def __str__(self):
        return self.org_id
    
class AssessmentResult(models.Model):
    org_id = models.CharField(max_length=50)
    assess_id = models.ForeignKey(QuestionPack, on_delete=models.CASCADE)
    result = models.CharField(max_length=20) 
    mssg = models.TextField()
    zip_url = models.URLField()
    logs = models.TextField()
    videos = models.URLField() 

    def __str__(self):
        return f"{self.org_id} - {self.assess_id}"