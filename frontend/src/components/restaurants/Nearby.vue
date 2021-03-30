<template>
  <div class="text-center">
    <v-row justify="end" class="pt-3 pr-3">
      <v-menu>
        <template v-slot:activator="{ attrs, on }">
          <v-chip
            color="#6A1B9A"
            class="ma-3"
            v-bind="attrs"
            v-on="on"
            outlined
            rounded
            small>
            카테고리
          </v-chip>
        </template>

        <v-list>
          <v-list-item
          v-for="item in items"
          :key="item"
          link
          >
          <v-list-item-title v-text="item"></v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    

      <v-chip
        class="ma-3"
        color="#6A1B9A"
        outlined
        small
      >
        최근 음식 제외
      </v-chip>
      <v-chip
        class="ma-3"
        color="#6A1B9A"
        outlined
        small
      >
        별점 많은 순
      </v-chip>
    </v-row>

    <v-row justify="end" class="pr-3">
      <v-chip
        class="ma-2"
        color="#6A1B9A"
        outlined
        small
      >
        리뷰 많은 순
      </v-chip>
      <v-chip
        class="ma-2"
        color="#6A1B9A"
        outlined
        small
      >
        재방문 많은 순
      </v-chip>
    </v-row>
    <br>
    <br>
    <RestaurantList></RestaurantList>
  </div>
</template>

<script>
import RestaurantList from '@/components/restaurants/RestaurantList.vue';

export default {
  name: 'Nearby',
  components: {
    RestaurantList
  },
  data: () => ({
      items: ['한식', '양식', '중식', '일식'],
    }),
}
</script>

<style scoped>
.font-weight {
  font-weight: bolder;
}
</style>