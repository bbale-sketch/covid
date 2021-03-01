from django.db import models
from django.urls import reverse


# Create your models here.


class Speech(models.Model):
    """Model representing a speech (but not a specific copy of a speech)."""
    title = models.CharField(max_length=2000)
    speaker = models.ForeignKey('Speaker', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter speech here')
    # date = models.DateField(null=True, blank=True)
    # isbn = models.CharField('ISBN', max_length=13, unique=True,
    #                          help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    # genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this speech."""
        return reverse('speech-detail', args=[str(self.id)])







class Speech(models.Model):
    """Model representing a speech (but not a specific copy of a speech)."""
    title = models.CharField(max_length=200)

  
    speaker = models.ForeignKey('speaker', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=1000, help_text='Enter speech here')
  

    

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this speech."""
        return reverse('speech-detail', args=[str(self.id)])



# import uuid 

# class speechInstance(models.Model):
#     """Model representing a specific copy of a speech (i.e. that can be borrowed from the library)."""
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
#     speech = models.ForeignKey('speech', on_delete=models.RESTRICT)
   

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.speech.title})'


class Speaker(models.Model):
    """Model representing an speaker."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
   
    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular speech instance."""
        return reverse('speech-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'



