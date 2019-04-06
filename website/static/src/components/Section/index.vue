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
import Question from '@components/Question';
import axios from 'axios';
import sortByPosition from '@utils/sortByPosition';

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
        getQuestions(section) {
            const self = this;
            const promises = this.section.questions.map(this.getQuestion);

            Promise.all(promises).then((questions) => {
                questions.sort(sortByPosition);

                self.questions = questions.map(question => question.question);
            });
        },
        getQuestion(questionId) {
            return axios.get(`http://localhost:8003/api/v1/section_questions/${questionId}/`).then(resp => resp.data);
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