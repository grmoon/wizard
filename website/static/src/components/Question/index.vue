<template>
    <div
        v-if='initialized'
        class='question'
    >
        <h4>{{ question.text }}</h4>
        <Field
            @activate='field_onActivate'
            @deactivate='field_onDeactivate'
            :answer='answer'
            :fieldClass='question.field_class'
            :id='question.field'
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
            answer: undefined
        }
    },
    computed: {
        ...mapFieldState({
            field({ fields }) {
                return fields[this.question.field];
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
            return this.answer !== undefined;
        }
    },
    props: {
        question: {
            required: true,
            type: Object
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
        getAnswer() {
            const self = this;

            if (this.question.answer === null) {
                self.answer = {
                    question: this.question.id,
                    value: null
                }
            }
            else {
                axios.get(`http://localhost:8003/api/v1/answers/${this.question.answer}/`)
                    .then((resp) => {
                        self.answer = resp.data;
                    });
            }
        }
    },
    beforeMount() {
        this.getAnswer();
    },
};
</script>