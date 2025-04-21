from django.db import models
from users.models import CustomUser

# Create your models here.

class Habit(models.Model):

    user = models.ForeignKey(CustomUser, 
                             null=False, 
                             on_delete=models.CASCADE,
                             related_name="user"
                             )
    place = models.CharField(max_length=50,
                              default=None,
                              null=True,
                              blank=True,
                              verbose_name='место выполнения привычки',
                              help_text='место, в котором необходимо выполнять привычку',
                              )
    data = models.CharField(max_length=50,
                              default=None,
                              null=True,
                              blank=True,
                              verbose_name='время выполнения привычки',
                              help_text='время, когда необходимо выполнять привычку',
                              )
    action = models.CharField(max_length=50,
                              default=None,
                              null=True,
                              blank=True,
                              verbose_name='действие-привычка',
                              help_text='действие, которое представляет собой привычка.',
                              )
    nice = models.BooleanField(default=False, 
                               verbose_name="Признак приятной привычки"
                               )
    related = models.ForeignKey(CustomUser, 
                             null=False, 
                             on_delete=models.CASCADE,
                             related_name="related"
                             )
    period = models.IntegerField(null=True,
                                blank=True,
                                verbose_name='периодичность выполнения'
                                ) 
    reward = models.CharField(max_length=50,
                              default=None,
                              null=True,
                              blank=True,
                              verbose_name='чем пользователь должен себя вознаградить',
                              help_text='вознаграждение',
                              )  
    time = models.IntegerField(null=True,
                                blank=True,
                                verbose_name='время на выполнение привычки'
                                )
    pablic = models.BooleanField(default=False, 
                                 verbose_name="привычки можно публиковать в общий доступ"
                                 ) 


    def __str__(self):
        return self.action
    
    def __repr__(self):
        return f"{self.pk} {self.action}"
