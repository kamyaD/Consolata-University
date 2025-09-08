# gallery/management/commands/import_photos.py
import os
from django.core.files import File
from django.core.management.base import BaseCommand
from gallery.models import Photo

class Command(BaseCommand):
    help = "Import all images from a folder into the Photo model"

    def add_arguments(self, parser):
        parser.add_argument("folder_path", type=str, help="Path to the folder with images")

    def handle(self, *args, **kwargs):
        folder_path = kwargs["folder_path"]

        if not os.path.isdir(folder_path):
            self.stdout.write(self.style.ERROR(f"{folder_path} is not a valid directory"))
            return

        count = 0
        for filename in os.listdir(folder_path):
            if filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".webp")):
                file_path = os.path.join(folder_path, filename)
                with open(file_path, "rb") as f:
                    photo = Photo.objects.create(image=File(f, name=filename))
                    count += 1
                    self.stdout.write(self.style.SUCCESS(f"Imported {photo.image.name}"))

        self.stdout.write(self.style.SUCCESS(f"✅ Imported {count} images from {folder_path}"))
