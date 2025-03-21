from django.db import models

# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="User Name")
    email = models.EmailField(verbose_name="Email")
    password = models.CharField(max_length=128, verbose_name="Password")
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number")
    age =models.CharField(max_length=15, verbose_name="age")
    address = models.TextField(verbose_name="Address")
    photo = models.ImageField(upload_to='profiles/', verbose_name="Upload Profile", null=True, blank=True)
    otp = models.CharField(max_length=6, default='000000', help_text='Enter OTP for verification')
    otp_status = models.CharField(max_length=15, default='Not Verified', help_text='OTP status')
    status = models.CharField(max_length=15,default='Pending')
    Last_Login_Time = models.TimeField(null = True)
    Last_Login_Date = models.DateField(null = True)
    No_Of_Times_Login = models.IntegerField(default = 0, null = True)

    def __str__(self):
        return self.full_name
    




class FeedbackModel(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)    
    Review = models.CharField(max_length = 1000)
    Rating = models.CharField(max_length = 1000)
    Sentiment = models.CharField(max_length = 1000)
    Feedback_Time = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = 'user_feedback'





        