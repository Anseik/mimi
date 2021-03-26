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


          <!-- <v-list-item-image>
            <v-img :src="item.image"></v-img>
          </v-list-item-image> -->

          <!--발표용-->
          <div>
          <v-list-item-image>
            <v-img src="@/assets/busan.jpg" style="width:100px"></v-img>
          </v-list-item-image>
          </div>
          <!--발표용-->
            <v-list-item-content style="margin-left:5px; text-align: left;">
              <v-list-item-title v-html="item.title"></v-list-item-title>
              <v-list-item-address v-html="item.address"></v-list-item-address>
              <v-list-item-opentime v-html="item.opentime"></v-list-item-opentime>
              <v-list-item-avgscore v-html="item.avgscore"></v-list-item-avgscore>
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
              <v-card-title class="headline">날짜 정보</v-card-title>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-container fluid>
                  <v-checkbox
                    v-model="selected"
                    label="아침"
                    value="John"
                    color="indigo darken-3"
                  ></v-checkbox>
                  <v-checkbox
                    v-model="selected"
                    label="점심"
                    value="Jacob"
                    color="indigo darken-3"
                  ></v-checkbox>
                  <v-checkbox
                    v-model="selected"
                    label="저녁"
                    value="Jacob"
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
    data () {
      return {
        dialog: false,
        items: [
          {
            image: '@/assets/busan.jpg',
            title: '해운대가야밀면',
            address: '부산관영시 해운대구 좌동 좌동순환로 27',
            opentime: '9:10 ~ 20:50',
            avgscore: '4.0',
          },
          { divider: true, inset: true },
          {
            image: '@/assets/busan2.jpg',
            title: '수변최고돼지국밥',
            address: '부산광역시 수영구 민락동 완안해변로 370',
            opentime: '8:00 ~ 21:30',
            avgscore: '4.4',        },
          { divider: true, inset: true },
        ],
      }
    },
  }
</script>

<style>

</style>