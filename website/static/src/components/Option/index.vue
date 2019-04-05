<template>
    <label>{{ label }}&nbsp;<input
        :checked='checked'
        :name='name'
        :type='type'
        :value='value'
    /></label>
</template>

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
        }
    }
};
</script>