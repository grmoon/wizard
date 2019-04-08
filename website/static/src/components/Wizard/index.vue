<template>
  <div>
    <h1>{{ wizard.name }}</h1>
    <form
      v-if="initialized"
      @submit.prevent="form_onSubmit"
    >
      <input
        type="button"
        value="Save"
        @click="saveAnswers"
      >
      <Step
        v-if="step"
        :step="step"
      />
      <input
        v-if="hasPreviousStep"
        name="previous"
        type="submit"
        value="Previous"
        @click="submitButton_onClick"
      >
      <input
        v-if="hasNextStep"
        name="next"
        type="submit"
        value="Next"
        @click="submitButton_onClick"
      >
      <input
        v-else
        name="finish"
        type="submit"
        value="Finish"
        @click="submitButton_onClick"
      >
    </form>
    <div v-else>
      Loading...
    </div>
  </div>
</template>

<script>
import Step from '@components/Step';
import { mapActions, mapMutations, mapState } from 'vuex';

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
        return {
            initialized: false,
            submitSource: undefined
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
    created() {
        this.initialize();
    },
    methods: {
        ...mapActions(['getWizardStep', 'saveAnswers']),
        ...mapMutations(['resetState']),
        submitButton_onClick(event) {
            this.submitSource = event.currentTarget.name;
        },
        form_onSubmit() {
            const routeParams = {
                'next': this.nextStep,
                'previous': this.previousStep,
                'finish': {
                    name: 'done'
                }
            }[this.submitSource];

            this.saveAnswers().then(() => {
                this.$router.push(routeParams);
            });
        },
        initialize() {
            this.resetState();
            this.initialized = false;

            const params = {
                stepNum: this.stepNum,
                wizardId: this.wizard.id
            }

            return this.getWizardStep(params).then(() => {
                this.initialized = true;
            });
        },
    }
}
</script>