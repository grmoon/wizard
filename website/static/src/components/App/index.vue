<template>
    <div v-if='initialized'>
        <label>
            Wizard:
            <select v-model='wizardId'>
                <option
                    value='-1'
                    disabled
                >Select a Wizard:</option>
                <option
                    v-for='(wizard, index) in Object.values(wizards)'
                    :key='index'
                    :value='wizard.id'
                >
                {{ wizard.name }}
                </option>
            </select>
        </label>
        <Wizard
            v-if='wizardId !== -1'
            :wizard='wizard'
        />
    </div>
</template>

<script>
import Wizard from '@components/Wizard';
import axios from 'axios';

export default {
    components: { Wizard },
    computed: {
        initialized() {
            return this.wizards !== undefined;
        },
        wizard() {
            return this.wizards[this.wizardId];
        }
    },
    methods: {
        getWizards() {
            const self = this;

            axios.get('http://localhost:8003/api/v1/wizards/').then(({ data: wizards }) => {
                self.wizards = wizards.reduce((accumulator, wizard) => {
                    accumulator[wizard.id] = wizard;

                    return accumulator;
                }, {});
            });
        }
    },
    data() {
        return {
            wizards: undefined,
            wizardId: -1
        }
    },
    beforeMount() {
        this.getWizards();
    }
}
</script>