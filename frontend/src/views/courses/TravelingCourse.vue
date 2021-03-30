<template>
  <div id="container">
    <h3>여행 코스 추천</h3>
    <v-col align="end">
      <v-btn
          class="ma-2"
          color="#EDE7F6"
          @click="moveToCourseCheck"
          >
          <span class="ts">코스 확인</span>
      </v-btn>
    </v-col>
    <Course align="center"></Course>
    <MatchingCategory></MatchingCategory>
    <PlaceList></PlaceList>
  </div>
</template>

<script>
import Course from '@/components/courses/Course.vue'
import MatchingCategory from '@/components/courses/MatchingCategory.vue'
import PlaceList from '@/components/courses/PlaceList.vue'
export default {
  name: 'TravelingCourse',
  components: {
      Course,
      MatchingCategory,
      PlaceList,
  },
  methods: {
      moveToCourseCheck() {
      console.log('코스확인으로 이동')
      this.$router.push({name : "CourseCheck"})
      },
  },
}
</script>

<style scoped>
.ts {
    color: #6A1B9A;
    font-weight: 900;
}
</style>