<template>
  <v-bottom-navigation style="height: 62px" fixed>
    <v-btn plain @click="moveToMain" style="margin-right: 3px;" color="#356859">
      <span>홈</span>
      <i class="fas fa-home fa-3x" style="color:#3949AB"></i>
    </v-btn>

    <v-btn plain @click="moveToCourse" style="margin-left: 3px; margin-right: 3px">
      <span>여행코스</span>
      <i class="fas fa-suitcase-rolling fa-3x" style="color:#3949AB"></i>
    </v-btn>

    <v-btn plain @click="moveToTimeline" style="margin-left: 3px; margin-right: 3px">
      <span>타임라인</span>
      <i class="fas fa-camera-retro fa-3x" style="color:#3949AB"></i>
    </v-btn>

    <v-btn plain @click="moveToDiary" style="margin-left: 3px">
      <span>다이어리</span>
      <i class="far fa-calendar-alt fa-3x" style="color:#3949AB"></i>
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
    moveToDiary() {
      this.$router.push({name : "Diary"})
    },
    moveToMain() {
      this.$router.push({name : "Main"})
    },
    moveToCourse() {
      this.$router.push({name : "SelectOption"})
    },
    moveToTimeline() {
      this.$router.push({name : "Timeline"})
    },
  },
}
</script>

<style>

</style>