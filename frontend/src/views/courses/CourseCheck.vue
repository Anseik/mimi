<template>
  <div class="backimgg" id="container">
      <h3>여행 코스 확인</h3>
      <v-col align="end">
        <v-btn
            class="ma-2"
            color="#AD1457"
            outlined
            >
            <span class="ts2">경로 최적화</span>
        </v-btn>
        <v-btn
            class="ma-2"
            color="#6A1B9A"
            @click="moveToCourseCheck"
            outlined
            >
            <span class="ts">다이어리 저장</span>
        </v-btn>
        <Course align="center"></Course>
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
    .ts2 {
        color: #AD1457;
        font-weight: 900;
    }
    .backimgg {
        background-image: url(https://i.ibb.co/C6SCsQT/backimg.png);
        min-height: 650px;
    }
</style>