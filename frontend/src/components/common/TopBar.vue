<template>
  <div>
    <v-app-bar
      color="deep-purple accent-4"
      dense
      dark
    >
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-spacer></v-spacer>

      <v-toolbar-title>미미여지도</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon @click="moveToDiary">
        <v-icon>mdi-book</v-icon>
      </v-btn>
    </v-app-bar>
  </div>
</template>

<script>
export default {
  name: 'TopBar',
  components: {

  },
  data: () => ({
    //
  }),
  methods: {
    moveToDiary() {
      console.log('다이어리로 이동')
      this.$router.push({name : "Diary"})
    }
  },
}
</script>

<style>

</style>