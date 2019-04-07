<template>
    <div>
        <h2>{{ step.name }}</h2>
        <template v-if='sections'>
            <Section
                v-for='(section, index) in sections'
                :section='section'
                :key='index'
            />
        </template>
    </div>
</template>

<script>
import Section from '@components/Section';
import { mapState} from 'vuex';

export default {
    components: { Section },
    computed: mapState(['sections']),
    props: {
        step: {
            required: true,
            type: Object
        }
    }
}
</script>