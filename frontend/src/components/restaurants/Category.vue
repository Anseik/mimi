<template>
  <div>
    <v-card>
      <v-tabs
        dark
        background-color= "rgb(255, 218, 115)"
        show-arrows
      >
        <v-tab class="categoty-imfo" @click="clickCategory('근처')"><span class="category-color">주변맛집</span>
        </v-tab>
        <v-tab class="categoty-imfo" @click="clickCategory('키워드')"><span class="category-color">키워드맛집</span>
        </v-tab>

      </v-tabs>
    </v-card>
    <div v-if="isNearby">
    <Nearby ></Nearby>
    </div>
    <div v-else-if="!isNearby">
    <Keyword></Keyword>
    </div>
  </div>
  
</template>

<script>
import Nearby from '@/components/restaurants/Nearby.vue';
import Keyword from '@/components/restaurants/Keyword.vue';


export default {
  name: 'Category',
  components: {
    Keyword,
    Nearby,
  },
  data() {
    return {
      isKeyword: false,
      isNearby: true,
    };
  },
  methods: {
    clickCategory(categorizeItem) {
      this.isKeyword = false;
      this.isNearby = false;

      switch(categorizeItem){
        case "근처" :
          this.isNearby = true;
          break;
        case "키워드" :
          this.isKeyword = true;
          break;
      }
    }
  }

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