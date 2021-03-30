<template>
  <div id="container">
      <v-col align="end">
        <v-btn
            class="ma-2"
            color="#6A1B9A"
            outlined
            >
            <span class="ts">경로 최적화</span>
        </v-btn>
        <v-btn
            class="ma-2"
            color="#6A1B9A"
            outlined
           
            >
            <span class="ts">다이어리 저장</span>
        </v-btn>
        <Course align="center" class="pt-6"></Course>
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

<style scoped>
    .ts {
        color: #6A1B9A;
        font-weight: 900;
    }
</style>