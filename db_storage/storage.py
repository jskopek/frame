from images.storage import LocalStorage
from db_storage.models import Image
from django.core.urlresolvers import reverse

class DBStorage(LocalStorage):
    def get_remote_path(self):
        """
        Returns a remote path for the file
        """
        return reverse('db_storage_image', kwargs={'file_name':self.filename})

    def get_file_data(self):
        """
        Returns the raw data for the specific file, downloading it from S3
        """
        image = Image.objects.get(file_name=self.filename)
        return image.data

    def store(self, file_instance, content_type=None):
        """
        Copy over the `file_instance` from memory to S3
        """
        data = file_instance.read()
        Image.objects.create(file_name=self.filename, mimetype=content_type, data=data)
