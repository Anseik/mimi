<template>
  <v-app>
    <TopBar />
    <v-main>
      <router-view />
    </v-main>
    <BottomBar />
  </v-app>
</template>

<script>
import TopBar from '@/components/common/TopBar.vue'
import BottomBar from '@/components/common/BottomBar.vue'

export default {
  name: 'Home',
  components: {
    TopBar,
    BottomBar,
  },
  data: () => ({
    //
  }),
  methods: {

  },
}
</script>

<style>

</style>