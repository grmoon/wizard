<template>
  <component
    :is="component"
    :answer="answer"
    :field="_field"
  />
</template>

<script>
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
        _field() {
            return {
                ...this.field,
                uuid: uuid()
            }
        },
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
