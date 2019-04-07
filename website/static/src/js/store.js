import Vuex from 'vuex';
import Vue from 'vue';
import axios from 'axios';
import sortByPosition from '@utils/sortByPosition';


Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        answers: {},
        questions: {},
        sectionQuestions: undefined,
        sections: undefined,
        step: undefined,
        stepSections: undefined,
        triggers: {},
        wizardStep: undefined,
    },
    actions: {
        get({ }, { url, config={} }) {
            return axios.get(url, config).then(resp => resp.data);
        },
        getWizardStep({ commit, dispatch }, { stepNum, wizardId }) {
            const url = 'http://localhost:8003/api/v1/wizard_steps/';
            const config = {
                params: {
                    step_num: stepNum,
                    wizard_id: wizardId
                }
            }

            return dispatch('get', { url, config }).then((wizardStep) => {
                commit('setWizardStep', wizardStep);

                return dispatch('getStep', wizardStep.step);
            });
        },
        getStep({ commit, dispatch }, stepId) {
            const url = `http://localhost:8003/api/v1/steps/${stepId}/`;

            return dispatch('get', { url }).then((step) => {
                commit('setStep', step);

                return dispatch('getStepSections', step.sections);
            });
        },
        getStepSections({ commit, dispatch }, stepSectionIds) {
            const url = 'http://localhost:8003/api/v1/step_sections/';
            const config = {
                params: { ids: stepSectionIds }
            };

            return dispatch('get', { url, config}).then((stepSections) => {
                commit('setStepSections', stepSections);

                return dispatch('getSections', stepSections.map(stepSection => stepSection.step));
            });

        },
        getSections({ commit, dispatch }, sectionIds) {
            const url = 'http://localhost:8003/api/v1/sections/';

            const config = {
                params: { ids: sectionIds }
            };

            return dispatch('get', { url, config }).then((sections) => {
                commit('setSections', sections);

                const sectionQuestionIds = sections.reduce((acc, section) => {
                    return acc.concat(section.questions);
                }, []);

                return dispatch('getSectionQuestions', sectionQuestionIds);
            });
        },
        getSectionQuestions({ commit, dispatch }, sectionQuestionIds) {
            const url = 'http://localhost:8003/api/v1/section_questions/';

            const config = {
                params: { ids: sectionQuestionIds}
            };

            return dispatch('get', { url, config }).then((sectionQuestions) => {
                commit('setSectionQuestions', sectionQuestions);

                const questionIds = sectionQuestions.map(sectionQuestion => sectionQuestion.question);

                return dispatch('getQuestions', questionIds);
            });
        },
        getQuestions({ commit, dispatch, state }, questionIds) {
            const url = 'http://localhost:8003/api/v1/questions/';
            const currentQuestionIds = Object.keys(state.questions);
            const paramQuestionIds = questionIds.filter((questionId) => {
                return currentQuestionIds.indexOf(questionId) === -1;
            });

            if (paramQuestionIds.length === 0) {
                return new Promise(resolve => resolve());
            }

            const config = {
                params: { ids: paramQuestionIds }
            };

            return dispatch('get', { url, config }).then((questions) => {
                commit('addQuestions', questions);

                const questionIds = questions.map(question => question.id);
                const answerPromise = dispatch('getAnswers', questionIds);
                const triggerPromise = dispatch('getTriggers', questionIds);

                return Promise.all([answerPromise, triggerPromise]);
            });
        },
        getAnswers({ commit, dispatch }, questionIds) {
            const url = 'http://localhost:8003/api/v1/answers/';

            const config = {
                params: { question_ids: questionIds }
            };

            return dispatch('get', { url, config }).then((answers) => {
                const remainingQuestionIds = Array.from(questionIds);
                const allAnswers = Array.from(answers);

                answers.forEach((answer) => {
                    const index = remainingQuestionIds.indexOf(answer.question);

                    if (index > -1) {
                        remainingQuestionIds.splice(index, 1);
                    }
                });

                remainingQuestionIds.forEach((questionId) => {
                    allAnswers.push({
                        question: questionId,
                        value: null,
                    })
                });

                commit('addAnswers', allAnswers);
            });
        },
        getTriggers({ commit, dispatch }, fromQuestionIds) {
            const url = 'http://localhost:8003/api/v1/triggers';

            const config = {
                params: { from_question_ids: fromQuestionIds }
            };

            return dispatch('get', { url, config }).then((triggers) => {
                if (triggers.length === 0) {
                    return new Promise(resolve => resolve([]));
                }

                commit('addTriggers', triggers);

                const toQuestionIds = triggers.map(trigger => trigger.to_question);

                return dispatch('getQuestions', toQuestionIds);
            });
        }
    },
    mutations: {
        setWizardStep(state, wizardStep) {
            state.wizardStep = wizardStep;
        },
        setStep(state, step) {
            state.step = step;
        },
        setStepSections(state, stepSections) {
            state.stepSections = stepSections.reduce((acc, stepSection) => {
                acc[stepSection.section] = stepSection;

                return acc;
            }, {});
        },
        setSections(state, sections) {
            sections.sort((section1, section2) => {
                return state.stepSections[section1.id].position - state.stepSections[section2.id].position;
            });

            state.sections = sections;
        },
        setSectionQuestions(state, sectionQuestions) {
            const sectionQuestionsBySection = sectionQuestions.reduce((acc, sectionQuestion) => {
                if (!(sectionQuestion.section in acc)) {
                    acc[sectionQuestion.section] = [];
                }

                acc[sectionQuestion.section].push(sectionQuestion);

                return acc;
            }, {});

            Object.values(sectionQuestionsBySection).forEach(sortByPosition);

            state.sectionQuestions = sectionQuestionsBySection;
        },
        addQuestions(state, questions) {
            questions.forEach((question) => {
                Vue.set(state.questions, question.id, question);
            });
        },
        addAnswers(state, answers) {
            answers.forEach((answer) => {
                Vue.set(state.answers, answer.question, answer);
            });
        },
        addTriggers(state, triggers) {
            const triggersByQuestion = triggers.reduce((acc, trigger) => {
                if (!(trigger.from_question in acc)) {
                    acc[trigger.from_question] = [];
                }

                acc[trigger.from_question].push(trigger);

                return acc;
            }, {});

            Object.values(triggersByQuestion).forEach(sortByPosition);

            state.triggers = triggersByQuestion;
        },
        setAnswerValue(state, { questionId, value }) {
            Vue.set(state.answers[questionId], 'value', value);
        },
    }
});