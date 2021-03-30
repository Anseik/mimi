<template>
  <div class="backgroundimg" id="container">
    <div >
      <img src="@/assets/mimi_logo.png" alt="" width="50%" style="margin:25% 25% 5% 25%;">
    </div>
    <v-row cols="12" justify="center">
      <v-col cols="7" class="pa-0">
        <v-text-field
            solo
            label="맛집검색"
            placeholder="상호명 or 주소 를 입력하세요"
            outlined
            dense
            class="text"
          ></v-text-field>
      </v-col>
      <v-btn elevation="0" height="40" min-width="40px" class="pa-0"><v-icon dark>mdi-magnify</v-icon></v-btn>
    </v-row>
  </div>
</template>

<script>
export default {
  name: 'Main',
  components: {

  },
}
</script>

<style>
.backgroundimg {
  background-image: url(https://i.ibb.co/THdNbcb/backback.jpg);
  min-height: 650px;
}
/* .backgroudcolor {
  background-color: rgba(253, 253, 253, 0.7);
  border-radius: 30px;
} */
</style>