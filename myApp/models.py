from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class Drive(models.Model): 

    STATUS_CHOICES = (
        (0, _('Open')),
        (1, _('Ongoing')),
        (2, _('Closed'))
    )

    CATEGORY_CHOICES = (
        (0, _('Healthcare')),
        (1, _('Animals')),
        (2, _('Art and Culture')),
        (3, _('Community Development')),
        (4, _('Environment')),
        (5, _('Education')),
        (6, _('Human Services')),
        (7, _('Religion')),
    )

    SIZE_CHOICES = (
        (0, _('Small')),
        (1, _('Medium')),
        (2, _('Big'))
    )

    name = models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=1000)
    expected_amount = models.IntegerField(default=0, blank=False)
    amount_raised = models.IntegerField(default=0)
    donation_count = models.IntegerField(default=0)
    owner_id = models.CharField(max_length=100, blank=False)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES)
    imageUrl = models.URLField(max_length=1000)
    state = models.CharField(max_length=100)
    size = models.CharField(max_length=50, choices=SIZE_CHOICES)


    class Meta:
        verbose_name = _('Drive')
        verbose_name_plural = _('Drives')

    def __str__(self) -> str:
        return self.name


class UserProfile(models.Model):
    TYPE_CHOICES = (
        (0, _('Individual')),
        (1, _('Organisation'))
    )

    GENDER_CHOICES = (
        (0, _('Female')),
        (1, _('Male')),
        (2, _('Others'))
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    address = models.CharField(max_length=1000)
    phone = models.CharField(max_length=20)
    donation_count = models.IntegerField(default=0)
    amount_donated = models.IntegerField(default=0)
    # Fields for individual user
    age = models.IntegerField(blank=True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, blank=True, null=True)
    profession = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = _('UserProfile')
        verbose_name_plural = _('UserProfiles')

    def __str__(self) -> str:
        return self.user.username


class TimeStamp(models.Model):
    date = models.DateTimeField(verbose_name=_('Donated On'), auto_now=True)

    def __str__(self) -> str:
        return str(self.date)

    class Meta:
        abstract = True


class Transactions(TimeStamp):
    drive = models.ForeignKey(Drive, related_name='drive', on_delete=models.CASCADE)
    userId = models.IntegerField(default=0, blank=False)
    amount = models.IntegerField(default=0, blank=False)
    
    class Meta:
        verbose_name = _('Transaction')
        verbose_name_plural = _('Transactions')

    def __str__(self) -> str:
        return f'{self.drive} - Amount {self.amount} donated by {self.userId} at {super().__str__()}.'