# wizard
## Creating a Wizard
Wizards are composed of steps. Steps are composed of sections. Sections are composed of questions. Questions are linked to fields. The easiest way to create a wizard is to start from the bottom up.
1. Create whatever fields you're need (e.g. TextField, RadioButtonField)
1. Create whatever questions you need, linking them to the fields you created in the previous step.
1. Create whatever sections you need, linking them to the fields you created in the previous step.
1. Create whatever steps you need, linking them to the sections you created in the previous step.
1. Create your wizard, linking it to the steps you made in the previous step.
## Through Models
As many components as possible are completely standalone. For example, a Step is not linked by a ForeignKey to a Wizard. Instead, a ManyToMany relationship is facilitated through a model called WizardStep, which links a Wizard to a Step so that a Step can be used in multiple wizards. Other through models are:
* WizardStep: Connects a Wizard to a Step
* StepSection: Connects a Step to a Section
* SectionQuestion: Connects a Section to a Question
* Trigger: Connects one Question to another
### Positions
When creating a wizard, you will care what order the steps are rendered, in what order the sections are rendered in a step, and in what order questions are rendered in a section. Each of the through models listed above has a field called `position`, which allows you to specify the order in which Steps/Sections/Questions should be rendered. Entities with lower `position` values will always be rendered before entities with higher values.
