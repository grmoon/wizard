<template>
    <input
        v-if='initialized'
        v-model='value'
        type='text'
        :required='field.required'
        :maxlength='field.maxlength'
        :minlength='field.minlength'
        :pattern='field.pattern'
        :placeholder='field.placeholder'
        :readonly='field.readonly'
        :size='field.size'
        :spellcheck='field.spellcheck'
    />
</template>

<script>
import axios from 'axios';
import { mapState, mapMutations } from 'vuex';

export default {
    props: {
        id: {
            required: true,
            type: Number
        },
        questionId: {
            required: true,
            type: Number
        }
    },
    data() {
        return {
            field: undefined
        }
    },
    computed: {
        ...mapState({
            answer({ answers }) {
                return answers[this.questionId];
            }
        }),
        value: {
            get() {
                return this.answer.value;
            },
            set(value) {
                this.setAnswerValue({
                    questionId: this.questionId,
                    value
                });
            }
        },
        initialized() {
            return this.field !== undefined &&
                this.answer !== undefined;
        }
    },
    methods: {
        ...mapMutations(['setAnswerValue']),
        getField() {
            const self = this;

            return axios.get(`http://localhost:8003/api/v1/text_fields/${this.id}/`)
                .then(({ data: field }) => {
                    self.field = field;
                });
        },
    },
    beforeMount() {
        this.getField();
    }
}
</script>