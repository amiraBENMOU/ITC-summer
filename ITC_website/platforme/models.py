from django.db import models
### FIRST CLASS
class POSITION_CHOICES(models.TextChoices):
        member = "member"
        teamLeader= "teamLeader"
        membreBireau= "membreBireau"
        ProjectManager= "ProjectManager"
       
class ITC_Member(models.Model):
 firstName = models.TextField (max_length=10 ,null=False, blank=False)
 lastName= models.TextField (max_length=10,null=False, blank=False)
 age=models.IntegerField()
 fiels_of_study=models.TextField (max_length=10,null=False, blank=False)
 position = models.CharField(max_length=20,choices=POSITION_CHOICES.choices,default= POSITION_CHOICES.member)
 # POSITIONS 
 
class POSITION_CHOICES(models.TextChoices):
        member = "member"
        teamLeader= "teamLeader"
        membreBireau= "membreBireau"
        ProjectManager= "ProjectManager"
       


    

    

