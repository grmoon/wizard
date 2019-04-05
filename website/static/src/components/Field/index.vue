<template>
    <component
        @activate='component_onActivate'
        @deactivate='component_onDeactivate'
        :answer='answer'
        :id='id'
        :is='component'
    />
</template>

<script>
import RadioButtonField from '@components/RadioButtonField';

export default {
    components: { RadioButtonField },
    methods: {
        component_onActivate(triggerIds) {
            this.$emit('activate', triggerIds);
        },
        component_onDeactivate(triggerIds) {
            this.$emit('deactivate', triggerIds);
        }
    },
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
