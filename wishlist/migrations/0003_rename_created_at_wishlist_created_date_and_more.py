
from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):
    dependencies = [
        ("wishlist", "0002_alter_wishlist_item_options_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="wishlist",
            old_name="created_at",
            new_name="created_date",
        ),
        migrations.RenameField(
            model_name="wishlist",
            old_name="updated_at",
            new_name="modified_date",
        ),
        migrations.AlterField(
            model_name="wishlist",
            name="session_id",
            field=models.CharField(blank=True, default="", max_length=3000, null=True),
        ),
    ]