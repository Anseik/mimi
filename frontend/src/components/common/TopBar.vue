<template>
  <div>
    <v-toolbar class="nav" style="height: 50px" :elevation="0">
      <v-toolbar-title
        style="margin-top: -1%; margin-left: 35%;"
      >
        <label>미미여지도</label>
      </v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon @click="logout"><v-icon>mdi-account-arrow-right </v-icon></v-btn>
    </v-toolbar>
  </div>
</template>

<script>
import { mapState } from 'vuex'
export default {
  name: 'TopBar',
  components: {

  },
  data: () => ({
    //
  }),
  methods: {
    logout() {
      this.$store.dispatch('LOGOUT')
      this.$router.push({name: 'Login'})
    }
  },
  computed: {
    ...mapState([
      'login',
      'user',
    ])
  }
}
</script>

<style>

</style>