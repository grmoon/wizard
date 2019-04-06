import Vuex from 'vuex';
import Vue from 'vue';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        answers: {}
    },
    mutations: {
        addAnswer(state, { answer, questionId }) {
            Vue.set(state.answers, questionId, answer);
        },
        setAnswerValue(state, { questionId, value }) {
            Vue.set(state.answers[questionId], 'value', value);
        }
    }
});