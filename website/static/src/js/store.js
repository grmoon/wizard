import Vuex from 'vuex';
import Vue from 'vue';

Vue.use(Vuex);

const questions = {
    namespaced: true,
    state: {
        questions: {},
    },
    mutations: {
        addQuestion(state, question) {
            Vue.set(state.questions, question.id, question);
        }
    }
}

const fields = {
    namespaced: true,
    state: {
        fields: {},
    },
    mutations: {
        addField(state, field) {
            Vue.set(state.fields, field.id, field);
        }
    }
}

const triggers = {
    namespaced: true,
    state: {
        triggers: {},
        triggersByFieldName: {}
    },
    mutations: {
        activate(state, triggerId) {
            Vue.set(state.triggers[triggerId], 'active', true);
        },
        deactivate(state, triggerId) {
            Vue.set(state.triggers[triggerId], 'active', false);
        },
        addTrigger(state, { trigger, fieldName }) {
            if (!(fieldName in state.triggersByFieldName)) {
                Vue.set(state.triggersByFieldName, fieldName, []);
            }

            state.triggersByFieldName[fieldName].push(trigger.id);
            Vue.set(state.triggers, trigger.id, trigger);
        }
    }
}

export default new Vuex.Store({
    modules: {
        fields,
        questions,
        triggers,
    }
});