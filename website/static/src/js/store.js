import Vuex from 'vuex';
import Vue from 'vue';
import axios from 'axios';
import sortByPosition from '@utils/sortByPosition';
import * as Cookies from 'js-cookie';


Vue.use(Vuex);
function defaultState(user) {
    return {
        answers: {},
        fields: {},
        multipleChoiceFieldOptions: {},
        options: {},
        questions: {},
        sectionQuestions: undefined,
        sections: undefined,
        step: undefined,
        stepSections: undefined,
        triggers: {},
        wizardStep: undefined,
        user
    }
}

export default new Vuex.Store({
    state: defaultState(),
    actions: {
        get(store, { url, config={} }) {
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
                const step = wizardStep.step;
                wizardStep.step = step.id;

                commit('setWizardStep', wizardStep);
                return dispatch('getStep', step);
            });
        },
        getStep({ commit, dispatch }, step) {
            const stepSections = step.sections;
            step.sections = stepSections.map(section => section.id);

            commit('setStep', step);
            return dispatch('getStepSections', stepSections);
        },
        getStepSections({ commit, dispatch }, _stepSections) {
            const stepSections = Array.from(_stepSections);
            const sections = stepSections.reduce((acc, stepSection) => {
                const section = stepSection.section;
                stepSection.section = section.id;

                acc.push(section);
                return acc;
            }, []);

            commit('setStepSections', stepSections);
            return dispatch('getSections', sections);
        },
        getSections({ commit, dispatch }, _sections) {
            const sections = Array.from(_sections);
            const sectionQuestions = sections.reduce((acc, section) => {
                const _sectionQuestions = section.questions;
                section.questions = _sectionQuestions.map(sectionQuestion => sectionQuestion.id);

                return acc.concat(_sectionQuestions);
            }, []);

            commit('setSections', sections);
            return dispatch('getSectionQuestions', sectionQuestions);
        },
        getSectionQuestions({ commit, dispatch }, _sectionQuestions) {
            const sectionQuestions = Array.from(_sectionQuestions);
            const questions = sectionQuestions.reduce((acc, sectionQuestion) => {
                const question = sectionQuestion.question;
                sectionQuestion.question = question.id;

                acc.push(question);
                return acc;
            }, []);

            commit('setSectionQuestions', sectionQuestions);
            return dispatch('getQuestions', questions);
        },
        getQuestions({ commit, dispatch, state }, _questions) {
            const questions = Array.from(_questions);

            const currentQuestionIds = Object.keys(state.questions).map(id => parseInt(id));
            const newQuestions = questions.filter((question) => {
                return currentQuestionIds.indexOf(question.id) === -1;
            });

            if (newQuestions.length === 0) {
                return new Promise(resolve => resolve());
            }

            const fields = [];
            const answers = [];
            let triggers = [];

            newQuestions.forEach((question) => {
                const field = question.field;
                question.field = field.id
                fields.push(field);

                const _triggers = question.triggers;
                question.triggers = _triggers.map(trigger => trigger.id);
                triggers = triggers.concat(_triggers);

                let answer;

                if (question.answer === null) {
                    answer = {
                        question: question.id,
                        user: state.user.id,
                        value: null,
                    };
                }
                else if (answer !== null) {
                    answer = question.answer
                    question.answer = answer.id;
                }

                answers.push(answer);
            });

            commit('addQuestions', newQuestions);

            const answerPromise = dispatch('getAnswers', answers);
            const triggerPromise = dispatch('getTriggers', triggers);
            const fieldsPromise = dispatch('getFields', fields);

            return Promise.all([answerPromise, triggerPromise, fieldsPromise]);
        },
        getAnswers({ commit }, _answers) {
            const answers = Array.from(_answers);

            commit('addAnswers', answers);

            return new Promise(resolve => resolve(answers));
        },
        getTriggers({ commit, dispatch }, _triggers) {
            const triggers = Array.from(_triggers)
            const toQuestions = triggers.reduce((acc, trigger) => {
                const question = trigger.to_question;
                trigger.to_question = question.id;

                acc.push(question);
                return acc;
            }, []);

            commit('addTriggers', triggers);

            return dispatch('getQuestions', toQuestions);
        },
        getFields({ commit, dispatch, state }, _fields) {
            const fields = Array.from(_fields);
            const currentFieldIds = Object.keys(state.fields).map(id => parseInt(id));
            const newFields = fields.filter((field) => {
                return currentFieldIds.indexOf(field.id) === -1;
            });

            if (newFields.length === 0) {
                return new Promise(resolve => resolve([]));
            }

            const multipleChoiceFieldOptions = newFields.reduce((acc, field) => {
                const options = field.options || [];
                field.options = options.map(option => option.id);

                return acc.concat(options);
            }, []);


            commit('addFields', newFields);

            return dispatch('getMultipleChoiceFieldOptions', multipleChoiceFieldOptions);

        },
        getMultipleChoiceFieldOptions({ commit, dispatch, state }, _multipleChoiceFieldOptions) {
            const multipleChoiceFieldOptions = Array.from(_multipleChoiceFieldOptions);
            const currentMultipleChoiceFieldOptionIds = Object.keys(state.multipleChoiceFieldOptions).map(id => parseInt(id));
            const newMultipleChoiceFieldOptions = multipleChoiceFieldOptions.filter((multipleChoiceFieldOption) => {
                return currentMultipleChoiceFieldOptionIds.indexOf(multipleChoiceFieldOption.id) === -1;
            });

            if (newMultipleChoiceFieldOptions.length === 0) {
                return new Promise(resolve => resolve([]));
            }

            commit('addMultipleChoiceOptions', multipleChoiceFieldOptions);

            const options = multipleChoiceFieldOptions.map((multipleChoiceFieldOption) => {
                const option = multipleChoiceFieldOption.option;
                multipleChoiceFieldOption.option = option.id

                return option;
            });

            return dispatch('getOptions', options);
        },
        getOptions({ commit, state }, _options) {
            const options = Array.from(_options);

            const currentOptionIds = Object.keys(state.options).map(id => parseInt(id));
            const newOptions = options.filter((option) => {
                return currentOptionIds.indexOf(option.id) === -1;
            });

            if (newOptions.length === 0) {
                return new Promise(resolve => resolve([]));
            }

            commit('addOptions', newOptions);

            return new Promise(resolve => resolve(newOptions));
        },
        getUser({ commit, dispatch }) {
            const url = 'http://localhost:8003/api/v1/me/';

            return dispatch('get', { url }).then((user) => {
                commit('setUser', user);
            });
        },
        post(store, { url, config={}, payload }) {
            const _config = {
                ...config,
                headers: {
                    'X-CSRFToken': Cookies.get('csrftoken')
                }
            }

            return axios.post(url, payload, _config).then(resp => resp.data);
        },
        patch(store, { url, config={}, payload }) {
            const _config = {
                ...config,
                headers: {
                    'X-CSRFToken': Cookies.get('csrftoken')
                }
            }

            return axios.patch(url, payload, _config).then(resp => resp.data);
        },
        saveAnswers({ state, commit, dispatch }) {
            const baseUrl = 'http://localhost:8003/api/v1/answers/';

            const promises = Object.values(state.answers).reduce((acc, answer) => {
                let promise;

                if (answer.value !== null) {
                    if (answer.id !== undefined) {
                        const url = `${baseUrl}${answer.id}/`;
                        promise = dispatch('patch', { url, payload: answer });
                    }
                    else {
                        promise = dispatch('post', { url: baseUrl, payload: answer });
                    }

                    acc.push(promise);
                }

                return acc;
            }, []);

            return Promise.all(promises).then((answers) => {
                commit('addAnswers', answers);

                return answers;
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

            state.triggers = {
                ...state.triggers,
                ...triggersByQuestion
            }
        },
        addFields(state, fields) {
            fields.forEach((field) => {
                Vue.set(state.fields, field.id, field);
            });
        },
        addMultipleChoiceOptions(state, multipleChoiceFieldOptions) {
            multipleChoiceFieldOptions.forEach((multipleChoiceFieldOption) => {
                Vue.set(state.multipleChoiceFieldOptions, multipleChoiceFieldOption.id, multipleChoiceFieldOption);
            });
        },
        addOptions(state, options) {
            options.forEach((option) => {
                Vue.set(state.options, option.id, option);
            });
        },
        setAnswerValue(state, { questionId, value }) {
            Vue.set(state.answers[questionId], 'value', value);
        },
        resetState(state) {
            Object.assign(state, defaultState(state.user));
        },
        setUser(state, user) {
            state.user = user;
        }
    }
});