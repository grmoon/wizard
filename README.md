# wizard
## Installation
**This has only been tested using python 3.7.0 and django 2.2**
1. Install [pyenv](https://github.com/pyenv/pyenv)
1. Install python 3.7.0
    ```bash
    pyenv install 3.7.0
    ```
1. Specify which version of python you'd like to use
    ```bash
    pyenv local 3.7.0
    ```
1. Create and activate a virtual environment
    ```bash
    python -m venv venv
    . venv/bin/activate
    ```
1. Clone the repo
    ```bash
    git clone git@github.com:grmoon/wizard.git
    cd wizard
    ```
1. Install dependencies
    ```bash
    pip install --upgrade pip setuptools
    pip install -r requirements.txt
    ````
1. Run migrations (after updating settings.py to point to the right db)
    ```bash
    python manage.py migrate
    ````
1. Create a superuser
    ```bash
    python manage.py createsuperuser
    ````
After running those steps you should be able to start the django server, login to the admin interface, and begin creating a wizard.
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
* RadioButtonFieldOption: Connects a RadioButtonField to an Option
* CheckboxFieldOption: Connects a CheckboxField to an Option
### Positions
When creating a wizard, you will care in what order the steps are rendered, in what order the sections are rendered in a step, and in what order questions are rendered in a section. Each of the through models listed above has a field called `position`, which allows you to specify the order in which Steps/Sections/Questions/Options should be rendered. Entities with lower `position` values will always be rendered before entities with higher values.
## Navigation
URLs of the form `/wizard/<wizard_id>/step/<step_num>/` are currently supported. The `wizard_id` parameter is self-explanatory. The `step_num` parameter *does not correspond to the id or position of a step*. Instead, it is the step of the wizard you wish to show. For example, if there is a Wizard with 3 steps:

| id | position | wizard_id |
| :-: | :-: | :-: |
| 10 | 2 | 1 |
| 11 | 3 | 1 |
| 21 | 4 | 1 |

The urls `/wizard/1/step/1/`, will return the step with id 10, `/wizard/1/step/2/` will return the step with id 11, and `/wizard/1/step/3/` will return the step with id 21. Any other `step_num` param should result in a 404.
        
## Entity-Relationship Diagram
You can generate an ERD for this project using the [django-extensions graph_models](https://django-extensions.readthedocs.io/en/latest/graph_models.html) command. [pygraphviz](https://pygraphviz.github.io/) and [django-extensions](https://github.com/django-extensions/django-extensions) are included in requirements.txt, so the only thing you should have to do it install the requisite [GraphViz](http://www.graphviz.org/) utilities.
