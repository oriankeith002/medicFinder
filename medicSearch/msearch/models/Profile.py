
from msearch.models import *

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField(choices=ROLE_CHOICE, default=3)
    birthday = models.DateField(default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=255, null=True, blank=True) 
    # patient can add favourite doctors to his profile
    favorites = models.ManyToManyField(User, blank=True, related_name='favorites');

    # doctor can now add his address and his specialities. 
    specialites = models.ManyToManyField(Speciality, blank=True, related_name="specialities")
    addressess = models.ManyToManyField(Address, blank=True, related_name='addresses');

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