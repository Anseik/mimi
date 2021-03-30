<template>
  <div>
    <v-app-bar 
      flat 
      fixed
    >
      <v-toolbar-title>
        <label>미미여지도</label>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon @click="logout"><v-icon>mdi-account-arrow-right</v-icon></v-btn>
    </v-app-bar>
    <div style="height: 60px;"></div>
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

<style scoped>
</style>