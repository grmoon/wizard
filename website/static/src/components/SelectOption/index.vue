<template>
  <option
    :selected="selected"
    :disabled="option.disabled"
    :label="option.label"
    :value="option.value"
  >
    {{ option.label }}
  </option>
</template>

<script>
export default {
    props: {
        option: {
            required: true,
            type: Object
        },
        selected: {
            required: true,
            type: Boolean
        },
    },
};
</script>