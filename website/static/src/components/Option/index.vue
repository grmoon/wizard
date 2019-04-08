<template>
  <label>{{ label }}&nbsp;<input
    :checked="checked"
    :name="name"
    :type="type"
    :value="value"
    @input="input_onChange"
  ></label>
</template>

<style>
label {
    display: block;
}
</style>

<script>
export default {
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
            validator: () => true
        }
    },
    methods: {
        input_onChange(event) {
            this.$emit('change', event);
        }
    }
};
</script>