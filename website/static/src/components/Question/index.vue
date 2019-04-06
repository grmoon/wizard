<template>
    <div
        v-if='initialized'
        class='question'
    >
        <h4>{{ question.text }}</h4>
        <Field
            :question-id='question.id'
            :field-class='question.field_class'
            :id='question.field'
        />
        <div
            v-if='activeTriggers.length > 0'
            class='subquestions'
        >
            <Question
                v-for='(trigger, index) in activeTriggers'
                :key='index'
                :question='trigger.question'
            />
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import Field from '@components/Field';
import sortByPosition from '@utils/sortByPosition';
import { mapState, mapMutations } from 'vuex';

export default {
    components: { Field },
    name: 'Question',
    data() {
        return {
            triggers: undefined
        }
    },
    computed: {
        initialized() {
            return this.answer !== undefined &&
                this.triggers !== undefined;
        }
    },
    props: {
        question: {
            required: true,
            type: Object
        }
    },
    computed: {
        ...mapState({
            answer({ answers }) {
                return answers[this.question.id];
            }
        }),
        activeTriggers() {
            const self = this;

            const activeTriggers = this.triggers.filter((trigger) => {
                return trigger.value == self.answer.value;
            });

            activeTriggers.sort(sortByPosition);

            return activeTriggers;
        },
        initialized() {
            return this.triggers !== undefined &&
                this.answer !== undefined;
        }
    },
    methods: {
        ...mapMutations(['addAnswer', 'removeAnswer']),
        initialize() {
            this.getAnswer().then(this.getTriggers);
        },
        getTriggers() {
            const self = this;
            const promises = this.question.triggers.map(this.getTrigger);

            Promise.all(promises).then((triggers) => {
                self.triggers = triggers;
            });
        },
        getTrigger(triggerId) {
            const self = this;

            return axios.get(`http://localhost:8003/api/v1/triggers/${triggerId}/`).then(({ data: trigger }) => {
                return self.attachQuestionToTrigger(trigger);
            });
        },
        attachQuestionToTrigger(trigger) {
            return this.getQuestion(trigger.to_question).then((question) => {
                return {
                    ...trigger,
                    question
                }
            })
        },
        getQuestion(questionId) {
            return axios.get(`http://localhost:8003/api/v1/questions/${questionId}/`).then(resp => resp.data);
        },
        getAnswer() {
            const self = this;
            let promise;

            if (this.question.answer === null) {
                promise = new Promise((resolve) => {
                    resolve({
                        question: this.question.id,
                        value: null
                    });
                });
            }
            else {
                promise = axios.get(`http://localhost:8003/api/v1/answers/${this.question.answer}/`).then(resp => resp.data);
            }

            return promise.then((answer) => {
                self.addAnswer({
                    answer,
                    questionId: self.question.id
                });
            });
        }
    },
    beforeMount() {
        this.initialize();
    },
    destroyed() {
        this.removeAnswer(this.question.id);
    },
};
</script>