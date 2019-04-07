<template>
    <component
        :answer='answer'
        :field='field'
        :is='component'
    />
</template>

<script>
import RadioButtonField from '@components/RadioButtonField';
import TextField from '@components/TextField';

export default {
    components: { RadioButtonField },
    computed: {
        component() {
            return {
                'RadioButtonField': RadioButtonField,
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
