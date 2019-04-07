<template>
    <div class='question'>
        <h4>{{ question.text }}</h4>
        <Field
            :question-id='question.id'
            :field-class='question.field_class'
            :id='question.field'
        />
        <div
            v-if='activeTriggers.length > 0'
            class='subquestions'
        >
            <Question
                v-for='(trigger, index) in activeTriggers'
                :key='index'
                :question='trigger.question'
            />
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import Field from '@components/Field';
import sortByPosition from '@utils/sortByPosition';
import { mapState, mapMutations } from 'vuex';

export default {
    components: { Field },
    name: 'Question',
    props: {
        question: {
            required: true,
            type: Object
        }
    },
    computed: {
        ...mapState({
            answer({ answers }) {
                return answers[this.question.id];
            },
            triggers({ questions, triggers }) {
                return (triggers[this.question.id] || []).map((trigger) => {
                    const question = questions[trigger.to_question];

                    return {
                        ...trigger,
                        question
                    }
                });
            }
        }),
        activeTriggers() {
            const self = this;

            const activeTriggers = this.triggers.filter((trigger) => {
                return trigger.value == self.answer.value;
            });

            return activeTriggers;
        },
        initialized() {
            return this.hasAnswer && this.triggers !== undefined;
        }
    },
};
</script>