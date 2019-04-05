<template>
    <div v-if='initialized'>
        <RadioButtonOption
            v-for='(option, index) in options'
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

export default {
    components: { RadioButtonOption },
    data() {
        return {
            name: undefined,
            options: undefined
        }
    },
    computed: {
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
                const options = Array.from(resp.data.options);
                options.sort();

                self.name = resp.data.name;
                self.options = options;
            });
    },
};
</script>