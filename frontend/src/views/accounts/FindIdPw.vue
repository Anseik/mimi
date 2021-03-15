<template>
  <div>
    <h2><span @click="showFindId">ID찾기 / </span><span @click="showFindPw">PW 찾기</span></h2>
    <FindId v-if="isFindId" />
    <FindPw v-if="isFindPw" />
  </div>
</template>

<script>
import FindId from '@/components/accounts/FindId.vue'
import FindPw from '@/components/accounts/FindPw.vue'

export default {
  name: 'FindIdPw',
  components: {
    FindId,
    FindPw,
  },
  data: () => ({
    isFindId: true,
    isFindPw: false,
  }),
  methods: {
    showFindId() {
      this.isFindId = true
      this.isFindPw = false
    },
    showFindPw() {
      this.isFindId = false
      this.isFindPw = true
    }
  },
}
</script>

<style>

</style>