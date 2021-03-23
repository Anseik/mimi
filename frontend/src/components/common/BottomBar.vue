<template>
  <v-bottom-navigation
    :value="value"
    color="primary"
  >
    <v-btn style="margin-top: 8px; margin-right: 3px">
      <span>홈</span>
      <i class="fas fa-home fa-3x"></i>
      <!-- <v-icon>mdi-home</v-icon> -->
    </v-btn>

    <v-btn style="margin-top: 8px; margin-left: 3px; margin-right: 3px">
      <span>여행코스</span>
      <i class="fas fa-suitcase-rolling fa-3x"></i>
      <!-- <v-icon>mdi-bag-suitcase-outline</v-icon> -->
    </v-btn>

    <v-btn style="margin-top: 8px; margin-left: 3px; margin-right: 3px">
      <span>타임라인</span>
      <i class="fas fa-camera-retro fa-3x"></i>
      <!-- <v-icon>mdi-account-clock-outline</v-icon> -->
    </v-btn>

    <v-btn style="margin-top: 8px; margin-left: 3px">
      <span>다이어리</span>
      <i class="far fa-calendar-alt fa-3x"></i>
      <!-- <v-icon>event-outline</v-icon> -->
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