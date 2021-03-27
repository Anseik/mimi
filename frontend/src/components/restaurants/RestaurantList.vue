<template>
  <div>
    <RestaurantItem
      v-for="(item, index) in items"
      :restaurantItem="item"
      :key="index"
    ></RestaurantItem>
  </div>
</template>

<script>
import RestaurantItem from "@/components/restaurants/RestaurantItem.vue";
export default {
  name: "RestaurantList",
  components: {
    RestaurantItem,
  },
  data() {
    return {
      items: [
        {
          image: "https://picsum.photos/200",
          title: "해운대가야밀면",
          address: "부산관영시 해운대구 좌동 좌동순환로 27",
          avgscore: "4.0",
        },
        {
          image: "https://picsum.photos/200",
          title: "수변최고돼지국밥",
          address: "부산광역시 수영구 민락동 완안해변로 370",
          avgscore: "4.4",
        },
      ],
    };
  },
};
</script>

<style></style>
