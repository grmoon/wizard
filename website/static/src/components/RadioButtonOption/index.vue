<template>
    <Option
        @change='option_onChange'
        v-if='initialized'
        type='radio'
        :checked='checked'
        :label='label'
        :name='name'
        :value='value'
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
    data() {
        return {
            label: undefined,
            triggerIds: undefined,
            value: undefined
        }
    },
    props: {
        id: {
            required: true,
            type: Number
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
                return this.triggerIds.map(triggerId => triggers[triggerId]);
            }
        }),
        checked() {
            return this.selectedValue == this.value;
        },
        initialized() {
            return this.label !== undefined &&
                this.value !== undefined &&
                this.triggerIds != undefined;
        }
    },
    methods: {
        ...mapMutations(['addTrigger']),
        option_onChange(event) {
            const payload = {
                triggerIds: this.triggerIds,
                value: this.value
            };

            this.$emit('activate', payload);
        },
        initialize() {
            this.getOption().then(this.getTriggers);
        },
        getTriggers(option) {
            const self = this;
            const promises = option.triggers.map(this.getTrigger);

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
            return axios.get(`http://localhost:8003/api/v1/triggers/${triggerId}/`).then(resp => resp.data);
        },
        getOption() {
            const self = this;

            return axios.get(`http://localhost:8003/api/v1/radio_button_options/${this.id}/`)
                .then((resp) => {
                    const option = resp.data;

                    self.label = option.label;
                    self.triggerIds = option.triggers;
                    self.value = option.value;

                    return option;
                });
        }
    },
    beforeMount() {
        this.initialize();
    }
};
</script>