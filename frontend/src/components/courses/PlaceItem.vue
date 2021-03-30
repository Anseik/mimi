<template>
  <div>
    <v-container fluid class="backcolor" @click="traveldetail">
      <v-simple-table dense>
        <template v-slot:default>
          <tbody>
            <tr>
              <th style="width: 100px">
                <v-img :src="placeItem.image" style="width: 100px; border-radius: 20px;"></v-img>

              </th>
              <th class="text-left">
                {{placeItem.title}}<br>
                {{placeItem.address}}<br>
                {{placeItem.info}}<br>
              </th>
              <th class="text-right">
                <v-dialog v-model="dialog" max-width="290">
                  <template v-slot:activator="{ on, attrs }">
                  <v-btn
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
                    <v-card-title>관광지 번호에 저장하세요.</v-card-title>
                    <v-divider></v-divider>
                    <v-card-text style="height: 150px;">
                      <v-radio-group
                        v-model="dialogm1"
                      >
                        <v-radio
                          label="1번 관광지"
                          value="one"
                        ></v-radio>
                        <v-radio
                          label="2번 관광지"
                          value="two"
                        ></v-radio>
                        <v-radio
                          label="3번 관광지"
                          value="three"
                        ></v-radio>
                        <v-radio
                          label="4번 관광지"
                          value="four"
                        ></v-radio>
                      </v-radio-group>
                    </v-card-text>
                    <v-card-actions>
                      <v-btn
                        color="black"
                        text
                        @click="dialog = false"
                      >
                        닫기
                      </v-btn>
                      <v-btn
                        color="black"
                        text
                        @click="dialog = false"
                      >
                        저장
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
              </th>
            </tr>
          </tbody>
        </template>
  </v-simple-table>

    </v-container>
    <div style="line-height:50%;">
      <br>
    </div>
  </div>
</template>

<script>
export default {
    name: 'PlaceItem',
    props: {
      placeItem: Object
    },
    data () {
      return {
        dialogm1: '',
        dialog: false,
      }
    },
    methods: {
      traveldetail() {
        this.$router.push({ name: 'TravelDetail' })
      }
    }
}
</script>

<style scoped>
.backcolor {
  background-color: white;
  border-radius: 20px;
}
</style>