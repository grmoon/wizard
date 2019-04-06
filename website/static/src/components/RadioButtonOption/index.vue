<template>
    <Option
        @change='option_onChange'
        type='radio'
        :checked='checked'
        :label='option.label'
        :name='name'
        :value='option.value'
    />
</template>

<style>
label {
    display: block;
}
</style>

<script>
import axios from 'axios';
import Option from '@components/Option';
import { mapState, mapMutations } from 'vuex';

export default {
    components: { Option },
    props: {
        option: {
            required: true,
            type: Object
        },
        name: {
            required: true,
            type: String
        },
        questionId: {
            required: true,
            type: Number
        }
    },
    computed: {
        ...mapState({
            answer({ answers }) {
                return answers[this.questionId];
            }
        }),
        checked() {
            return this.answer.value == this.option.value;
        }
    },
    methods: {
        ...mapMutations(['setAnswerValue']),
        option_onChange(event) {
            this.setAnswerValue({
                questionId: this.questionId,
                value: event.currentTarget.value
            });
        }
    }
};
</script>