<template>
  <router-view />
</template>

<script>
import { mapActions } from 'vuex';

export default {
  created() {
    this.getUser();
  },
  methods: mapActions(['getUser']),
}
</script>