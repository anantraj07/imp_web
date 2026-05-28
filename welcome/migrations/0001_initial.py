from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='SiteConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_year', models.CharField(default='2025', help_text='e.g. 2025', max_length=10)),
                ('gform_url', models.URLField(default='https://forms.google.com', help_text='Google Form URL for newcomers to fill', max_length=500)),
                ('whatsapp_channel_url', models.URLField(blank=True, default='', help_text='WhatsApp Channel invite link', max_length=500)),
                ('announcement', models.TextField(blank=True, default='', help_text='Optional announcement banner (leave blank to hide)')),
                ('admission_date', models.CharField(default='16th July', help_text='Admission date to display', max_length=50)),
            ],
            options={'verbose_name': 'Site Configuration', 'verbose_name_plural': 'Site Configuration'},
        ),
    ]
