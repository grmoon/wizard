<template>
    <div v-if='initialized'>
        <h1>{{ name }}</h1>
        <Step
            v-for='(stepId, index) in stepIds'
            :id='stepId'
            :key='index'
        />
    </div>
</template>

<script>
import axios from 'axios';
import Step from '@components/Step';

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
            stepIds: undefined
        }
    },
    computed: {
        initialized() {
            return this.name !== undefined &&
                this.stepIds !== undefined;
        }
    },
    beforeMount() {
        const self = this;

        axios.get(`http://localhost:8003/api/v1/wizards/${this.id}/`)
            .then((resp) => {
                const wizard = resp.data;

                self.stepIds = wizard.steps;
                self.name = wizard.name;
            })

    }
}
</script>