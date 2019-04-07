<template>
    <component
        :answer='answer'
        :field='field'
        :is='component'
    />
</template>

<script>
import MultipleChoiceField from '@components/MultipleChoiceField';
import TextField from '@components/TextField';

export default {
    computed: {
        component() {
            return {
                'CheckboxField': MultipleChoiceField,
                'RadioButtonField': MultipleChoiceField,
                'TextField': TextField,
            }[this.field.class]
        }
    },
    props: {
        answer: {
            required: true,
            type: Object
        },
        field: {
            required: true,
            type: Object
        },
    }
}
</script>
