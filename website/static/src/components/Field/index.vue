<template>
  <component
    :is="component"
    :answer="answer"
    :field="augmentedField"
  />
</template>

<script>
import FileField from '@components/FileField';
import MultipleChoiceField from '@components/MultipleChoiceField';
import TextField from '@components/TextField';
import { v4 as uuid } from 'uuid';

export default {
    props: {
        answer: {
            required: true,
            type: Object
        },
        field: {
            required: true,
            type: Object
        },
    },
    computed: {
        augmentedField() {
            return {
                ...this.field,
                uuid: uuid()
            }
        },
        component() {
            return {
                'CheckboxField': MultipleChoiceField,
                'FileField': FileField,
                'RadioButtonField': MultipleChoiceField,
                'SelectField': MultipleChoiceField,
                'TextField': TextField,
            }[this.field.class]
        }
    }
}
</script>
