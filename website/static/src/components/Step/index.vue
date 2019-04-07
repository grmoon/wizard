<template>
    <div v-if='initialized'>
        <h2>{{ step.name }}</h2>
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
import sortByPosition from '@utils/sortByPosition';

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
    watch: {
        step() {
            this.initialize();
        }
    },
    methods: {
        initialize() {
            this.getSections();
        },
        getSections() {
            const self = this;
            const promises = this.step.sections.map(this.getSection);

            Promise.all(promises).then((sections) => {
                sections.sort(sortByPosition);

                self.sections = sections.map(section => section.section);
            });
        },
        getSection(sectionId) {
            return axios.get(`http://localhost:8003/api/v1/step_sections/${sectionId}/`).then(resp => resp.data);
        }
    },
    beforeMount() {
        this.initialize();
    }
}
</script>