<template>
  <div>
    <Course></Course>
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
}
</script>

<style>

</style>