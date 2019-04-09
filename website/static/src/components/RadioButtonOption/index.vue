<template>
  <Option
    type="radio"
    :checked="checked"
    :label="option.label"
    :name="name"
    :value="option.value"
    :required="required"
    @change="option_onChange"
  />
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
        required: {
            required: true,
            type: Boolean
        },
        name: {
            required: true,
            type: String
        },
        answer: {
            required: true,
            type: Object
        }
    },
    computed: {
        checked() {
            return this.answer.value == this.option.value;
        }
    },
    methods: {
        ...mapMutations(['setAnswerValue']),
        option_onChange(event) {
            this.setAnswerValue({
                questionId: this.answer.question,
                value: event.currentTarget.value
            });
        }
    }
};
</script>