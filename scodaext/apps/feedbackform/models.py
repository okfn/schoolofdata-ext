from django.db import models
from scodaext.apps.badgeclient.models import BadgeService

# Create your models here.

agree_choice = [("1","Strongly disagree"),
                ("2","Disagree"),
                ("3","Neither"),
                ("4","Agree"),
                ("5","Strongly Agree"),
                ]

class Feedback(models.Model):
    date = models.DateTimeField(auto_now=True)
    event = models.ForeignKey('Event',
                              null=True,
                              blank=True,
                              )
    name = models.CharField(
        "Your Name",
        max_length=200,
        null=True,
        blank=True,
        )
    email = models.EmailField(
        "Your email address",
        null=True,
        blank=True,
        )
    nationality = models.CharField(
        "Nationality",
        max_length=200,
        null=True,
        blank=True,
        )
    worthwhile = models.CharField(
        "It was worthwhile for me attending the event",
        max_length=50,
        choices=agree_choice,
        )
    useful = models.CharField(
        "I learned something useful",
        max_length=50,
        choices=agree_choice,
        )
    empowered = models.CharField(
        "I feel more empowered to use data effectively",
        max_length=50,
        choices=agree_choice,
        )
    organise = models.CharField(
        "I am likely to organise a similar event in my community",
        max_length=50,
        choices=agree_choice,
        )
    learned = models.TextField(
        "What is the main thing you have learned today?",
        null=True,
        blank=True,
        )
    improve = models.TextField(
        "What is the main thing we should improve for the next event?",
        null=True,
        blank=True,
        )
    testimonial = models.TextField(
        """Leave a brief testimonial to future learners so we can spread the
        word:""",
        null=True,
        blank=True,
        )

    def __unicode__(self):
        return u"%s-%s-%s" % (
            self.name,
            self.email,
            self.date,
            )


class Event(models.Model):
    """ Events for Badging """
    name = models.CharField(max_length=200,unique=True)
    badge = models.SlugField(null=True,blank=True)
    badge_service = models.ForeignKey(BadgeService,null=True,blank=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name
