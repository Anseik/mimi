<template>
  <div>
    <h3>Q. 관심있는 여행 테마는 무엇인가요?</h3>
    <v-row justify="center">
        <v-col cols="12">
            <div class="pa-6">
            <v-chip-group
                active-class="green--text"
                column
            >
                <v-chip
                v-for="tag in tags"
                :key="tag"
                outlined
                color="#356859"
                >
                {{ tag }}
                </v-chip>
            </v-chip-group>
            </div>
        </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
    name: 'ThirdOption',
    data: () => ({
      tags: [
        '산',
        '바다',
        '공원',
        '전망대',
        '테마파크',
        '문화시설',
        '박물관/기념관',
        '문화마을',
        '온천',
        '섬',
        '강/호수',
        '촬영지',
        '액티비티/체험활동',
        '캠핑',
        '동굴',
        '산책로',
        '전통시장',
        '랜드마크',
        '계곡/폭포',
      ],
    }),
}
</script>

<style>

</style>