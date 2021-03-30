<template>
  <div class="text-center">
    <br>
    <br>
    <v-menu >
      <v-list>
        <v-list-item
        
        >
        <!-- <v-list-item
        v-for="item in items"
        :key="index"
        link
        > -->
        <!-- <v-list-item-title v-text="item"></v-list-item-title> -->
        </v-list-item>
      </v-list>
    </v-menu>
  

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
    <br>
    <br>
    <!-- <RestaurantList></RestaurantList> -->
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

</style>