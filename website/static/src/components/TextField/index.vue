<template>
  <input
    v-model="value"
    type="text"
    :required="field.required"
    :maxlength="field.maxlength"
    :minlength="field.minlength"
    :pattern="field.pattern"
    :placeholder="field.placeholder"
    :readonly="field.readonly"
    :size="field.size"
    :spellcheck="field.spellcheck"
  >
</template>

<script>
import { mapMutations } from 'vuex';

export default {
    props: {
        answer: {
            required: true,
            type: Object
        },
        field: {
            required: true,
            type: Object
        }
    },
    computed: {
        value: {
            get() {
                return this.answer.value;
            },
            set(value) {
                this.setAnswerValue({
                    questionId: this.answer.question,
                    value
                });
            }
        }
    },
    methods: mapMutations(['setAnswerValue'])
}
</script>