<template>
    <component
        :question-id='questionId'
        :id='id'
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
                'radiobuttonfield': RadioButtonField,
                'textfield': TextField,
            }[this.fieldClass]
        }
    },
    props: {
        questionId: {
            required: true,
            type: Number
        },
        fieldClass: {
            required: true,
            type: String
        },
        id: {
            requird: true,
            type: Number
        }
    }
}
</script>
