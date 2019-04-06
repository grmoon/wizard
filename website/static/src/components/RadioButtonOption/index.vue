<template>
    <Option
        @change='option_onChange'
        type='radio'
        :checked='checked'
        :label='option.label'
        :name='name'
        :value='option.value'
    />
</template>

<style>
label {
    display: block;
}
</style>

<script>
import axios from 'axios';
import Option from '@components/Option';
import { createNamespacedHelpers } from 'vuex';

const { mapState, mapMutations } = createNamespacedHelpers('triggers');

export default {
    components: { Option },
    props: {
        option: {
            required: true,
            type: Object
        },
        name: {
            required: true,
            type: String
        },
        selectedValue: {
            required: true
        }
    },
    computed: {
        ...mapState({
            triggers({ triggers }) {
                return this.option.triggers.map(triggerId => triggers[triggerId]);
            }
        }),
        checked() {
            return this.selectedValue == this.option.value;
        }
    },
    methods: {
        ...mapMutations(['addTrigger']),
        option_onChange(event) {
            const payload = {
                triggerIds: this.option.triggers,
                value: this.option.value
            };

            this.$emit('activate', payload);
        },
        getTriggers() {
            const self = this;
            const promises = this.option.triggers.map(this.getTrigger);

            Promise.all(promises).then((triggers) => {
                triggers.forEach((trigger) => {
                    const payload = {
                        fieldName: this.name,
                        trigger: {
                            ...trigger,
                            active: this.checked,
                        }
                    }

                    this.addTrigger(payload);
                });
            });
        },
        getTrigger(triggerId) {
            return axios.get(`http://localhost:8003/api/v1/triggers/${triggerId}/`)
                .then((resp) => {
                    const trigger = resp.data

                    return this.attachQuestionToTrigger(trigger);
                });
        },
        attachQuestionToTrigger(trigger) {
            return this.getQuestion(trigger.question).then((question) => {
                return {
                    ...trigger,
                    question,
                }
            });
        },
        getQuestion(questionId) {
            return axios.get(`http://localhost:8003/api/v1/questions/${questionId}/`).then(resp => resp.data);
        }
    },
    beforeMount() {
        this.getTriggers();
    }
};
</script>