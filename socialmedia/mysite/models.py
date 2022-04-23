from django.db import models
from django.utils import timezone
from mysite.managers import RecentlyPostManager


class User(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    national_code = models.CharField(max_length=10, unique=True)
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    image = models.ImageField(upload_to='images', verbose_name="Image")
    caption = models.TextField(max_length=100, blank=True)
    title = models.CharField(max_length=20, null=False, blank=False, unique=True)
    create_date = models.DateTimeField(default=timezone.now,)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = RecentlyPostManager()

    class Meta:
        db_table = "mysite_post"
        ordering = ['-create_date']

    def __str__(self):
        return f"user: {self.user},title: {self.title}"


class Comment(models.Model):
    comment = models.TextField(max_length=300, null=False, blank=False)
    created_date = models.DateTimeField(default=timezone.now,)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comment')

    def __str__(self):
        return 'Comment:{} by {} at time {} '.format(self.comment, self.user, self.created_date)
