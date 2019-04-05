<template>
    <div v-if='initialized'>
        <h3>{{ name }}</h3>
        <Question
            v-for='(question, index) in questions'
            :id='question'
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
    props: {
        id: {
            required: true,
            type: Number
        }
    },
    beforeMount() {
        const self = this;

        axios.get(`http://localhost:8003/api/v1/sections/${this.id}/`)
            .then((resp) => {
                const section = resp.data;
                const questions = section.questions;

                questions.sort((question1, question2) => question1 - question2);

                self.questions = questions;
                self.name = section.name;
            });
    }
}
</script>