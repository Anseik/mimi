<template>
  <div>
    <div class="text-center category-background">
      <v-chip
        class="ma-3"
        color="indigo darken-3"
        outlined
      >
        전체
      </v-chip>
      <v-chip
        class="ma-3"
        color="indigo darken-3"
        outlined
      >
        80% 이상
      </v-chip>
      <v-chip
        class="ma-2"
        color="indigo darken-3"
        outlined
      >
        50% 이상
      </v-chip>
      <v-chip
        class="ma-2"
        color="indigo darken-3"
        outlined
      >
        50% 미만
      </v-chip>
      <!-- <RestaurantList></RestaurantList> -->
    </div>
  </div>
</template>

<script>
export default {
    // name: 'MatchingCategory',
}
</script>

<style scoped>
.category-color {
  font-weight: 700;
  color: rgb(50, 121, 67);
  font-size: 125%;
}
.categoty-imfo {
  padding-left: 60px;
  padding-right: 60px;
}
.category-background {
  background-color: #EEEEEE;
}

</style>