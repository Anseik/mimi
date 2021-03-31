<template>
  <div>
    <v-container v-for="n in reviewList" :key="n.content" class="pb-0">
      <v-rating
        v-model="n.score"
        background-color="#FFC107"
        color="#FFC107"
        dense
        class="pl-4 pb-2"
      ></v-rating>
      <p class="pl-5">{{ n.content }}</p>
      <v-row style="width: 90%; margin-left: 5%" class="mt-0 mb-0">
        <v-divider></v-divider>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      reviewList: [
        {score: 5, content: "앙동규 조용히좀 해"},
        {score: 3, content: "너무 시끄러워"},
      ]
    };
  }
}
</script>

<style>

</style>