<template>
  <v-bottom-navigation
    color="primary"
  >
    <v-btn>
      <span>홈</span>

      <v-icon>mdi-home</v-icon>
    </v-btn>

    <v-btn>
      <span>여행코스</span>

      <v-icon>mdi-bag-suitcase-outline</v-icon>
    </v-btn>

    <v-btn>
      <span>타임라인</span>

      <v-icon>mdi-account-clock-outline</v-icon>
    </v-btn>
  </v-bottom-navigation>
</template>

<script>
export default {
  name: 'BottomBar',
  components: {

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