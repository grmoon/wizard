<template>
  <component
    :is="component"
    :answer="answer"
    :field="field"
  />
</template>

<script>
import MultipleChoiceField from '@components/MultipleChoiceField';
import TextField from '@components/TextField';

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
        component() {
            return {
                'CheckboxField': MultipleChoiceField,
                'RadioButtonField': MultipleChoiceField,
                'TextField': TextField,
            }[this.field.class]
        }
    }
}
</script>
