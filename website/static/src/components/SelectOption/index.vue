<template>
  <option
    :selected="selected"
    :disabled="option.disabled"
    :label="option.label"
    :value="option.value"
  >{{ option.label }}</option>
</template>

<script>
import Option from '@components/Option';
import { mapMutations } from 'vuex';

export default {
    components: { Option },
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