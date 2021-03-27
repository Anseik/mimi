<template>
  <v-container fluid>
    <router-link style="text-decoration: none; color: black;" :to="{ name: 'RestaurantDetail' }">
      <v-row no-gutters>
        <v-col style="margin-right:-16px">
          <v-img :src="restaurantItem.image" style="width: 100px"></v-img>
        </v-col>
        <v-col style="text-align: baseline">
          <v-rows style="text-justify: center">
            <v-row>
          {{restaurantItem.title}}
            </v-row>
            <v-row>
          {{restaurantItem.address}}
            </v-row>
            <v-row>
          {{restaurantItem.avhscore}}
            </v-row>
          </v-rows>
        </v-col>
      </v-row>
      <v-divider style="width: 100%"></v-divider>
    </router-link>
    
  </v-container>
</template>

<script>
export default {
    name: 'RestaurantItem',
    props: {
      restaurantItem: Object
    },
    // methods: {
    //   gotoLink() {
    //     this.$router.push({ name: 'TravelDetail' })
    //   }
    // }
}
</script>

<style>

</style>