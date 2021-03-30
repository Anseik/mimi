<template>
  <div id="container">
    <v-img src="@/assets/busan3.jpg" class="alignend" height="250px">
      <div class="fill-height bottom-gradient text-type">가게 이름(★5.0)</div>
    </v-img>
    <RestaurantDetailCategory></RestaurantDetailCategory>
  </div>
</template>

<script>
import RestaurantDetailCategory from "@/components/restaurants/RestaurantDetailCategory.vue";

export default {
  name: "RestaurantDetail",
  components: {
    RestaurantDetailCategory,
  },
};
</script>

<style scoped>
.bottom-gradient {
  background-image: linear-gradient(to top, rgba(0, 0, 0, 0.6) 10%, transparent 100px);
}
.text-type {
  color: white;
  font-size: 40px;
}
.alignend {
  align-items: flex-end;
}
</style>
