from django.db import models

from wizard.models.base import BaseModel

class WizardStep(BaseModel):
    position = models.PositiveIntegerField()
    step = models.ForeignKey('wizard.Step', on_delete=models.CASCADE)
    wizard = models.ForeignKey('wizard.Wizard', on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            ('position', 'wizard'),
            ('wizard', 'step'),
        )

    def __str__(self):
        return '{} > {}'.format(self.wizard, self.step)