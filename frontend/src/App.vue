<template>
  <v-app>
    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',

  components: {

  },

  data: () => ({
    //
  }),
};
</script>
<style>
#container {
  font-family: "Do Hyeon", sans-serif;
}
@font-face {
  font-family: "NanumBarunGothic";
  src: local("NanumBarunGothic"),
    url(./fonts/NanumBarunGothic.ttf) format("truetype");
}
</style>