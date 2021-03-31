<template>
  <div>
    <!-- <v-sheet
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
    </v-sheet> -->
  <wordcloud
    :data="defaultWords"
    nameKey="name"
    valueKey="value"
    class="description"
    :color="myColors"
    :showTooltip="false"
    :wordClick="wordClickHandler">
  </wordcloud>  
  <RestaurantList />
  </div>
</template>

<script>
import RestaurantList from '@/components/restaurants/RestaurantList.vue'
import wordcloud  from 'vue-wordcloud'
export default {
  name: 'Keyword',
  components: {
    RestaurantList,
    wordcloud ,
  },
  data: () => ({
    myColors: ['#1f77b4', '#629fc9', '#94bedb', '#c9e0ef'],
    defaultWords: [{
        "name": "따뜻한",
        "value": 26,
      },
      {
        "name": "가족",
        "value": 19
      },
      {
        "name": "연인",
        "value": 18
      },
      {
        "name": "분위기",
        "value": 16
      },
      {
        "name": "편안한",
        "value": 15
      },
      {
        "name": "가성비",
        "value": 9
      },
      {
        "name": "데이트",
        "value": 9
      },
      {
        "name": "친구",
        "value": 9
      },
      {
        "name": "비오는날",
        "value": 6
      }
    ]
  }),
  methods: {
    wordClickHandler(name, value, vm) {
      console.log('wordClickHandler', name, value, vm)
    }
  },
}
</script>

<style scoped>
  .description {
    font-family: "NanumBarunGothic", Helvetica, Arial;
  }
</style>