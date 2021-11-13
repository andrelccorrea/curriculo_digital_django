from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


class Skill(models.Model):

    name = models.CharField(verbose_name='Nome',
                            max_length=20, blank=True, null=True)
    score = models.IntegerField(
        verbose_name='Nível', default=80, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to='skills')
    is_key_skill = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Habilidade'
        verbose_name_plural = 'Habilidades'

    def __str__(self) -> str:
        return self.name


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to='avatar')
    title = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    cv = models.FileField(blank=True, null=True, upload_to='cv')

    class Meta:
        verbose_name = 'Perfil de usuário'
        verbose_name_plural = 'Perfis de usuário'

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'


class ContactProfile(models.Model):

    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name='Nome', max_length=100)
    email = models.EmailField(verbose_name='E-mail')
    message = models.TextField(verbose_name='Mensagem')

    class Meta:
        verbose_name = 'Perfil de contato'
        verbose_name_plural = 'Perfis de contato'
        ordering = ['timestamp']

    def __str__(self) -> str:
        return f'{self.name}'


class Testimonial(models.Model):

    thumbnail = models.ImageField(
        blank=True, null=True, upload_to='testimonials')
    name = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=200, blank=True, null=True)
    quote = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Depoimento'
        verbose_name_plural = 'Depoimentos'
        ordering = ['name']

    def __str__(self) -> str:
        return self.name


class Media(models.Model):

    image = models.ImageField(blank=True, null=True, upload_to='media')
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Mídia'
        verbose_name_plural = 'Mídias'
        ordering = ['name']

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)


class Portfolio(models.Model):

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='portfolio')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'
        ordering = ['name']

    def save(self, *args, **kwargs):
        if self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return f'/portfolio/{ self.slug }'


class Blog(models.Model):

    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(verbose_name='Autor',
                              max_length=200, blank=True, null=True)
    name = models.CharField(verbose_name='Nome',
                            max_length=200, blank=True, null=True)
    description = models.CharField(
        verbose_name='Descrição', max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='blog')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ['timestamp']

    def save(self, *args, **kwargs):
        if self.id:
            self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return f'/blog/{ self.slug }'


class Certificate(models.Model):

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name
