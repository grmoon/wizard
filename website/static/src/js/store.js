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
        multipleChoiceOptions: {},
        options: {},
        questions: {},
        sectionQuestions: undefined,
        sections: undefined,
        step: undefined,
        stepSections: undefined,
        triggers: {},
        wizardStep: undefined,
        uploads: {},
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

            return dispatch('get', { url, config }).then(({
                wizard_step: wizardStep,
                step,
                step_sections: stepSections,
                sections,
                section_questions: sectionQuestions,
                questions,
                fields,
                answers,
                triggers,
                multiple_choice_options: multipleChoiceOptions,
                options,
                uploads,
            }) => {
                commit('setWizardStep', wizardStep);
                commit('setStep', step);
                commit('setStepSections', stepSections);
                commit('setSections', sections);
                commit('setSectionQuestions', sectionQuestions);
                commit('setFields', fields);
                commit('setTriggers', triggers);
                commit('setMultipleChoiceOptions', multipleChoiceOptions);
                commit('setOptions', options);
                commit('setQuestions', questions);
                commit('setAnswers', answers);
                commit('setUploads', uploads);
            });
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
                    'Content-Type': 'multipart/form-data',
                    'X-CSRFToken': Cookies.get('csrftoken'),
                }
            }

            return axios.post(url, payload, _config).then(resp => resp.data);
        },
        saveAnswers({ state, commit, dispatch }) {
            const temp = 'http://localhost:8003/api/v1/answers/bulk/';
            const formData = new FormData();
            const jsonAnswers = [];
            const fileAnswers = [];
            let fileIndex = 0;

            Object.values(state.answers)
                .filter(answer => answer.value !== null)
                .forEach((answer) => {
                    const _answer = {
                        question_id: answer.question,
                        user_id: answer.user,
                    };

                    if (answer.id !== null) {
                        _answer['id'] = answer.id;
                    }

                    if (answer.value instanceof FileList) {
                        _answer['file_indices'] = [];

                        Array.from(answer.value).forEach((file) => {
                            const currentFileIdx = fileIndex++;
                            _answer['file_indices'].push(currentFileIdx);
                            formData.append(`files`, file);
                        });

                        fileAnswers.push(_answer);
                    }
                    else {
                        _answer['value'] = answer.value;
                        jsonAnswers.push(_answer);
                    }
                });

            formData.append('file_answers', JSON.stringify(fileAnswers));
            formData.append('json_answers', JSON.stringify(jsonAnswers));

            return dispatch('post', { url: temp, payload: formData }).then(({ answers, uploads }) => {
                commit('updateUploads', uploads);
                commit('updateAnswers', answers);

                return answers;
            });
        },
        delete(store, { url, config={} }) {
            const _config = {
                ...config,
                headers: {
                    'X-CSRFToken': Cookies.get('csrftoken'),
                }
            }

            return axios.delete(url, _config).then(resp => resp.data);
        },
        deleteUploads({ state, dispatch }, uploadIds) {
            const url = 'http://localhost:8003/api/v1/uploads/bulk/';
            const config = {
                params: {
                    upload_ids: uploadIds,
                }
            }

            return dispatch('delete', { url, config }).then((uploads) => {
                uploads.forEach((upload) => {
                    Vue.delete(state.uploads, upload.answer);
                });
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
        setQuestions(state, questions) {
            questions.forEach((question) => {
                Vue.set(state.questions, question.id, question);
            });
        },
        updateAnswers(state, answers) {
            answers.forEach((answer) => {
                Vue.set(state.answers, answer.question, answer);
            });
        },
        updateUploads(state, uploads) {
            uploads.forEach((upload) => {
                if (!(upload.answer in state.uploads)) {
                    Vue.set(state.uploads, upload.answer, []);
                }

                state.uploads[upload.answer].push(upload);
            });
        },
        setAnswers(state, answers) {
            const answersByQuestion = answers.reduce((acc, answer) => {
                acc[answer.question] = answer;
                return acc;
            }, {});

            Object.keys(state.questions).forEach((questionId) => {
                let answer;

                if (questionId in answersByQuestion) {
                    answer = answersByQuestion[questionId];
                }
                else {
                    const question = state.questions[questionId];

                    answer = {
                        question: question.id,
                        user: state.user.id,
                        value: question.default
                    };
                }

                Vue.set(state.answers, questionId, answer);
            });
        },
        setTriggers(state, triggers) {
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
        setFields(state, fields) {
            fields.forEach((field) => {
                Vue.set(state.fields, field.id, field);
            });
        },
        setMultipleChoiceOptions(state, multipleChoiceOptions) {
            multipleChoiceOptions.forEach((multipleChoiceOption) => {
                const fieldId = multipleChoiceOption.field;
                let value;

                if (fieldId in state.multipleChoiceOptions) {
                    value = {...state.multipleChoiceOptions[fieldId]};
                }
                else {
                    value = {}
                }

                value[multipleChoiceOption.option] = multipleChoiceOption;

                Vue.set(state.multipleChoiceOptions, fieldId, value);
            });
        },
        setOptions(state, options) {
            options.forEach((option) => {
                Vue.set(state.options, option.id, option);
            });
        },
        setUploads(state, uploads) {
            state.uploads = uploads.reduce((acc, upload) => {
                if (!(upload.answer in acc)) {
                    acc[upload.answer] = []
                }

                acc[upload.answer].push(upload);

                return acc;
            }, {});
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