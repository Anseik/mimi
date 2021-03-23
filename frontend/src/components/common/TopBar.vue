<template>
  <div>
    <!-- <v-app-bar
      color="deep-purple accent-4"
      dense
      dark
    >
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-spacer></v-spacer>

      <v-toolbar-title>미미여지도</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-book</v-icon>
      </v-btn>
    </v-app-bar> -->
    
    <v-toolbar class="nav" style="height: 50px">
      <v-toolbar-title
        style="margin-top: -1%; margin-left: 35%"
      >
        <label style="color: #f9a825">미미여지도</label>
      </v-toolbar-title>
    </v-toolbar>
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

  },
}
</script>

<style>

</style>