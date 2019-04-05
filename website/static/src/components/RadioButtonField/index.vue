<template>
    <div v-if='initialized'>
        <RadioButtonOption
            v-for='(option, index) in options'
            @activate='option_onActivate'
            :id='option'
            :key='index'
            :name='name'
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
        }
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
        const self = this;

        axios.get(`http://localhost:8003/api/v1/radio_button_fields/${this.id}/`)
            .then((resp) => {
                const field = resp.data;
                const options = Array.from(field.options);
                options.sort();

                self.name = field.name;
                self.options = options;
                self.addField(field);
            });
    },
};
</script>