<template>
    <div v-if='initialized'>
        <h3>{{ name }}</h3>
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

export default {
    components: { Question },
    data() {
        return {
            questions: undefined,
            name: undefined
        }
    },
    computed: {
        initialized() {
            return this.questions !== undefined &&
                this.name !== undefined;
        }
    },
    methods: {
        initialize() {
            return this.getSection().then(this.getQuestions);
        },
        getSection() {
            const self = this;

            return axios.get(`http://localhost:8003/api/v1/sections/${this.id}/`)
                .then((resp) => {
                    const section = resp.data;

                    self.name = section.name;

                    return section;
                });
        },
        getQuestions(section) {
            const self = this;
            const promises = section.questions.map(this.getQuestion);

            Promise.all(promises).then((questions) => {
                questions.sort((question1, question2) => {
                    return question1.position - question2.position;
                });

                self.questions = questions
            });
        },
        getQuestion(questionId) {
            return axios.get(`http://localhost:8003/api/v1/questions/${questionId}/`)
                .then(resp => resp.data);
        }
    },
    props: {
        id: {
            required: true,
            type: Number
        }
    },
    beforeMount() {
        this.initialize()
    }
}
</script>