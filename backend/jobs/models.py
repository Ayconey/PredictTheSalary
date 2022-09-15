from django.db import models


# Create your models here.

class Job(models.Model):
    work_year = models.IntegerField()
    experience_level = models.CharField(max_length=5)  # experience levels are:
    # EN Entry-level/Junior, MI Mid-level/Intermediate, SE Senior-level/Expert, EX Executive-level/Director
    employment_type = models.CharField(max_length=5)  # The type of employement for the role: PT Part-time,
    # FT Full-time, CT Contract, FL Freelance
    job_title = models.CharField(max_length=100)
    salary = models.IntegerField()
    salary_currency = models.CharField(max_length=10)
    salary_in_usd = models.IntegerField()
    employee_residence = models.CharField(max_length=100)
    remote_ratio = models.IntegerField()
    company_location = models.CharField(max_length=200)
    company_size = models.IntegerField()

    def __str__(self):
        return self.job_title + ' ' + self.experience_level
