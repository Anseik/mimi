<template>
  <div class="backimg" id="container">
      <v-timeline
        align-top
        dense
      >
        <v-timeline-item
          color="#6A1B9A"
          small
        >
          <v-row class="pt-1 pr-3">
            <v-col cols="12">
              <strong>2021-03-27</strong>
            </v-col>
            <v-col cols="4">
                <v-card
                    class="mx-auto"
                    width="100"
                    @click="moveToDetailPage"
                >
                    <v-img
                    class="white--text align-end"
                    height="100px"
                    src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
                    >
                    </v-img>

                    <v-card-subtitle class="pt-0 pb-0">
                    이름
                    </v-card-subtitle>
                </v-card>
                <div style="text-align: center;">아침</div>
            </v-col>
            <v-col cols="4" align-self="center">
                <v-card
                    class="mx-auto"
                    width="100"
                    @click="moveToDetailPage"
                >
                    <v-img
                    class="white--text align-end"
                    height="100px"
                    src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
                    >
                    </v-img>

                    <v-card-subtitle class="pt-0 pb-0">
                    이름
                    </v-card-subtitle>
                </v-card>
                <div style="text-align: center;">점심</div>
            </v-col>
            <v-col cols="4">
                <v-card
                    class="mx-auto"
                    width="100"
                    @click="moveToDetailPage"
                >
                    <v-img
                    class="white--text align-end"
                    height="100px"
                    src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
                    >
                    </v-img>

                    <v-card-subtitle class="pt-0 pb-0">
                    이름
                    </v-card-subtitle>
                </v-card>
                <div style="text-align: center;">저녁</div>
            </v-col>
          </v-row>
        </v-timeline-item>
      </v-timeline>
  </div>
</template>

<script>
export default {
    name: 'Timeline',
    methods: {
        moveToDetailPage() {
            this.$router.push({name : "RestaurantDetail"})
        },
    }

}
</script>

<style scoped>
.backimg {
  background-image: url(https://i.ibb.co/C6SCsQT/backimg.png);
  min-height: 650px;
}
</style>