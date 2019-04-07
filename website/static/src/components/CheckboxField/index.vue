<template>
    <div>
        <CheckboxOption
            v-for='(option, index) in options'
            :key='index'
            :name='field.name'
            :option='option'
            :answer='answer'
        />
    </div>
</template>

<script>
import CheckboxOption from '@components/CheckboxOption';
import { mapState } from 'vuex';

export default {
    components: { CheckboxOption },
    props: {
        answer: {
            required: true,
            type: Object
        },
        field: {
            required: true,
            type: Object
        },
        options: {
            required: true,
            type: Array
        },
    }
};
</script>