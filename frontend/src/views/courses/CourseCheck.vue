<template>
  <div>
      <h3>여행 코스 확인</h3>
      <v-col align="end">
        <v-btn
            class="ma-2"
            color="#FFFBE6"
            @click="moveToCourseCheck"
            >
            <span class="ts">다이어리 저장</span>
        </v-btn>
        </v-col>
      <Course align="center"></Course>
      <v-col align="end">
        <v-btn
            class="ma-2"
            color="#FFFBE6"
            >
            <span class="ts">경로 최적화</span>
        </v-btn>
        </v-col>
      <CourseMap align="center"></CourseMap>
      <Category></Category>
  </div>
</template>

<script>
import Category from '@/components/restaurants/Category.vue'
import Course from '@/components/courses/Course.vue'
import CourseMap from '@/components/courses/CourseMap.vue'
export default {
    name: 'CourseCheck',
    components: {
        Category,
        Course,
        CourseMap,
    },
}
</script>

<style>
    .ts {
        color: #356859;
        font-weight: 900;
    }
</style>