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


          <v-list-item-image style="width: 100px">
            <v-img :src="item.image"></v-img>
          </v-list-item-image>

            <v-list-item-content style="margin-left:5px; text-align: left;">
              <v-list-item-title v-html="item.title"></v-list-item-title>
              <v-list-item-address v-html="item.address"></v-list-item-address>
              <v-list-item-opentime v-html="item.opentime"></v-list-item-opentime>
            </v-list-item-content>
          
          <!-- 버튼&모달 start -->

          <v-dialog v-model="dialog" persistent max-width="290">
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                class="mx-2"
                fab
                dark
                small
                color="indigo"
                v-bind="attrs"
                v-on="on"
              >
                <v-icon dark>
                  mdi-plus
                </v-icon>
              </v-btn>
            </template>
            <v-card>
              <v-card-title class="headline">관광지 번호에 저장하세요!</v-card-title>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-container fluid>
                  <v-checkbox
                    label="1번 관광지"
                    color="indigo darken-3"
                  ></v-checkbox>
                  <v-checkbox
                    label="2번 관광지"
                    color="indigo darken-3"
                  ></v-checkbox>
                  <v-checkbox
                    label="3번 관광지"
                    color="indigo darken-3"
                  ></v-checkbox>
                  <v-checkbox
                    label="4번 관광지"
                    color="indigo darken-3"
                  ></v-checkbox>
                  <v-btn color="green darken-1" text @click="dialog = false">저장</v-btn>
                  <v-btn color="green darken-1" text @click="dialog = false">닫기</v-btn>
                </v-container>

              </v-card-actions>
            </v-card>
          </v-dialog>

          <!-- 버튼&모달 end -->
          
        </v-list-item>
      </template>
    </v-list>
  </v-card>
</template>

<script>
export default {
    name: 'PlaceItem',
    data () {
      return {
        dialog: false,
        items: [
          {
            image: 'https://picsum.photos/200',
            title: '관광지명',
            address: '주소',
            opentime: '시설정보',
          },
          { divider: true, inset: true },
          {
            image: 'https://picsum.photos/200',
            title: '관광지명',
            address: '주소',
            opentime: '시설정보',
          },
          { divider: true, inset: true },
        ],
      }
    },
}
</script>

<style>

</style>