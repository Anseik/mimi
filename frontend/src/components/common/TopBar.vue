<template>
  <div>
    <v-toolbar class="nav" style="height: 50px">
      <v-toolbar-title
        style="margin-top: -1%; margin-left: 35%;"
      >
        <label>미미여지도</label>
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
    moveToDiary() {
      console.log('다이어리로 이동')
      this.$router.push({name : "Diary"})
    }
  },
}
</script>

<style>

</style>