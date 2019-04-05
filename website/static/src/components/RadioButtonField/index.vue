<template>
    <div v-if='initialized'>
        <RadioButtonOption
            v-for='(option, index) in options'
            @activate='option_onActivate'
            :key='index'
            :name='name'
            :option='option'
            :selectedValue='answer.value'
        />
    </div>
</template>

<script>
import axios from 'axios';
import RadioButtonOption from '@components/RadioButtonOption';
import { createNamespacedHelpers } from 'vuex';

const { mapState: mapTriggerState } = createNamespacedHelpers('triggers');
const { mapMutations: mapFieldMutations } = createNamespacedHelpers('fields');

export default {
    methods: {
        ...mapFieldMutations(['addField']),
        option_onActivate({ triggerIds, value }) {
            this.$emit('deactivate', this.activeTriggerIds);
            this.$emit('activate', triggerIds);
        },
        getField() {
            const self = this;

            return axios.get(`http://localhost:8003/api/v1/radio_button_fields/${this.id}/`)
                .then((resp) => {
                    const field = resp.data;

                    self.name = field.name;
                    self.addField(field);

                    return field;
                });
        },
        getOptions(field) {
            const self = this;
            const promises = field.options.map(this.getOption);

            Promise.all(promises).then((options) => {
                options.sort((option1, option2) => {
                    return option1.position - option2.position;
                });

                self.options = options;
            });
        },
        getOption(optionId) {
            return axios.get(`http://localhost:8003/api/v1/radio_button_options/${optionId}/`)
                .then(resp => resp.data);
        },
        initialize() {
            this.getField().then(this.getOptions);
        }
    },
    components: { RadioButtonOption },
    data() {
        return {
            name: undefined,
            options: undefined
        }
    },
    computed: {
        ...mapTriggerState({
            triggerIds({ triggersByFieldName }) {
                return triggersByFieldName[this.name] || {};
            },
            activeTriggerIds({ triggers }) {
                return Object.values(this.triggerIds).filter(triggerId => triggers[triggerId].active);
            }
        }),
        initialized() {
            return this.name !== undefined && this.options !== undefined;
        },
    },
    props: {
        answer: {
            required: true,
            type: Object
        },
        id: {
            required: true,
            type: Number
        }
    },
    beforeMount() {
        this.initialize();
    }
};
</script>