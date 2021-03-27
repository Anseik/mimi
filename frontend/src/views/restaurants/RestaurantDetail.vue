<template>
  <div>
    <h1>음식점 디테일 페이지</h1>
    <h2>음식점 사진, 이름, 평점 자리</h2>
    <RestaurantDetailCategory></RestaurantDetailCategory>
  </div>
</template>

<script>
import RestaurantDetailCategory from '@/components/restaurants/RestaurantDetailCategory.vue';

export default {
    name: 'RestaurantDetail',
    components: {
      RestaurantDetailCategory
    },
}
</script>

<style>

</style>