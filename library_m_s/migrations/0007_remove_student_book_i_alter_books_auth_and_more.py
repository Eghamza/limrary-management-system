# Generated by Django 4.1.4 on 2022-12-30 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_m_s', '0006_remove_student_books_student_book_student_book_i'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='book_i',
        ),
        migrations.AlterField(
            model_name='books',
            name='auth',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='books',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='staf_user',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='staf_user',
            name='frist_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='staf_user',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='staf_user',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]
