<template>
  <div>
  <v-sheet
    class="mx-auto my-5"
  >
    <v-slide-group
      multiple
      show-arrows
    >
      <v-slide-item
        v-for="n in 5"
        :key="n"
        v-slot="{ active, toggle }"
      >
        <v-btn
          class="mx-2"
          :input-value="active"
          active-class="purple white--text"
          depressed
          rounded
          @click="toggle"
        >
          Keyword {{ n }}
        </v-btn>
      </v-slide-item>
    </v-slide-group>
  </v-sheet>
  <RestaurantList />
  </div>
</template>

<script>
import RestaurantList from '@/components/restaurants/RestaurantList.vue'
export default {
  name: 'Keyword',
  components: {
    RestaurantList,
  }
}
</script>

<style>

</style>