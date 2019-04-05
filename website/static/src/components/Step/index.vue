<template>
    <div v-if='initialized'>
        <h2>Step {{ step.position }}</h2>
        <Section
            v-for='(section, index) in sections'
            :section='section'
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
            sections: undefined
        }
    },
    computed: {
        initialized() {
            return this.sections !== undefined;
        }
    },
    props: {
        step: {
            required: true,
            type: Object
        }
    },
    methods: {
        getSections() {
            const self = this;
            const promises = this.step.sections.map(this.getSection);

            Promise.all(promises).then((sections) => {
                sections.sort((section1, section2) => {
                    return section1.position - section2.position;
                });

                self.sections = sections
            });
        },
        getSection(sectionId) {
            return axios.get(`http://localhost:8003/api/v1/sections/${sectionId}/`)
                .then(resp => resp.data);
        }
    },
    beforeMount() {
        this.getSections();
    }
}
</script>