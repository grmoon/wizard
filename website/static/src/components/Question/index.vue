<template>
    <div
        v-if='initialized'
        class='question'
    >
        <h4>{{ text }}</h4>
        <Field
            @activate='field_onActivate'
            @deactivate='field_onDeactivate'
            :answer='answer'
            :fieldClass='fieldClass'
            :id='fieldId'
        />
        <div
            v-if='triggers.length > 0'
            class='subquestions'
        >
            <Question
                v-for='(trigger, index) in triggers'
                :key='index'
                :id='trigger.question'
            />
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import Field from '@components/Field';
import { createNamespacedHelpers } from 'vuex';

const {
    mapState: mapTriggerState,
    mapMutations: mapTriggerMutations
} = createNamespacedHelpers('triggers');
const { mapState: mapFieldState } = createNamespacedHelpers('fields');

export default {
    components: { Field },
    name: 'Question',
    data() {
        return {
            answer: undefined,
            fieldId: undefined,
            fieldClass: undefined,
            text: undefined
        }
    },
    computed: {
        ...mapFieldState({
            field({ fields }) {
                return fields[this.fieldId];
            }
        }),
        ...mapTriggerState({
            triggers({ triggers: allTriggers, triggersByFieldName }) {
                let triggerIds;

                if (this.field === undefined) {
                    triggerIds = []
                }
                else {
                    triggerIds = triggersByFieldName[this.field.name];
                }

                let triggers;

                if (triggerIds === undefined) {
                    triggers = []
                }
                else {
                    triggers = triggerIds.map(triggerId => allTriggers[triggerId]);
                }

                return triggers.filter(trigger => trigger.active);
            }
        }),
        initialized() {
            return this.fieldId !== undefined &&
                this.fieldClass !== undefined &&
                this.text !== undefined &&
                this.answer !== undefined
        }
    },
    props: {
        id: {
            required: true,
            type: Number
        }
    },
    methods: {
        ...mapTriggerMutations(['activate', 'deactivate']),
        field_onActivate(triggerIds) {
            triggerIds.forEach(this.activate);
        },
        field_onDeactivate(triggerIds) {
            triggerIds.forEach(this.deactivate);
        },
        initialize() {
            this.getQuestion().then(this.getAnswer);
        },
        getQuestion() {
            const self = this;

            return axios.get(`http://localhost:8003/api/v1/questions/${this.id}/`)
                .then((resp) => {
                    const question = resp.data;

                    self.fieldId = question.field;
                    self.fieldClass = question.field_class;
                    self.text = question.text;

                    return question;
                });
        },
        getAnswer(question) {
            const self = this;

            if (question.answer === null) {
                self.answer = {
                    question: question.id,
                    value: null
                }
            }
            else {
                axios.get(`http://localhost:8003/api/v1/answers/${question.answer}/`)
                    .then((resp) => {
                        self.answer = resp.data;
                    });
            }
        }
    },
    beforeMount() {
        this.initialize()
    },
};
</script>