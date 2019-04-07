<template>
    <div>
        <h1>{{ wizard.name }}</h1>
        <template v-if='initialized'>
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
        </template>
    </div>
</template>

<script>
import axios from 'axios';
import Step from '@components/Step';
import sortByPosition from '@utils/sortByPosition';
import { mapActions, mapState } from 'vuex';

export default {
    components: { Step },
    data() {
        return {
            initialized: false
        }
    },
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
    computed: {
        ...mapState(['step']),
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
        ...mapActions(['getWizardStep']),
        initialize() {
            this.initialized = false;

            const params = {
                stepNum: this.stepNum,
                wizardId: this.wizard.id
            }

            return this.getWizardStep(params).then(() => {
                this.initialized = true;
            });
        },
    },
    created() {
        this.initialize();
    }
}
</script>