<template>
    <div>
        <h1>{{ wizard.name }}</h1>
        <Step
            v-if='step'
            :step='step'
        />
        <router-link
            v-if='hasPreviousStep'
            :to='previousStep'
        >Previous</router-link>
        <router-link
            v-if='hasNextStep'
            :to='nextStep'
        >Next</router-link>
    </div>
</template>

<script>
import axios from 'axios';
import Step from '@components/Step';
import sortByPosition from '@utils/sortByPosition';

export default {
    components: { Step },
    props: {
        stepNum: {
            required: true,
            type: Number
        },
        wizard: {
            required: true,
            type: Object
        }
    },
    data() {
        return { step: undefined };
    },
    computed: {
        stepParams() {
            return {
                name: 'wizard',
                params: {
                    wizardId: this.wizard.id
                }
            };
        },
        nextStep() {
            return {
                ...this.stepParams,
                params: {
                    stepNum: this.stepNum + 1,
                }
            };
        },
        previousStep() {
            return {
                ...this.stepParams,
                params: {
                    stepNum: this.stepNum - 1,
                }
            };
        },
        hasNextStep() {
            return this.stepNum < this.wizard.steps.length;
        },
        hasPreviousStep() {
            return this.stepNum > 1;
        }
    },
    watch: {
        stepNum() {
            this.initialize();
        },
        wizard() {
            this.initialize();
        }
    },
    methods: {
        initialize() {
            return this.getStep().then(this.setStep);
        },
        getStep() {
            const config = {
                params: {
                    step_num: this.stepNum,
                    wizard_id: this.wizard.id
                }
            }
            const url = 'http://localhost:8003/api/v1/wizard_steps/';

            return axios.get(url, config).then(resp => resp.data.step);
        },
        setStep(step) {
            this.step = step;
        }
    },
    created() {
        this.initialize();
    }
}
</script>