<template>
  <div>
    <h3>Q. 언제 여행을 떠나시나요?</h3>
    <br>
    <v-row justify="center">
        <v-date-picker
        v-model="picker"
        color="#356859"
        header-color="#356859"
        full-width
        ></v-date-picker>
    </v-row>
  </div>
</template>

<script>
export default {
    name: 'FirstOption',
    data () {
      return {
        picker: new Date().toISOString().substr(0, 10),
      }
    },
    
}
</script>

<style>

</style>