from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from webapp.models import BaseModel
from django.utils.translation import gettext_lazy as _

statuses = [
    ("new", _("models.article.statuses: new")),
    ("moderated", _("models.article.statuses: moderated")),
    ("deleted", _("models.article.statuses: deleted"))
]


class Article(BaseModel):
    title = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name=_("models.article.title: title"),
    )
    content = models.TextField(
        null=False,
        blank=False,
        verbose_name=_("models.article.title: content"),
    )
    status = models.CharField(max_length=20, choices=statuses, verbose_name="Статус", default=statuses[0][0])

    author = models.ForeignKey(
        get_user_model(),
        related_name="articles",
        on_delete=models.SET_DEFAULT,
        default=1
    )

    tags = models.ManyToManyField(
        "webapp.Tag",
        related_name="articles",
        verbose_name="Теги",
        blank=True,
    )

    def caclucate(self):
        pass

    def get_absolute_url(self):
        return reverse("webapp:article_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.pk}. {self.title}: {self.author}"

    class Meta:
        db_table = "articles"
        verbose_name = _("models.article.verbose_name: verbose_name")
        verbose_name_plural = _("models.article.verbose_name_plural: verbose_name_plural")
        permissions = [("change_article_status", "менять статус статье")]
