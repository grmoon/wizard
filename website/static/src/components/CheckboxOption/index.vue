<template>
    <Option
        @change='option_onChange'
        type='checkbox'
        :checked='checked'
        :label='option.label'
        :name='name'
        :value='option.value'
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
        name: {
            required: true,
            type: String
        },
        answer: {
            required: true,
            type: Object
        },
        exclusiveValues: {
            required: true,
            type: Array
        },
    },
    computed: {
        exclusive() {
            return this.exclusiveValues.includes(this.option.value);
        },
        checked() {
            return this.answerValue.includes(this.option.value);
        },
        answerValue() {
            return this.answer.value || [];
        }
    },
    methods: {
        ...mapMutations(['setAnswerValue']),
        option_onChange(event) {
            let value = Array.from(this.answerValue);
            const currentTargetValue = event.currentTarget.value;

            if (event.currentTarget.checked) {
                if (this.exclusive) {
                    value = [currentTargetValue];
                }
                else {
                    this.exclusiveValues.forEach((exclusiveValue) => {
                        const index = value.indexOf(exclusiveValue);

                        if (index !== -1) {
                            value.splice(index, 1);
                        }
                    });

                    value.push(currentTargetValue);
                }
            }
            else {
                const index = value.indexOf(currentTargetValue);

                if (index > -1) {
                    value.splice(index, 1);
                }
            }

            this.setAnswerValue({
                questionId: this.answer.question,
                value
            });
        }
    }
};
</script>