<template>
  <div>
    <v-row cols=12 class="ma-0 pa-3">
      <v-col cols="1">
        <v-icon color="#AB47BC">mdi-map-marker-radius-outline</v-icon>
      </v-col>
      <v-col cols="10" class="pl-4">
        <p class="mb-0">가게 주소</p>
      </v-col>
    </v-row>
    <v-row style="width: 90%; margin-left: 5%" class="mt-0 mb-0">
      <v-divider></v-divider>
    </v-row>
    <v-row cols=12 class="ma-0 pa-3">
      <v-col cols="1">
        <v-icon color="#AB47BC">mdi-clock-time-four-outline</v-icon>
      </v-col>
      <v-col cols="10" class="pl-4">
        <p class="mb-0">가게 영업 시간</p>
      </v-col>
    </v-row>
    <v-row style="width: 90%; margin-left: 5%" class="mt-0 mb-0">
      <v-divider></v-divider>
    </v-row>
    <v-row cols=12 class="ma-0 pa-3">
      <v-col cols="1">
        <v-icon color="#AB47BC">mdi-phone-outline</v-icon>
      </v-col>
      <v-col cols="10" class="pl-4">
        <p class="mb-0">가게 전화번호</p>
      </v-col>
    </v-row>
    <v-row style="width: 90%; margin-left: 5%" class="mt-0 mb-0">
      <v-divider></v-divider>
    </v-row>
    <v-row cols=12 class="ma-0 pa-3">
      <v-col cols="1">
        <v-icon color="#AB47BC">mdi-silverware</v-icon>
      </v-col>
      <v-col cols="10" class="pl-4">
        <p class="mb-0">가게 메뉴</p>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {

}
</script>

<style>
.justifycenter {
  justify-content: center;
}
</style>