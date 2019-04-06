<template>
    <div v-if='initialized'>
        <h1>{{ name }}</h1>
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
        id: {
            required: true,
            type: Number
        }
    },
    data() {
        return {
            name: undefined,
            steps: undefined
        }
    },
    computed: {
        initialized() {
            return this.name !== undefined &&
                this.steps !== undefined;
        }
    },
    methods: {
        initialize() {
            return this.getWizard().then(this.getSteps);
        },
        getWizard() {
            const self = this;

            return axios.get(`http://localhost:8003/api/v1/wizards/${this.id}/`)
                .then(({ data: wizard }) => {
                    self.name = wizard.name;

                    return wizard;
                });
        },
        getSteps(wizard) {
            const self = this;
            const promises = wizard.steps.map(this.getStep);

            Promise.all(promises).then((steps) => {
                steps.sort(sortByPosition);

                self.steps = steps
            });
        },
        getStep(stepId) {
            return axios.get(`http://localhost:8003/api/v1/steps/${stepId}/`).then(resp => resp.data);
        }
    },
    beforeMount() {
        this.initialize();
    }
}
</script>