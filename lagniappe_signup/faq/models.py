from django.db import models

class FAQ(models.Model):
    """
    Model representing a Frequently Asked Question (FAQ).
    """

    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self) -> str:
        """
        Returns a string representation of the FAQ object.
        """
        return str(self.question)  # Explicitly convert to str (if necessary)
