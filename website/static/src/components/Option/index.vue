<template>
  <label>{{ label }}&nbsp;<input
    :checked="checked"
    :name="name"
    :type="type"
    :value="value"
    :required="required"
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
        required: {
            required: true,
            type: Boolean
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