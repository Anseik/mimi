<template>
  <div>
      <RestaurantItem></RestaurantItem>
  </div>
</template>

<script>
import RestaurantItem from '@/components/restaurants/RestaurantItem.vue'
export default {
    name: 'RestaurantList',
    components: {
        RestaurantItem,
    },
}
</script>

<style>

</style>