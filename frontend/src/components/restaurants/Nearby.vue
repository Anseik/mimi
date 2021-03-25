<template>
  <div class="text-center">
    <v-row style="margin-top: 5px;">
      <v-menu>
        <template v-slot:activator="{ attrs, on }">
          <v-chip
            color="indigo darken-3"
            v-bind="attrs"
            v-on="on"
            outlined
            rounded
          >
            카테고리
          </v-chip>
        </template>

        <v-list>
          <v-list-item
          v-for="item in items"
          :key="item"
          link
          >
          <v-list-item-title v-text="item"></v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-row>

    <v-chip
      class="ma-2"
      color="indigo darken-3"
      outlined
    >
      <v-icon left>
        mdi-cancel
      </v-icon>
      최근 음식 제외
    </v-chip>
    <v-chip
      class="ma-2"
      color="indigo darken-3"
      outlined
    >
      <v-icon left>
        mdi-star
      </v-icon>
      별점 많은 순
    </v-chip>
    <v-chip
      class="ma-2"
      color="indigo darken-3"
      outlined
    >
      <v-icon>mdi-pencil</v-icon>
      리뷰 많은 순
    </v-chip>
    <v-chip
      class="ma-2"
      color="indigo darken-3"
      outlined
    >
      <v-icon left>
        mdi-heart
      </v-icon>
      재방문 많은 순
    </v-chip>
  </div>
</template>

<script>
export default {
  name: 'Nearby',
  data: () => ({
      items: ['한식', '양식', '중식', '일식'],
    }),
}
</script>

<style scoped>
.font-weight {
  font-weight: bolder;
}
</style>