<template>
    <div v-if='initialized'>
        <RadioButtonOption
            v-for='(option, index) in options'
            :key='index'
            :name='name'
            :option='option'
            :question-id='questionId'
        />
    </div>
</template>

<script>
import axios from 'axios';
import RadioButtonOption from '@components/RadioButtonOption';
import sortByPosition from '@utils/sortByPosition';
import { mapState } from 'vuex';

export default {
    methods: {
        getField() {
            const self = this;

            return axios.get(`http://localhost:8003/api/v1/radio_button_fields/${this.id}/`)
                .then(({ data: field }) => {
                    self.name = field.name;

                    return field;
                });
        },
        getOptions(field) {
            const self = this;
            const promises = field.options.map(this.getOption);

            Promise.all(promises).then((options) => {
                options.sort(sortByPosition);

                self.options = options.map(option => option.option);
            });
        },
        getOption(optionId) {
            return axios.get(`http://localhost:8003/api/v1/radio_button_field_options/${optionId}/`).then(resp => resp.data);
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
        ...mapState({
            answer({ answers }) {
                return answers[this.questionId];
            }
        }),
        initialized() {
            return this.name !== undefined && this.options !== undefined;
        },
    },
    props: {
        questionId: {
            required: true,
            type: Number
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