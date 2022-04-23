from datetime import datetime, timedelta
from django.db import models


class RecentlyPostManager(models.Manager):

    def get_query_set(self):
        return super().get_queryset().filter(create_date__gte=datetime.now() - timedelta(days=7))
