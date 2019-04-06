<template>
    <div v-if='initialized'>
        <h3>{{ section.name }}</h3>
        <Question
            v-for='(question, index) in questions'
            :question='question'
            :key='index'
        />
    </div>
</template>

<script>
import axios from 'axios';
import Question from '@components/Question';
import { createNamespacedHelpers } from 'vuex';

const { mapMutations } = createNamespacedHelpers('questions');

export default {
    components: { Question },
    data() {
        return {
            questions: undefined
        }
    },
    computed: {
        initialized() {
            return this.questions !== undefined;
        }
    },
    methods: {
        ...mapMutations(['addQuestion']),
        getQuestions(section) {
            const self = this;
            const promises = this.section.questions.map(this.getQuestion);

            Promise.all(promises).then((questions) => {
                questions.sort((question1, question2) => {
                    return question1.position - question2.position;
                });

                self.questions = questions
            });
        },
        getQuestion(questionId) {
            const self = this;

            return axios.get(`http://localhost:8003/api/v1/questions/${questionId}/`)
                .then((resp) => {
                    const question = resp.data;

                    self.addQuestion(question);

                    return question;
                });
        }
    },
    props: {
        section: {
            required: true,
            type: Object
        }
    },
    beforeMount() {
        this.getQuestions();
    }
}
</script>