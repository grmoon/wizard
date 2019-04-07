<template>
    <div>
        <CheckboxOption
            v-for='(option, index) in options'
            :key='index'
            :name='field.name'
            :option='option.option'
            :answer='answer'
            :exclusiveValues='exclusiveValues'
        />
    </div>
</template>

<script>
import CheckboxOption from '@components/CheckboxOption';
import { mapState } from 'vuex';

export default {
    components: { CheckboxOption },
    computed: {
        exclusiveValues() {
            return this.options.reduce((acc, option) => {
                if (option.exclusive) {
                    acc.push(option.option.value)
                }

                return acc
            }, []);
        }
    },
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