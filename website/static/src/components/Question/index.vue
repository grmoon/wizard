<template>
  <div class="question">
    <h4>{{ question.text }}</h4>
    <Field
      :answer="answer"
      :field="field"
    />
    <div
      v-if="activeTriggers.length > 0"
      class="subquestions"
    >
      <Question
        v-for="(trigger, index) in activeTriggers"
        :key="index"
        :question="trigger.question"
      />
    </div>
  </div>
</template>

<script>
import Field from '@components/Field';
import sortByPosition from '@utils/sortByPosition';
import checkTrigger from '@utils/checkTrigger';
import { mapState } from 'vuex';

export default {
    name: 'Question',
    components: { Field },
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
            field({ fields }) {
                return fields[this.question.field];
            },
            triggers({ questions, triggers }) {
                const _triggers = (triggers[this.question.id] || []).map((trigger) => {
                    const question = questions[trigger.to_question];

                    return {
                        ...trigger,
                        question
                    }
                });

                _triggers.sort(sortByPosition);

                return _triggers;
            }
        }),
        activeTriggers() {
            const self = this;

            const activeTriggers = this.triggers.filter((trigger) => {
                return checkTrigger(trigger, self.answer);
            });

            return activeTriggers;
        },
        initialized() {
            return this.hasAnswer && this.triggers !== undefined;
        }
    },
};
</script>