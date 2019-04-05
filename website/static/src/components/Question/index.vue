<template>
    <div v-if='initialized'>
        <h4>{{ text }}</h4>
        <Field
            :answer='answer'
            :fieldClass='fieldClass'
            :id='fieldId'
        />
    </div>
</template>

<script>
import axios from 'axios';
import Field from '@components/Field';

export default {
    components: { Field },
    data() {
        return {
            answer: undefined,
            fieldId: undefined,
            fieldClass: undefined,
            text: undefined
        }
    },
    computed: {
        initialized() {
            return this.fieldId !== undefined &&
                this.fieldClass !== undefined &&
                this.text !== undefined &&
                this.answer !== undefined;
        }
    },
    props: {
        id: {
            required: true,
            type: Number
        }
    },
    methods: {
        initialize() {
            this.getQuestion().then(this.getAnswer);
        },
        getQuestion() {
            const self = this;

            return axios.get(`http://localhost:8003/api/v1/questions/${this.id}/`)
                .then((resp) => {
                    const question = resp.data;

                    self.fieldId = question.field;
                    self.fieldClass = question.field_class;
                    self.text = question.text;

                    return question;
                });
        },
        getAnswer(question) {
            const self = this;

            if (question.answer === null) {
                self.answer = {
                    question: question.id,
                    value: null
                }
            }
            else {
                axios.get(`http://localhost:8003/api/v1/answers/${question.answer}/`)
                    .then((resp) => {
                        self.answer = resp.data;
                    });
            }
        }
    },
    beforeMount() {
        this.initialize()
    },
};
</script>