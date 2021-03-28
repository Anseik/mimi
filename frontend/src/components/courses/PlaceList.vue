<template>
    <div>
        <PlaceItem v-for="(item, index) in items" :placeItem="item" :key="index"></PlaceItem>
    </div>
</template>

<script>
import PlaceItem from '@/components/courses/PlaceItem.vue'
export default {
    name: 'PlaceList',
    components: {
        PlaceItem,
    },
     data () {
      return {
        dialog: false,
        items: [
          {
            image: 'https://picsum.photos/200',
            title: '관광지명',
            address: '주소',
            info: '시설정보',
          },
          {
            image: 'https://picsum.photos/200',
            title: '관광지명',
            address: '주소',
            info: '시설정보',
          },
        ],
      }
    },
}
</script>

<style>

</style>