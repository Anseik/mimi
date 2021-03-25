<template>
  <div>
      <h3>여행 코스 확인</h3>
      <v-col align="end">
        <v-btn
            class="ma-2"
            color="#FFFBE6"
            @click="moveToCourseCheck"
            >
            <span class="ts">코스 확인</span>
        </v-btn>
        </v-col>
      <Course align="center"></Course>
      <Category></Category>
  </div>
</template>

<script>
import Category from '@/components/restaurants/Category.vue'
import Course from '@/components/courses/Course.vue'
export default {
    name: 'CourseCheck',
    components: {
        Category,
        Course,
    },
}
</script>

<style>
    .ts {
        color: #356859;
        font-weight: 900;
    }
</style>