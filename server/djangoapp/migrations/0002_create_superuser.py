from django.db import migrations

def create_superuser(apps, schema_editor):
    from django.contrib.auth.models import User
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')

class Migration(migrations.Migration):
    dependencies = [
        ('djangoapp', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(create_superuser),
    ]
