<template>
  <div>
    <img src="@/assets/mimi_logo.png" alt="" width="250px" style="margin-left: 80px; margin-top: 100px" @click="restaurant">
    <v-text-field
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
  data: () => ({
    //
  }),
  methods: {
      restaurant() {
        this.$router.push('/Category')
      }
  },
}
</script>

<style>

</style>