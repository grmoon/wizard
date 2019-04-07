<template>
  <div>
    <h3>{{ section.name }}</h3>
    <Question
      v-for="(question, index) in questions"
      :key="index"
      :question="question"
    />
  </div>
</template>

<script>
import Question from '@components/Question';
import { mapState } from 'vuex';

export default {
    components: { Question },
    props: {
        section: {
            required: true,
            type: Object
        }
    },
    computed: mapState({
        questions({ sectionQuestions, questions }) {
            let _questions;
            const sectionHasQuestions = this.section.id in sectionQuestions;

            if (sectionHasQuestions) {
                const questionIds = sectionQuestions[this.section.id].map(sectionQuestion => sectionQuestion.question);

                _questions = questionIds.map(questionId => questions[questionId]);
            }
            else {
                _questions = [];
            }

            return _questions;
        }
    })
}
</script>