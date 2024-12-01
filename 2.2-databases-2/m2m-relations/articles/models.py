from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name="Название")
    text = models.TextField(verbose_name="Текст")
    published_at = models.DateTimeField(verbose_name="Дата публикации")
    image = models.ImageField(null=True, blank=True, verbose_name="Изображение")

    tags = models.ManyToManyField(
        Tag,
        through="Scope",
        related_name="articles",
        verbose_name="Теги"
    )

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["-published_at"]

    def __str__(self):
        return self.title


class Scope(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name="Тег")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="scopes")
    is_main = models.BooleanField(verbose_name="Основной", default=False)

    class Meta:
        verbose_name = "Связь статьи с тегом"
        verbose_name_plural = "Связи статьи с тегами"
        unique_together = ("article", "tag")

    def __str__(self):
        return f"{self.article.title} - {self.tag.name} ({'Основной' if self.is_main else 'Дополнительный'})"
