from django.db import models


class MlMenu(models.Model):
    class Meta:
        managed = False

        permissions = (
            ("showmenu", "Show to Main Menu"),
        )
