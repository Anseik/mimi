<template>
  <div>
    <v-container fluid class="backcolor" @click="RestaurantDetail">
      <v-simple-table dense>
        <template v-slot:default>
          <tbody>
            <tr>
              <th style="width: 100px">
                <v-img :src="restaurantItem.image" style="width: 100px; border-radius: 20px;"></v-img>

              </th>
              <th class="text-left">
                {{restaurantItem.title}}<br>
                {{restaurantItem.address}}<br>
                {{restaurantItem.info}}<br>
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
                    <v-card-title>음식점을 저장하세요.</v-card-title>
                    <p>해당날짜</p>
                    <v-divider></v-divider>
                    <v-card-text style="height: 100px;">
                      <v-radio-group
                        v-model="dialogm1"
                        
                      >
                        <v-radio
                          label="아침"
                          value="breakfast"
                        ></v-radio>
                        <v-radio
                          label="점심"
                          value="lunch"
                        ></v-radio>
                        <v-radio
                          label="저녁"
                          value="dinner"
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
    name: 'RestaurantItem',
    props: {
      restaurantItem: Object
    },
    data () {
      return {
        dialogm1: '',
        dialog: false,
      }
    },
    methods: {
      RestaurantDetail() {
        this.$router.push({ name: 'RestaurantDetail' })
      },
      
    }
}
</script>

<style scoped>
.backcolor {
  background-color: white;
  border-radius: 20px;
}
</style>