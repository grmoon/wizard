<template>
    <div v-if='initialized'>
        <h1>{{ wizard.name }}</h1>
        <Step
            v-for='(step, index) in steps'
            :step='step'
            :key='index'
        />
    </div>
</template>

<script>
import axios from 'axios';
import Step from '@components/Step';
import sortByPosition from '@utils/sortByPosition';

export default {
    components: { Step },
    props: {
        wizard: {
            required: true,
            type: Object
        }
    },
    data() {
        return {
            name: undefined,
            steps: undefined,
        }
    },
    computed: {
        initialized() {
            return this.steps !== undefined;
        }
    },
    methods: {
        initialize() {
            return this.getSteps();
        },
        getSteps() {
            const self = this;
            const promises = this.wizard.steps.map(this.getStep);

            Promise.all(promises).then((steps) => {
                steps.sort(sortByPosition);

                self.steps = steps.map(step => step.step);
            });
        },
        getStep(stepId) {
            return axios.get(`http://localhost:8003/api/v1/wizard_steps/${stepId}/`).then(resp => resp.data);
        }
    },
    beforeMount() {
        this.initialize();
    }
}
</script>