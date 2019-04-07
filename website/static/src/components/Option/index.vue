<template>
    <label>{{ label }}&nbsp;<input
        @input='input_onChange'
        :checked='checked'
        :name='name'
        :type='type'
        :value='value'
    /></label>
</template>

<style>
label {
    display: block;
}
</style>

<script>
export default {
    methods: {
        input_onChange(event) {
            this.$emit('change', event);
        }
    },
    props: {
        checked: {
            required: true,
            type: Boolean
        },
        label: {
            required: true,
            type: String
        },
        name: {
            required: true,
            type: String
        },
        type: {
            required: true,
            type: String
        },
        value: {
            required: true,
        }
    }
};
</script>