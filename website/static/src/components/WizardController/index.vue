<template>
    <Wizard
        v-if='wizard'
        :step-num='stepNum'
        :wizard='wizard'
    />
</template>

<script>
import Wizard from '@components/Wizard';
import axios from 'axios'

export default {
    components: { Wizard },
    data() {
        return { wizard: undefined };
    },
    computed: {
        stepNum() {
            return parseInt(this.$route.params.stepNum);
        }
    },
    watch: {
        $route(oldRoute, newRoute) {
            const oldWizardId = oldRoute.params.wizardId;
            const newWizardId = newRoute.params.wizardId;

            if (oldWizardId !== newWizardId) {
                this.initialize();
            }
        }
    },
    methods: {
        getWizard(wizardId) {
            const url = `http://localhost:8003/api/v1/wizards/${wizardId}/`;

            return axios.get(url).then(resp => resp.data);
        },
        setWizard(wizard) {
            this.wizard = wizard;
        },
        initialize() {
            const wizardId = this.$route.params.wizardId;

            this.getWizard(wizardId).then(this.setWizard);
        }
    },
    created() {
        this.initialize();
    },
}
</script>