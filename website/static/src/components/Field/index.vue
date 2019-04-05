<template>
    <component
        :answer='answer'
        :id='id'
        :is='component'
    />
</template>

<script>
import RadioButtonField from '@components/RadioButtonField';

export default {
    components: { RadioButtonField },
    computed: {
        component() {
            return {
                'radiobuttonfield': RadioButtonField
            }[this.fieldClass]
        }
    },
    props: {
        answer: {
            required: true,
            type: Object
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
