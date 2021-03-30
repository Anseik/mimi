<template>
  <div class="backgroundimg" id="container">
    <div >
      <img src="@/assets/mimi_logo.png" alt="" width="50%" style="margin:25% 25% 5% 25%;">
    </div>
      <v-text-field
          solo
          label="맛집검색"
          placeholder="상호명 or 주소 를 입력하세요"
          outlined
          dense
          style="width: 80%; margin: 1% auto; margin-bottom: -6%"
          class="text"
        ></v-text-field>
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