<template>
    <div v-if='initialized'>
        <h2>Step {{ position }}</h2>
        <Section
            v-for='(section, index) in sections'
            :id='section'
            :key='index'
        />
    </div>
</template>

<script>
import axios from 'axios';
import Section from '@components/Section';

export default {
    components: { Section },
    data() {
        return {
            sections: undefined,
            position: undefined
        }
    },
    computed: {
        initialized() {
            return this.sections !== undefined &&
                this.position !== undefined;
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

        axios.get(`http://localhost:8003/api/v1/steps/${this.id}/`)
            .then((resp) => {
                const step = resp.data;
                const sections = step.sections;

                sections.sort((section1, section2) => section1 - section2);

                self.sections = sections;
                self.position = step.position;
            });
    }
}
</script>