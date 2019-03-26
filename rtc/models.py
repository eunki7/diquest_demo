from django.db import models


class RtcMenu(models.Model):
    class Meta:
        managed = False

        permissions = (
            ("showmenu", "Show to Main Menu"),
        )
