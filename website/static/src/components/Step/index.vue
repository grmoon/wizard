<template>
  <div>
    <h2>{{ step.name }}</h2>
    <template v-if="sections">
      <Section
        v-for="(section, index) in sections"
        :key="index"
        :section="section"
      />
    </template>
  </div>
</template>

<script>
import Section from '@components/Section';
import { mapState} from 'vuex';

export default {
    components: { Section },
    props: {
        step: {
            required: true,
            type: Object
        }
    },
    computed: mapState(['sections'])
}
</script>