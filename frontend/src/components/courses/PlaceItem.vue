<template>
  <div>
    <v-container fluid class="backcolor">
      <router-link style="text-decoration: none; color: black;" :to="{ name: 'TravelDetail' }">
        <v-row no-gutters>
          <v-col style="margin-right:-16px">
            <v-img :src="placeItem.image" style="width: 100px"></v-img>
          </v-col>
          <v-col style="text-align: baseline">
            <v-rows style="text-justify: center">
              <v-row>
            {{placeItem.title}}
              </v-row>
              <v-row>
            {{placeItem.address}}
              </v-row>
              <v-row>
            {{placeItem.info}}
              </v-row>
            </v-rows>
          </v-col>
        </v-row>
        <v-divider style="width: 100%"></v-divider>
      </router-link> 
    </v-container>
    <br>
  </div>
</template>

<script>
export default {
    name: 'PlaceItem',
    props: {
      placeItem: Object
    },
    // methods: {
    //   gotoLink() {
    //     this.$router.push({ name: 'TravelDetail' })
    //   }
    // }
}
</script>

<style scoped>
.backcolor {
  background-color: whitesmoke;
}
</style>