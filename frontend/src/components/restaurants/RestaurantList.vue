<template>
  <v-card
    max-width="450"
    class="mx-auto"
  >
    <v-list three-line>
      <template v-for="(item, index) in items">

        <v-divider
          v-if="item.divider"
          :key="index"
          :inset="item.inset"
        ></v-divider>

        <v-list-item
          v-else
          :key="item.title"
        >
          <v-list-item-image>
            <v-img :src="item.image"></v-img>
          </v-list-item-image>
          
          <v-list-item-content style="margin-left:-150px;">
            <v-list-item-title v-html="item.title"></v-list-item-title>
            <v-list-item-address v-html="item.address"></v-list-item-address>
            <v-list-item-opentime v-html="item.opentime"></v-list-item-opentime>
            <v-list-item-avgscore v-html="item.avgscore"></v-list-item-avgscore>
          </v-list-item-content>
        </v-list-item>
      </template>
    </v-list>
  </v-card>
</template>

<script>
export default {
    data: () => ({
      items: [
        {
          image: 'https://picsum.photos/100',
          title: '식당이름',
          address: '주소',
          opentime: '영업시간',
          avgscore: '평점',
        },
        { divider: true, inset: true },
        {
          image: 'https://picsum.photos/100',
          title: '식당이름',
          address: '주소',
          opentime: '영업시간',
          avgscore: '평점',        },
        { divider: true, inset: true },
      ],
    }),
  }
</script>

<style>

</style>