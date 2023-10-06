
from msearch.models import *

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerChoices(choices=ROLE_CHOICE, default=3)
    birthday = models.DateField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    token = models.CharField()

    def __str__(self):
        return '{}'.format(self.user.username)  
    

    @receiver(post_save,sender=User)
    def create_user_profile(sender, instance, created,**kwargs):
        '''
        Info: Method to create the user profile
        '''
        try:
            if created:
                Profile.object.create(user=instance)
        except: 
            pass 


    @receiver(post_save, sender=User)
    def save_user_pofile(sender, instance, **kwargs):
        try: 
            instance.profile.save()
        except:
            pass