<template>
  <v-card width="350px" style="margin-top: 20px; margin-bottom:20px; margin-left:30px;">
    <template>
      <v-img src="@/assets/mimi_logo.png" width="100px"></v-img>
      <v-card-title>
        여행지
      </v-card-title>
      <v-card-text>
      <v-row
        align="center"
        class="mx-0"
      >
        <v-rating
          :value="4.5"
          color="amber"
          dense
          half-increments
          readonly
          size="14"
        ></v-rating>
      </v-row>
      <br>
      <div>Small plates, salads & sandwiches - an intimate setting with 12 indoor seats plus patio seating.</div>
    </v-card-text>
    </template>
  </v-card>
</template>

<script>
export default {

}
</script>

<style>

</style>