<template>
    <div v-if='initialized'>
        <h4>{{ text }}</h4>
        <Field
            :fieldClass='fieldClass'
            :id='fieldId'
        />
    </div>
</template>

<script>
import axios from 'axios';
import Field from '@components/Field';

export default {
    components: { Field },
    data() {
        return {
            fieldId: undefined,
            fieldClass: undefined,
            text: undefined
        }
    },
    computed: {
        initialized() {
            return this.fieldId !== undefined &&
                this.fieldClass !== undefined &&
                this.text !== undefined;
        }
    },
    props: {
        id: {
            required: true,
            type: Number
        }
    },
    beforeMount() {
        const self = this;

        axios.get(`http://localhost:8003/api/v1/questions/${this.id}/`)
            .then((resp) => {
                const question = resp.data;

                self.fieldId = question.field;
                self.fieldClass = question.field_class;
                self.text = question.text;
            });
    },
};
</script>