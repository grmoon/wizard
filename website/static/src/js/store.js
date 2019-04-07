import Vuex from 'vuex';
import Vue from 'vue';
import axios from 'axios';
import sortByPosition from '@utils/sortByPosition';


Vue.use(Vuex);
function defaultState() {
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
    }
};

export default new Vuex.Store({
    state: defaultState(),
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
            const stepSectionIdArray = Array.from(stepSectionIds);

            if(stepSectionIdArray.length === 0) {
                return new Promise(resolve => resolve([]))
            }

            const url = 'http://localhost:8003/api/v1/step_sections/';
            const config = {
                params: { ids: stepSectionIdArray }
            };

            return dispatch('get', { url, config}).then((stepSections) => {
                commit('setStepSections', stepSections);

                const sectionIds = new Set(stepSections.map(stepSection => stepSection.section));

                return dispatch('getSections', sectionIds);
            });

        },
        getSections({ commit, dispatch }, sectionIds) {
            const sectionIdArray = Array.from(sectionIds);

            if(sectionIdArray.length === 0) {
                return new Promise(resolve => resolve([]))
            }

            const url = 'http://localhost:8003/api/v1/sections/';

            const config = {
                params: { ids: sectionIdArray }
            };

            return dispatch('get', { url, config }).then((sections) => {
                commit('setSections', sections);

                const sectionQuestionIds = new Set(sections.reduce((acc, section) => {
                    return acc.concat(section.questions);
                }, []));

                return dispatch('getSectionQuestions', sectionQuestionIds);
            });
        },
        getSectionQuestions({ commit, dispatch }, sectionQuestionIds) {
            const sectionQuestionIdArray = Array.from(sectionQuestionIds);

            if(sectionQuestionIdArray.length === 0) {
                return new Promise(resolve => resolve([]))
            }

            const url = 'http://localhost:8003/api/v1/section_questions/';

            const config = {
                params: { ids: sectionQuestionIdArray }
            };

            return dispatch('get', { url, config }).then((sectionQuestions) => {
                commit('setSectionQuestions', sectionQuestions);

                const questionIds = new Set(sectionQuestions.map(sectionQuestion => sectionQuestion.question));

                return dispatch('getQuestions', questionIds);
            });
        },
        getQuestions({ commit, dispatch, state }, questionIds) {
            const currentQuestionIds = Object.keys(state.questions).map(id => parseInt(id));
            const paramQuestionIds = new Set(Array.from(questionIds).filter((questionId) => {
                return currentQuestionIds.indexOf(questionId) === -1;
            }));

            if (paramQuestionIds.size === 0) {
                return new Promise(resolve => resolve());
            }

            const url = 'http://localhost:8003/api/v1/questions/';
            const config = {
                params: { ids: Array.from(paramQuestionIds) }
            };

            return dispatch('get', { url, config }).then((questions) => {
                commit('addQuestions', questions);

                const fieldIds = new Set(questions.map(question => question.field));
                const triggerIds = new Set(questions.reduce((acc, question) => {
                    return acc.concat(question.triggers);
                }, []));
                const answerPromise = dispatch('getAnswers', paramQuestionIds);
                const triggerPromise = dispatch('getTriggers', triggerIds);
                const fieldsPromise = dispatch('getFields', fieldIds);

                return Promise.all([answerPromise, triggerPromise, fieldsPromise]);
            });
        },
        getAnswers({ commit, dispatch}, questionIds) {
            const questionIdArray = Array.from(questionIds);

            if (questionIdArray.length === 0) {
                return new Promise(resolve => resolve([]));
            }

            const url = 'http://localhost:8003/api/v1/answers/';
            const config = {
                params: { question_ids: questionIdArray }
            };

            return dispatch('get', { url, config }).then((answers) => {
                const allAnswers = Array.from(answers);
                const answerQuestionIds = answers.map(answer => answer.question);
                const remainingQuestionIds = questionIdArray.filter((questionId) => {
                    return answerQuestionIds.indexOf(questionId) === -1;
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
        getTriggers({ commit, dispatch }, triggerIds) {
            const triggerIdArray = Array.from(triggerIds);

            if (triggerIdArray.length === 0) {
                return new Promise(resolve => resolve([]));
            }

            const url = 'http://localhost:8003/api/v1/triggers/';
            const config = {
                params: { ids: triggerIdArray }
            };

            return dispatch('get', { url, config }).then((triggers) => {
                commit('addTriggers', triggers);

                const toQuestionIds = new Set(triggers.map(trigger => trigger.to_question));

                return dispatch('getQuestions', toQuestionIds);
            });
        },
        getFields({ commit, dispatch, state }, fieldIds) {
            const currentFieldIds = Object.keys(state.fields).map(id => parseInt(id));
            const paramFieldIds = new Set(Array.from(fieldIds).filter((fieldId) => {
                return currentFieldIds.indexOf(fieldId) === -1;
            }));

            if (paramFieldIds.size === 0) {
                return new Promise(resolve => resolve());
            }

            const url = 'http://localhost:8003/api/v1/fields/';
            const config = {
                params: { ids: Array.from(paramFieldIds) }
            };

            return dispatch('get', { url, config }).then((fields) => {
                commit('addFields', fields);

                const multipleChoiceFieldOptionIds = fields.reduce((acc, field) => {
                    return acc.concat(field.options || []);
                }, []);

                return dispatch('getMultipleChoiceFieldOptions', multipleChoiceFieldOptionIds)
            });
        },
        getMultipleChoiceFieldOptions({ commit, dispatch, state }, multipleChoiceFieldMultipleChoiceFieldOptionIds) {
            const currentMultipleChoiceFieldOptionIds = Object.keys(state.options).map(id => parseInt(id));
            const paramMultipleChoiceFieldOptionIds = new Set(Array.from(multipleChoiceFieldMultipleChoiceFieldOptionIds).filter((multipleChoiceFieldMultipleChoiceFieldOptionId) => {
                return currentMultipleChoiceFieldOptionIds.indexOf(multipleChoiceFieldMultipleChoiceFieldOptionId) === -1;
            }));

            if (paramMultipleChoiceFieldOptionIds.size === 0) {
                return new Promise(resolve => resolve());
            }

            const url = 'http://localhost:8003/api/v1/multiple_choice_field_options/';
            const config = {
                params: { ids: Array.from(paramMultipleChoiceFieldOptionIds) }
            };

            return dispatch('get', { url, config }).then((multipleChoiceFieldOptions) => {
                commit('addMultipleChoiceOptions', multipleChoiceFieldOptions);

                const optionIds = multipleChoiceFieldOptions.reduce((acc, multipleChoiceFieldOption) => {
                    acc.add(multipleChoiceFieldOption.option);

                    return acc;
                }, new Set());

                return dispatch('getOptions', optionIds);
            });
        },
        getOptions({ commit, dispatch, state }, optionIds) {
            const currentOptionIds = Object.keys(state.options).map(id => parseInt(id));
            const paramOptionIds = new Set(Array.from(optionIds).filter((optionId) => {
                return currentOptionIds.indexOf(optionId) === -1;
            }));

            if (paramOptionIds.size === 0) {
                return new Promise(resolve => resolve());
            }

            const url = 'http://localhost:8003/api/v1/options/';
            const config = {
                params: { ids: Array.from(paramOptionIds) }
            };

            return dispatch('get', { url, config }).then((options) => {
                commit('addOptions', options);
            });
        },
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
            Object.assign(state, defaultState());
        }
    }
});