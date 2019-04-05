<template>
    <Option
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

export default {
    components: { Option },
    data() {
        return {
            label: undefined,
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
        checked() {
            return this.selectedValue == this.value;
        },
        initialized() {
            return this.label !== undefined && this.value !== undefined;
        }
    },
    beforeMount() {
        const self = this;

        axios.get(`http://localhost:8003/api/v1/radio_button_options/${this.id}/`)
            .then((resp) => {
                self.label = resp.data.label;
                self.value = resp.data.value;
            });
    }
};
</script>