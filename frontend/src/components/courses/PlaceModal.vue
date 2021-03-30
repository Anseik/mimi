<template>
  <div class="backimg" id="container" >
    <br />
    <v-card width="90%" height="90%" style="margin: 5% 5% 5% 5%">
      <template>
        <br>
        <v-img
          :src="placeModal.image"
          width="70%"
          style="margin-left: 15%;"
        ></v-img>
        <v-card-title>
          {{ placeModal.title }}
        </v-card-title>
        <v-card-text>
          <div>
            <p>{{ placeModal.telephone }}</p>
            <p>{{ placeModal.address }}</p>
            <p>{{ placeModal.info }}</p>
          </div>
          <br>
        </v-card-text>
      </template>
      <v-card-actions>
        <v-row justify="center">
          <v-btn color="black" text plain>
            닫기
          </v-btn>
        </v-row>
      </v-card-actions>
    </v-card>
    <br>
  </div>
</template>

<script>
export default {
  props: {
    placeModal: Object,
  },
};
</script>

<style scoped>
.backimg {
  background-color: #f8e9ee;
}
</style>
